from typing import Optional, TypeVar, NamedTuple, Type

import pandas as pd

from languages import get_lang_codes, registered_languages
from signals import ExitSignal
from utils import PrettyPrintMixin, translate_dict
from validators import *

pd.set_option('display.max_columns', None)

# Common class for all validators
Validator = TypeVar('Validator', bound=AbstractValidator)


class FieldAttrs(NamedTuple):
    # Tuple of logical operations available on a field
    operations: tuple[str]
    # Reference to the Validator class for the field
    validator_class: Type[Validator]
    # Key to get the argument to initialize the validator
    validator_arg_code: str
    # Key for receiving the message that needs to be displayed when entering a field value
    input_message: str
    # Form for composing a query request when filtering
    query_form: str


# Database configuration
database_fields = {
    'date': FieldAttrs(
        operations=('==', '>', '>=', '<', '<='),
        validator_class=RegExValidator,
        validator_arg_code='date_regex',
        input_message='date_input',
        query_form='{main_arg}{operation}"{sub_arg}"'
    ),
    'type': FieldAttrs(
        operations=('==',),
        validator_class=ValueInValidator,
        validator_arg_code='values_for_type',
        input_message='type_input',
        query_form='{main_arg}{operation}"{sub_arg}"'
    ),
    'amount': FieldAttrs(
        operations=('==', '>', '>=', '<', '<='),
        validator_class=TypeValidator,
        validator_arg_code='amount_type',
        input_message='amount_input',
        query_form='{main_arg}{operation}{sub_arg}'
    ),
    'descr': FieldAttrs(
        operations=('==',),
        validator_class=None,
        validator_arg_code=None,
        input_message='descr_input',
        query_form='{main_arg}{operation}"{sub_arg}"'
    ),

}


# Handler classes
class AbstractHandler(ABC):
    """Implements the abstract method "operate" and a protected method "_get_command"."""

    def __init__(self, language: dict[str, str | dict]):
        self.language = language

    @abstractmethod
    def operate(self):
        pass

    def _get_command(self, message: str, validator: Optional[AbstractValidator] = None) -> str:
        """
        Uses the resulting validator to validate user-supplied values.
        Will require you to repeat the value entry until it passes validation.

        If the validator has not been passed, it considers any entered value to be valid.

        If the user enters "exit", it will throw an error "ExitSignal",
        which will interrupt the input at any stage of the program.
        """
        user_entered = input(message).strip()

        while validator and not validator.validate(user_entered) or user_entered == 'exit':
            if user_entered == 'exit':
                raise ExitSignal

            user_entered = input(self.language.get(validator.err_code)).strip()

        return user_entered


class SetLanguageHandler(AbstractHandler):
    def operate(self) -> dict[str, object]:
        """
        The function sets the interface language.
        The user is given a choice from all registered language packs.
        """
        # Gets a list of all registered language packs
        lang_codes = get_lang_codes()

        # Offers the user a choice of which interface language to use
        message = self.language.get('select_language').format(options=', '.join(lang_codes))
        validator = ValueInValidator(options=lang_codes)
        chosen_code = self._get_command(message, validator)

        # Returns the language pack
        return registered_languages.get(chosen_code)


class WelcomeHandler(AbstractHandler):
    def operate(self) -> bool:
        """The function welcomes the user and offers training."""
        # Receives yes/no translation for selected language
        options = self.language.get('agree_disagree')

        # Requests to the user about his desire to show tutorial
        message = self.language.get('start').format(options='/'.join(options.keys()))
        validator = ValueInValidator(options=list(options.keys()))
        show_tutorial = self._get_command(message, validator)

        # Returns user decision
        return options[show_tutorial]


class ShowTutorialHandler(AbstractHandler):
    def __init__(self, language: dict[str, str | dict], tutorial_steps: tuple[str]):
        super().__init__(language)
        self.tutorial_steps = tutorial_steps

    def operate(self) -> None:
        """
        Function iterates through the tutorials_step collection, displays the corresponding
        training item and prompts the user to continue or stop.
        """
        for step in self.tutorial_steps:
            # Receives yes/no translation for selected language
            options = self.language.get('agree_disagree')

            # Requests to the user about his desire to continue training
            message = self.language.get(step).format(options='/'.join(options.keys()))
            validator = ValueInValidator(options=list(options.keys()))
            further = self._get_command(message, validator)

            if not options[further]:
                break


Handler = TypeVar('Handler', bound=AbstractHandler)


