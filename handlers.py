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


class AbstractHandler(ABC):
    """Implements the abstract method "operate" and a protected method "_validate_entered"."""
    def __init__(self, language: dict[str, str | dict]):
        self.language = language

    @abstractmethod
    def operate(self):
        pass

    def _validate_entered(self, message: str, validator: Optional[AbstractValidator] = None) -> str:
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
    """A handler class that sets the interface language."""
    def operate(self) -> dict[str, object]:
        # Gets a list of all registered language packs
        lang_codes = get_lang_codes()

        # Offers the user a choice of which interface language to use
        message = self.language.get('select_language').format(options=', '.join(lang_codes))
        validator = ValueInValidator(options=lang_codes)
        chosen_code = self._validate_entered(message, validator)

        # Returns the language pack
        return registered_languages.get(chosen_code)


class WelcomeHandler(AbstractHandler):
    """Welcomes the user and offers training"""
    def operate(self):
        options = self.language.get('agree_disagree')
        message = self.language.get('start').format(options='/'.join(options.keys()))

        validator = ValueInValidator(options=list(options.keys()))
        show_tutorial = self._validate_entered(message, validator)

        return options[show_tutorial]


class ShowTutorialHandler(AbstractHandler):
    def __init__(self, language: dict[str, str | dict], tutorial_steps: tuple[str]):
        super().__init__(language)
        self.tutorial_steps = tutorial_steps

    def operate(self):
        """

        Goes through all training points, the user is given the opportunity
        to exit the training mode at any time.

        """

        for step in self.tutorial_steps:
            if step not in self.language:
                continue
            options = self.language.get('agree_disagree')
            message = self.language.get(step).format(options='/'.join(options.keys()))

            validator = ValueInValidator(options=list(options.keys()))
            further = self._validate_entered(message, validator)

            if not options[further]:
                break


class ChooseCommandHandler(AbstractHandler):
    def __init__(self, language: dict[str, str], commands: dict[str, AbstractHandler]):
        super().__init__(language)
        self.commands = commands

    def operate(self):
        message = self.language.get('require_input').format(
            commands=', '.join(self.commands.keys())
        )
        validator = ValueInValidator(options=self.commands.keys())
        command = self._validate_entered(message, validator)

        return self.commands.get(command)


class ShowStatisticHandler(AbstractHandler, PrettyPrintMixin):
    def __init__(self, language: dict[str, str | dict], database_fields: dict[str, FieldAttrs]):
        super().__init__(language)
        self.database_fields = database_fields

    def operate(self):
        """

        The function will request and display the page as requested by
        the user until the 'exit' command is received.
        The number of records displayed on an individual page is configured in
        the paginate_by variable.

        """
        print(self.language.get('chosen_show_list'))
        df = pd.read_csv('database.csv', index_col='pk')

        if len(df) == 0:
            print(self.language.get('empty_table'))
            return

        expense, income = df.groupby('type').amount.sum()

        print(self.language.get('statistic').format(
            summary=income - expense, income=income, expense=expense
        ))

        validator = ValueInValidator(options=self.language.get('values_for_type'))
        message = self.language.get('filter_by_type').format(
            options=', '.join(self.language.get('values_for_type').values())
        )
        display_by_type = self._validate_entered(message, validator)

        while True:
            message_keys = {'income': 'income_message', 'expense': 'expense_message'}
            print(self.language.get(message_keys[display_by_type]))

            df.loc[df.type == display_by_type].apply(
                self.pprint, fields=self.database_fields, language=self.language, axis=1
            )

            display_by_type = self._validate_entered(message, validator)

    @translate_dict
    def _validate_entered(self, message: str, validator: Optional[callable] = None) -> str:
        return super()._validate_entered(message, validator)


class AddNoteHandler(AbstractHandler, PrettyPrintMixin):
    def __init__(self, language: dict[str, str], database_fields: dict[str, FieldAttrs]):
        super().__init__(language)
        self.database_fields = database_fields

    def operate(self):
        """

        Prompts the user for the value of all fields contained in
        the database_field collection.
        Adds a new entry to the data file based on the received values.
        For a new entry, the id is obtained by finding the number
        of entries in the file.

        """
        print(self.language.get('chosen_add_note'))
        entity = {}

        for field, field_attrs in self.database_fields.items():
            message = self.language.get(
                field_attrs.input_message
            )

            validator = field_attrs.validator_class
            if validator:
                validator = validator(
                    self.language.get(field_attrs.validator_arg_code),
                    err_code='input_error'
                )

            field_value = self._validate_entered(message, validator)
            entity[field] = field_value

        df = pd.read_csv('database.csv', index_col='pk')
        df.loc[len(df.index)] = entity.values()

        print(self.language.get('note_add_success'))

        df.tail(1).apply(
            self.pprint, fields=self.database_fields, language=self.language, axis=1
        )
        df.to_csv('database.csv')

    @translate_dict
    def _validate_entered(self, message: str, validator: Optional[callable] = None) -> str:
        return super()._validate_entered(message, validator)


