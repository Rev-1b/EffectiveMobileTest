from abc import ABC, abstractmethod
from datetime import datetime

import pandas as pd

from languages import get_lang_codes, registered_languages
from mixins import PrettyPrintMixin

pd.set_option('display.max_columns', None)


class AbstractHandler(ABC):
    def __init__(self, language: dict[str, str]):
        self.language = language

    @abstractmethod
    def operate(self):
        pass

    def _validate_entered(self, message: str,
                          options: [iter, None] = None,
                          err_message_key: str = 'notfound_command') -> str:
        """

        Requires user to enter the correct command until it gets it.

        """

        user_entered = input(message).strip()

        while options and user_entered not in options:
            error_message = self.language.get(err_message_key)
            print(error_message.format(command=user_entered, options=', '.join(options)))

            user_entered = input(self.language.get('try_again')).strip()

        return user_entered


class SetLanguageHandler(AbstractHandler):
    def operate(self):
        lang_codes = get_lang_codes()
        message = self.language.get('select_language').format(options=lang_codes)

        chosen_code = self._validate_entered(message, lang_codes)

        return registered_languages.get(chosen_code)


class StartHandler(AbstractHandler):
    def operate(self):
        options = {'y': True, 'n': False}
        message = self.language.get('start')
        show_tutorial = self._validate_entered(message, list(options.keys()))

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
            further = self._validate_entered(message, list(options.keys()))

            if not options[further]:
                break


class ChooseCommandHandler(AbstractHandler):
    def __init__(self, language: dict[str, str], commands: dict[str, callable]):
        super().__init__(language)
        self.commands = commands

    def operate(self):
        message = self.language.get('require_input').format(commands=', '.join(self.commands.keys()))
        command = self._validate_entered(message, self.commands.keys())

        return self.commands.get(command)


class ShowStatisticHandler(AbstractHandler, PrettyPrintMixin):
    def __init__(self, language: dict[str, str], database_fields: dict[str, dict]):
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
        print(f'Текущий баланс: {income - outcome}')
        print(f'Доход: {income}')
        print(f'Расход: {outcome}\n')

        print('---------- СПИСОК ВСЕХ ТРАНЗАКЦИЙ ПО КАТЕГОРИЯМ ------------\n')

        def _print_by_type( transaction_type: str, message_key: str):
            print(self.language.get(message_key))
            df.loc[df.type == transaction_type].apply(self.pprint, fields=self.database_fields, language=self.language,
                                                      axis=1)

        for transaction, message in {'income': 'income_message', 'outcome': 'outcome_message'}.items():
            _print_by_type(transaction, message)


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

            if field == 'date':
                field_value = datetime.now().strftime('%Y-%m-%d')
            else:
                message = self.language.get('input_note_data').format(
                    field_name=field_attrs[self.language.get('name_key')])
                field_value = self._validate_entered(message, field_attrs['valid_values'])

            entity[field] = field_value

        df = pd.read_csv('database.csv', index_col='pk')
        df.loc[len(df.index)] = entity.values()

        print(self.language.get('note_add_success'))
        df.tail(1).apply(self.pprint, axis=1)

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
            further = self._validate_entered(message, options=['y', 'n'])

        union_query = f'({") & (".join(queries)})'
        return union_query

    def _validate_entered_query(self):
        """

        Calls '_get_query_obj' for 3 objects: filtered field,
        filter operation and filter operation argument.

        Returns query string.

        """

        main_arg = self._validate_entered(
            message=self.language.get('chose_first_arg').format(
                options=', '.join(self.database_fields.keys())),
            options=list(self.database_fields.keys()),
            err_message_key='first_arg_err'
        )

        operation = self._validate_entered(
            message=self.language.get('chose_operator').format(
                options=', '.join(self.database_fields[main_arg]['operations'])
            ),
            options=self.database_fields[main_arg]['operations'],
            err_message_key='operator_err'
        )

        sub_arg = self._validate_entered(
            message=self.language.get('chose_sub_arg'),
            options=None,
            err_message_key='sub_arg_err'
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
            filtered_df.apply(self.pprint, axis=1)
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
                field_name=self.database_fields[field][self.language.get('name_key')])
            )
            result[field] = field_value

        return result


database_fields = {
    'date': {
        'name_key': 'date_name',
        'operations': ('==', '>', '>=', '<', '<='),
        'valid_values_key': None,
        'query_form': '{main_arg}{operation}"{sub_arg}"',
    },
    'type': {
        'name_key': 'type_name',
        'operations': ('==',),
        'valid_values_key': 'values_for_type',
        'query_form': '{main_arg}{operation}"{sub_arg}"',
    },
    'amount': {
        'name_key': 'amount_name',
        'operations': ('==', '>', '>=', '<', '<='),
        'valid_values_key': None,
        'query_form': '{main_arg}{operation}{sub_arg}',
    },
    'descr': {
        'name_key': 'descr_name',
        'operations': ('==',),
        'valid_values_key': None,
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
