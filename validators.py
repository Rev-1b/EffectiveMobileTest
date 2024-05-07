import re
from abc import ABC, abstractmethod


class AbstractValidator(ABC):
    def __init__(self, err_code: str = 'notfound_command'):
        self.err_code = err_code

    @abstractmethod
    def validate(self, user_entered):
        return True


class RegExValidator(AbstractValidator):
    def __init__(self, regex: str, err_code: str = 'notfound_command'):
        super().__init__(err_code)
        self.regex = regex

    def validate(self, user_entered):
        return re.search(self.regex, user_entered) is not None


class ValueInValidator(AbstractValidator):
    def __init__(self, options: iter, err_code: str = 'notfound_command'):
        super().__init__(err_code)
        self.options = options

    def validate(self, user_entered: str) -> bool:
        return user_entered.lower() in self.options