class FindNotesHandler(AbstractHandler, PrettyPrintMixin):
    def __init__(self, language: dict[str, str], database_fields: dict[str, FieldAttrs]):
        super().__init__(language)
        self.database_fields = database_fields

    def operate(self):
        print(self.language.get('chosen_find_notes'))

        queries = []
        df = pd.read_csv('database.csv', index_col='pk')

        further = 'y'
        while further == 'y':
            queries.append(self._validate_entered_query())
            filtered_df = df.loc[df.query(f'({") & (".join(queries)})').index]
            if not len(filtered_df):
                print(self.language.get('bad_query'))
                raise ExitSignal

            print(self.language.get('n_notes_found').format(number=len(filtered_df)))
            filtered_df.apply(
                self.pprint, fields=self.database_fields, language=self.language, axis=1
            )

            message = self.language.get('add_query')
            validator = ValueInValidator(options=('y', 'n'))
            further = self._validate_entered(message, validator)

        return df, f'({") & (".join(queries)})'

    @translate_dict
    def _validate_entered(self, message: str, validator: Optional[callable] = None) -> str:
        return super()._validate_entered(message, validator)

    def _validate_entered_query(self):
        """

        Calls '_get_query_obj' for 3 objects: filtered field,
        filter operation and filter operation argument.

        Returns query string.

        """

        main_validator = ValueInValidator(
            options={k: self.language.get(k) for k in self.database_fields},
            err_code='first_arg_err'
        )
        main_arg = self._validate_entered(
            message=self.language.get('chose_first_arg').format(
                options=', '.join(self.language.get(k) for k in self.database_fields)),
            validator=main_validator
        )

        field_attrs = self.database_fields[main_arg]

        oper_validator = ValueInValidator(
            options=field_attrs.operations,
            err_code='operator_err'
        )
        operation = self._validate_entered(
            message=self.language.get('chose_operator').format(
                options=', '.join(field_attrs.operations)),
            validator=oper_validator
        )

        sub_validator = field_attrs.validator_class(
            self.language.get(field_attrs.validator_arg_code),
            err_code='input_error'
        ) if field_attrs.validator_class else None

        sub_arg = self._validate_entered(
            message=self.language.get('chose_sub_arg'),
            validator=sub_validator
        )

        return self.database_fields[main_arg].query_form.format(
            main_arg=main_arg,
            operation=operation,
            sub_arg=sub_arg
        )


class ChangeNotesHandler(FindNotesHandler):
    def operate(self):
        df, query = super().operate()

        new_fields = self.validate_change_input()
        df.loc[df.query(query).index, new_fields.keys()] = tuple(new_fields.values())

        df.to_csv('database.csv')

    def validate_change_input(self):
        """

        Receives a raw string from the user, which should list all
        the fields to be changed separated by spaces.
        If at least one field is specified incorrectly, it requires
        you to enter a new value. Next, for each selected field, it
        prompts you to specify a new value.

        """

        fields_to_change = set()
        further = 'y'
        while further == 'y':
            validator = ValueInValidator(
                options={k: self.language.get(k) for k in self.database_fields},
                err_code='first_arg_err'
            )
            message = self.language.get('choose_field_to_change').format(
                fields=', '.join([self.language.get(k) for k in self.database_fields])
            )
            field = self._validate_entered(message, validator)
            fields_to_change.add(field)

            message = self.language.get('add_field')
            validator = ValueInValidator(options=('y', 'n'))
            further = self._validate_entered(message, validator)

        result = {}
        for field in fields_to_change:
            field_attrs = self.database_fields.get(field)

            validator = field_attrs.validator_class
            if validator:
                validator = validator(
                    self.language.get(field_attrs.validator_arg_code),
                    err_code='input_error'
                )
            message = self.language.get(field_attrs.input_message)
            field_value = self._validate_entered(message, validator)

            if field_value.isdigit():
                field_value = int(field_value)
            result[field] = field_value

        return result


commands = {
    'show': ShowStatisticHandler,
    'add': AddNoteHandler,
    'find': FindNotesHandler,
    'change': ChangeNotesHandler,
}
