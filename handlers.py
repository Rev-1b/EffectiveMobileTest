from abc import ABC, abstractmethod
from datetime import datetime

import pandas as pd
from tabulate import tabulate

from languages import get_lang_codes, registered_languages

pd.set_option('display.max_columns', None)
PAGINATE_BY = 5


class AbstractHandler(ABC):
    def __init__(self, language: dict[str, str]):
        self.language = language

    @abstractmethod
    def operate(self):
        pass

    def _validate_input(self, message: str, options=None) -> str:
        """

        Requires user to enter the correct command until it gets it.

        """

        input_command = input(message).strip()

        while options and input_command not in options:
            error_message = self.language.get('notfound_command', '__ERROR__')
            print(error_message.format(command=input_command, options=', '.join(options)))

            input_command = input(self.language.get('try_again', '__ERROR__')).strip()

        return input_command


class SetLanguageHandler(AbstractHandler):
    def operate(self):
        lang_codes = get_lang_codes()
        message = self.language.get('select_language', '__ERROR__').format(options=lang_codes)

        chosen_code = self._validate_input(message, lang_codes)

        return registered_languages.get(chosen_code)


class StartHandler(AbstractHandler):
    def operate(self):
        options = {'y': True, 'n': False}
        message = self.language.get('start', '__ERROR__')
        show_tutorial = self._validate_input(message, list(options.keys()))

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
            message = self.language.get(step, '__ERROR__')
            options = {'y': True, 'n': False}
            further = self._validate_input(message, list(options.keys()))

            if not options[further]:
                break


class ChooseCommandHandler(AbstractHandler):
    def __init__(self, language: dict[str, str], commands: dict[str, callable]):
        super().__init__(language)
        self.commands = commands

    def operate(self):
        message = self.language.get('require_input', '__ERROR__').format(commands=', '.join(self.commands.keys()))
        command = self._validate_input(message, self.commands.keys())

        return self.commands.get(command)


class ShowStatisticHandler(AbstractHandler):
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
        print(self.language.get('chosen_show_list', '__ERROR__'))
        df = pd.read_csv('database.csv', index_col='pk')

        if len(df) == 0:
            print(self.language.get('empty_table', '__ERROR__'))
            return

        # print('\n' + tabulate(df, headers=['ID', *self.database_fields.values()]), end='\n\n')

        income, outcome = df.groupby('type').amount.sum()
        print(f"Текущий баланс: {income - outcome}\n\n")

        def pprint(obj):
            print(
                'Дата: {date}\n'
                'Категория: {type}\n'
                'Сумма: {amount}\n'
                'Описание: {descr}\n'.format(**obj)
            )

        df.loc[df.type == 'income'].apply(pprint, axis=1)


class AddNoteHandler(AbstractHandler):
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
        print(self.language.get('chosen_add_note', '__ERROR__'))
        entity = {}

        for field, field_attrs in self.database_fields.items():

            if field == 'date':
                field_value = datetime.now().strftime('%Y-%m-%d')
            else:
                message = self.language.get('input_note_data', '__ERROR__').format(field_name=field_attrs['name'])
                field_value = self._validate_input(message, field_attrs['valid_values'])

            entity[field] = field_value
        df = pd.read_csv('database.csv', index_col='pk')
        df.loc[len(df.index)] = entity.values()

        print(self.language.get('note_add_success', '__ERROR__'))
        print(tabulate(df.tail(1), headers=['ID', *map(lambda val: val['name'], self.database_fields.values())]),
              end='\n\n')

        df.to_csv('database.csv')


class FindNoteHandler(AbstractHandler):
    def operate(self):
        pass




database_fields = {
    'date': {
        'name': 'Date',
        'operations': ('==', '>', '>=', '<', '<='),
        'valid_values': None
    },
    'type': {
        'name': 'Transaction type',
        'operations': ('==',),
        'valid_values': ('income', 'outcome',)
    },
    'amount': {
        'name': 'Amount',
        'operations': ('==',),
        'valid_values': None
    },
    'descr': {
        'name': 'Description',
        'operations': ('==',),
        'valid_values': None
    },
}

# At the moment, filtering fields is only available by the equal sign, however,
# to add new operations it is enough to register them in this dictionary

# All commands specified in this collection become available to the user in the main menu
commands = {
    'help': ShowTutorialHandler,
    'sh': ShowStatisticHandler,
    'add': AddNoteHandler,
    # 'find_notes': find_notes_handler,
    # 'edit_notes': edit_notes_handler,
    # 'exit': exit_handler,
}
