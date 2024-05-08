from typing import Optional

import pandas as pd

from languages import get_lang_codes, registered_languages
from mixins import PrettyPrintMixin, translate_dict
from validators import *

pd.set_option('display.max_columns', None)


class AbstractHandler(ABC):
    def __init__(self, language: dict[str, str]):
        self.language = language

    @abstractmethod
    def operate(self):
        pass

    def _validate_entered(self, message: str, validator: Optional[callable] = None) -> str:
        """

        Requires user to enter the correct command until it gets it.

        """

        user_entered = input(message).strip()
        if user_entered == 'exit':
            return user_entered

        while validator and not validator.validate(user_entered):
            error_message = self.language.get(validator.err_code)
            print(error_message)

            user_entered = input(self.language.get('try_again')).strip()
            if user_entered == 'exit':
                return user_entered

        return user_entered


class SetLanguageHandler(AbstractHandler):
    def operate(self):
        lang_codes = get_lang_codes()
        message = self.language.get('select_language').format(options=lang_codes)

        validator = ValueInValidator(options=lang_codes)
        chosen_code = self._validate_entered(message, validator)

        return registered_languages.get(chosen_code)


class StartHandler(AbstractHandler):
    def operate(self):
        options = {'y': True, 'n': False}
        message = self.language.get('start')

        validator = ValueInValidator(options=list(options.keys()))
        show_tutorial = self._validate_entered(message, validator)

        return options[show_tutorial]


class ShowTutorialHandler(AbstractHandler):
    def __init__(self, language: dict[str, str], tutorial_steps: tuple[str]):
        super().__init__(language)
        self.tutorial_steps = tutorial_steps

    def operate(self):
        """

        Goes through all training points, the user is given the opportunity
        to exit the training mode at any time.

        """

        for step in self.tutorial_steps:
            message = self.language.get(step)
            options = {'y': True, 'n': False}

            validator = ValueInValidator(options=list(options.keys()))
            further = self._validate_entered(message, validator)

            if not options[further]:
                break


class ChooseCommandHandler(AbstractHandler):
    def __init__(self, language: dict[str, str], commands: dict[str, callable]):
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
    def __init__(self, language: dict[str, str | dict], database_fields: dict[str, dict]):
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

        income, outcome = df.groupby('type').amount.sum()

        print(self.language.get('statistic').format(
            summary=income - outcome, income=income, outcome=outcome
        ))

        validator = ValueInValidator(options=self.language.get('values_for_type'))
        message = self.language.get('filter_by_type').format(
            options=', '.join(map(str.capitalize, self.language.get('values_for_type').values()))
        )
        display_by_type = self._validate_entered(message, validator)

        while display_by_type != 'exit':
            message_keys = {'income': 'income_message', 'outcome': 'outcome_message'}
            print(self.language.get(message_keys[display_by_type]))

            df.loc[df.type == display_by_type].apply(
                self.pprint, fields=self.database_fields, language=self.language, axis=1
            )

            display_by_type = self._validate_entered(message, validator)

    @translate_dict
    def _validate_entered(self, message: str, validator: Optional[callable] = None) -> str:
        return super()._validate_entered(message, validator)


