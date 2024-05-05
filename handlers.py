from languages import get_lang_codes, registered_languages
from validators import *

import pandas as pd
from tabulate import tabulate

from abc import ABC, abstractmethod

pd.set_option('display.max_columns', None)
paginate_by = 5


class AbstractHandler(ABC):
    def __init__(self, language: dict[str, str]):
        self.language = language

    @abstractmethod
    def operate(self):
        pass

    @abstractmethod
    def _validate_input(self, *args, **kwargs) -> str:
        """

        Requires user to enter the correct command until it gets it.

        """
        initial_message, options = args[:2]
        input_command = input(initial_message).strip()

        while input_command not in options:
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

    def _validate_input(self, *args, **kwargs) -> str:
        return super()._validate_input(*args, **kwargs)


class StartHandler(AbstractHandler):
    def operate(self):
        options = {'y': True, 'n': False}
        message = self.language.get('start', '__ERROR__')
        show_tutorial = self._validate_input(message, list(options.keys()))

        return options[show_tutorial]

    def _validate_input(self, *args, **kwargs) -> str:
        return super()._validate_input(*args, **kwargs)


class ShowTutorialHandler(AbstractHandler):
    def __init__(self, language: dict[str, str], tutorial_steps: list[str]):
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

    def _validate_input(self, *args, **kwargs) -> str:
        return super()._validate_input(*args, *kwargs)


class ChooseCommandHandler(AbstractHandler):
    def __init__(self, language: dict[str, str], commands: dict[str]):
        super().__init__(language)
        self.commands = commands

    def operate(self):
        message = self.language.get('require_input', '__ERROR__').format(commands=', '.join(self.commands.keys()))
        command = self._validate_input(message, self.commands.keys())

        return self.commands.get(command)

    def _validate_input(self, *args, **kwargs) -> str:
        return super(*args, **kwargs)