class ChooseCommandHandler(AbstractHandler):
    def __init__(self, language: dict[str, str], commands_dict: dict[str, Handler]):
        super().__init__(language)
        self.commands = commands_dict

    def operate(self) -> Type[Handler]:
        """Function offers the user a choice of handlers registered in the "commands" collection."""
        message = self.language.get('require_input').format(
            commands=', '.join(self.commands.keys())
        )
        validator = ValueInValidator(options=self.commands.keys())
        command = self._get_command(message, validator)

        # Returns a reference to the handler class that needs to be launched
        return self.commands.get(command)


class ShowStatisticHandler(AbstractHandler, PrettyPrintMixin):
    def __init__(self, language: dict[str, str | dict], fields: dict[str, FieldAttrs]):
        super().__init__(language)
        self.database_fields = fields

    def operate(self) -> None:
        """
        Function displays statistics to the user on his income/expenses.
        The user can also get a list of database records filtered by category.
        """
        print(self.language.get('chosen_show_list'))
        df = pd.read_csv('database.csv', index_col='pk')

        if len(df) == 0:
            print(self.language.get('empty_table'))
            raise ExitSignal

        # Groups all records by income/expenses
        expense, income = df.groupby('type').amount.sum()

        print(self.language.get('statistic').format(
            summary=income - expense, income=income, expense=expense
        ))

        # Prompts the user which transaction category to display
        validator = ValueInValidator(options=self.language.get('values_for_type'))
        message = self.language.get('filter_by_type').format(
            options=', '.join(self.language.get('values_for_type').values())
        )
        display_by_type = self._get_command(message, validator)

        # The loop will run until the user enters "exit"
        while True:
            message_keys = {'income': 'income_message', 'expense': 'expense_message'}
            print(self.language.get(message_keys[display_by_type]))

            df.loc[df.type == display_by_type].apply(
                self.pprint, fields=self.database_fields, language=self.language, axis=1
            )

            display_by_type = self._get_command(message, validator)

    @translate_dict
    def _get_command(self, message: str, validator: Optional[callable] = None) -> str:
        return super()._get_command(message, validator)


class AddNoteHandler(AbstractHandler, PrettyPrintMixin):
    def __init__(self, language: dict[str, str], fields: dict[str, FieldAttrs]):
        super().__init__(language)
        self.database_fields = fields

    def operate(self) -> None:
        """
        Prompts the user for the value of all fields contained in the database_field collection.
        Adds a new entry to the data file based on the received values.
        For a new entry, the id is obtained by finding the number of entries in the file.
        """
        print(self.language.get('chosen_add_note'))
        entity = {}

        for field, field_attrs in self.database_fields.items():
            message = self.language.get(field_attrs.input_message)

            # Since a field may not have a validator class, you must ensure that
            # it exists before initializing a validator
            validator = field_attrs.validator_class
            validator = validator(
                self.language.get(field_attrs.validator_arg_code),
                err_code='input_error'
            ) if validator else None

            field_value = self._get_command(message, validator)
            entity[field] = field_value

        df = pd.read_csv('database.csv', index_col='pk')
        df.loc[len(df.index)] = entity.values()

        # Displays the added entry
        print(self.language.get('note_add_success'))
        df.tail(1).apply(
            self.pprint, fields=self.database_fields, language=self.language, axis=1
        )

        df.to_csv('database.csv')

    @translate_dict
    def _get_command(self, message: str, validator: Optional[callable] = None) -> str:
        return super()._get_command(message, validator)