class AddNoteHandler(AbstractHandler, PrettyPrintMixin):
    def __init__(self, language: dict[str, str], database_fields: dict[str, dict]):
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
            message = self.language.get('input_note_data').format(
                field_name=self.language.get(field)
            )

            validator = field_attrs['validator_class']

            if validator:
                validator = validator(
                    self.language.get(field_attrs['validator_arg_code'])
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


class GetQueryMixin(AbstractHandler):
    def __init__(self, language: dict[str, str], database_fields: dict[str, dict]):
        super().__init__(language)
        self.database_fields = database_fields

    def operate(self):
        print(self.get_full_query())

    def get_full_query(self):
        """

        Until the user decides to finish, new queries are requested.
        Then the function combines all received requests into one and returns it.

        """
        queries = []
        further = 'y'

        while further == 'y':
            query = self._validate_entered_query()
            queries.append(query)

            message = self.language.get('add_query')
            validator = ValueInValidator(options=['y', 'n'])
            further = self._validate_entered(message, validator)

        union_query = f'({") & (".join(queries)})'
        return union_query

    def _validate_entered_query(self):
        """

        Calls '_get_query_obj' for 3 objects: filtered field,
        filter operation and filter operation argument.

        Returns query string.

        """

        main_validator = ValueInValidator(
            options=self.database_fields.keys(),
            err_code='first_arg_err'
        )
        main_arg = self._validate_entered(
            message=self.language.get('chose_first_arg').format(
                options=', '.join(self.database_fields.keys())
            ),
            validator=main_validator
        )

        field_attrs = self.database_fields[main_arg]

        oper_validator = ValueInValidator(
            options=field_attrs['operations'],
            err_code='operator_err'
        )
        operation = self._validate_entered(
            message=self.language.get('chose_operator').format(
                options=', '.join(field_attrs['operations'])
            ),
            validator=oper_validator
        )

        sub_validator = field_attrs['validator_class'](
            self.language.get(field_attrs['validator_arg_code']),
            err_code='sub_arg_err'
        ) if field_attrs['validator_class'] else None

        sub_arg = self._validate_entered(
            message=self.language.get('chose_sub_arg'),
            validator=sub_validator
        )

        return self.database_fields[main_arg]['query_form'].format(
            main_arg=main_arg,
            operation=operation,
            sub_arg=sub_arg
        )


class FindNotesHandler(GetQueryMixin, PrettyPrintMixin):
    def operate(self):
        print(self.language.get('chosen_find_notes'))
        query = self.get_full_query()

        df = pd.read_csv('database.csv', index_col='pk')
        filtered_df = df.loc[df.query(query).index]

        if not len(filtered_df):
            print(self.language.get('bad_query'))
        else:
            filtered_df.apply(
                self.pprint, fields=self.database_fields, language=self.language, axis=1
            )
            return df, query


class ChangeNotesHandler(FindNotesHandler):
    def operate(self):
        df_query = super().operate()

        if df_query is None:
            return

        df, query = df_query

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
        raw_input = input(self.language.get('change_fields').format(
            fields=', '.join(self.database_fields.keys()))
        )
        managed_data = raw_input.split()

        while any(field not in self.database_fields.keys() for field in managed_data):
            managed_data = input(self.language.get('unexpected_field')).split()

        result = {}
        for field in managed_data:
            field_value = input(self.language.get('change_field').format(
                field_name=self.language.get(field)
            ))
            if field_value.isdigit():
                field_value = int(field_value)
            result[field] = field_value

        return result


database_fields = {
    'date': {
        'operations': ('==', '>', '>=', '<', '<='),
        'validator_class': RegExValidator,
        'validator_arg_code': 'date_regex',
        'query_form': '{main_arg}{operation}"{sub_arg}"',
    },
    'type': {
        'operations': ('==',),
        'validator_class': ValueInValidator,
        'validator_arg_code': 'values_for_type',
        'query_form': '{main_arg}{operation}"{sub_arg}"',
    },
    'amount': {
        'operations': ('==', '>', '>=', '<', '<='),
        'validator_class': None,
        'validator_arg_code': None,
        'query_form': '{main_arg}{operation}{sub_arg}',
    },
    'descr': {
        'operations': ('==',),
        'validator_class': None,
        'validator_arg_code': None,
        'query_form': '{main_arg}{operation}"{sub_arg}"',
    },
}

# All commands specified in this collection become available to the user in the main menu
commands = {
    'help': ShowTutorialHandler,
    'sh': ShowStatisticHandler,
    'add': AddNoteHandler,
    'gk': FindNotesHandler,
    'ch': ChangeNotesHandler,
    # 'exit': exit_handler,
}