class FindNotesHandler(AbstractHandler, PrettyPrintMixin):
    def __init__(self, language: dict[str, str | dict], fields: dict[str, FieldAttrs]):
        super().__init__(language)
        self.database_fields = fields

    def operate(self) -> tuple[pd.DataFrame, str]:
        """
        Creates a database query based on user selection.
        After generating each request, the user will be shown all the filtered records from the database.
        Next, the user is asked to create an additional query for the already filtered records.

        The function returns a database object and a generated query, which is necessary for ChangeNotesHandler to work.
        """
        print(self.language.get('chosen_find_notes'))

        queries = []
        df = pd.read_csv('database.csv', index_col='pk')

        # Receives yes/no translation for selected language
        options = self.language.get('agree_disagree')

        further = True
        while further:
            queries.append(self._get_query())
            filtered_df = df.loc[df.query(f'({") & (".join(queries)})').index]
            if not len(filtered_df):
                print(self.language.get('bad_query'))
                raise ExitSignal

            print(self.language.get('n_notes_found').format(number=len(filtered_df)))
            filtered_df.apply(
                self.pprint, fields=self.database_fields, language=self.language, axis=1
            )

            # Requests to the user about his desire to add more queries
            message = self.language.get('add_query').format(options='/'.join(options.keys()))
            validator = ValueInValidator(options.keys())
            further = options[self._get_command(message, validator)]

        return df, f'({") & (".join(queries)})'

    @translate_dict
    def _get_command(self, message: str, validator: Optional[callable] = None) -> str:
        return super()._get_command(message, validator)

    def _get_query(self) -> str:
        """
        Prompts the user for 3 parameters:
        1) Field by which filtering will occur
        2) A logical operation performed on the field values
        3) The value with which the field values will be compared

        After this, the function returns the completed query string
        """
        # Gets a field to filter
        main_validator = ValueInValidator(
            options={k: self.language.get(k) for k in self.database_fields},
            err_code='first_arg_err'
        )
        main_arg = self._get_command(
            message=self.language.get('chose_first_arg').format(
                options=', '.join(self.language.get(k) for k in self.database_fields)),
            validator=main_validator
        )

        # Specifies the arguments for the selected field
        field_attrs = self.database_fields[main_arg]

        # Gets an operation type
        oper_validator = ValueInValidator(
            options=field_attrs.operations,
            err_code='operator_err'
        )
        operation = self._get_command(
            message=self.language.get('chose_operator').format(
                options=', '.join(field_attrs.operations)),
            validator=oper_validator
        )

        # Gets a filter value
        sub_validator = field_attrs.validator_class(
            self.language.get(field_attrs.validator_arg_code),
            err_code='input_error'
        ) if field_attrs.validator_class else None

        sub_arg = self._get_command(
            message=self.language.get('chose_sub_arg'),
            validator=sub_validator
        )

        return self.database_fields[main_arg].query_form.format(
            main_arg=main_arg,
            operation=operation,
            sub_arg=sub_arg
        )


class ChangeNotesHandler(FindNotesHandler):
    def operate(self) -> None:
        """
        Gets the fields to change and then the new values for the selected fields.
        After this it overwrites the database.
        """
        # Gets the results of FindNotesHandler.
        df, query = super().operate()

        fields_to_change = self._get_fields_to_change()
        new_fields = self._get_new_field_values(fields_to_change)

        df.loc[df.query(query).index, new_fields.keys()] = tuple(new_fields.values())

        df.to_csv('database.csv')

    def _get_fields_to_change(self) -> list[str]:
        """
        Prompts the user for a field to change.
        After this, it prompts you to enter a few more fields.
        """
        fields_to_change = set()

        # Receives yes/no translation for selected language
        options = self.language.get('agree_disagree')
        further = True

        while further:
            validator = ValueInValidator(
                options={k: self.language.get(k) for k in self.database_fields},
                err_code='first_arg_err'
            )
            message = self.language.get('choose_field_to_change').format(
                fields=', '.join([self.language.get(k) for k in self.database_fields])
            )
            field = self._get_command(message, validator)
            fields_to_change.add(field)

            # Requests to the user about his desire to continue adding fields to change list
            message = self.language.get('add_field').format(options='/'.join(options.keys()))
            validator = ValueInValidator(options.keys())
            further = options[self._get_command(message, validator)]

        return list(fields_to_change)

    def _get_new_field_values(self, fields_to_change: list[str]) -> dict[str, str | int]:
        """
        For each field in the fields_to_change collection, gets a new value.

        Returns a dictionary as: {field: new_field_value}
        """
        result = {}
        for field in fields_to_change:
            field_attrs = self.database_fields.get(field)

            # Since a field may not have a validator class, you must ensure that
            # it exists before initializing a validator
            validator = field_attrs.validator_class
            validator = validator(
                self.language.get(field_attrs.validator_arg_code),
                err_code='input_error'
            ) if validator else None

            message = self.language.get(field_attrs.input_message)
            field_value = self._get_command(message, validator)

            # Crutch for pandas. If you do not convert numeric values to Integer,
            # Pandas will display a warning when saving
            if field_value.isdigit():
                field_value = int(field_value)
            result[field] = field_value

        return result


# All new commands are registered here.
# The dictionary key is the command alias by which the value - handler can be called
commands = {
    'show': ShowStatisticHandler,
    'add': AddNoteHandler,
    'find': FindNotesHandler,
    'change': ChangeNotesHandler,
}
