import re
from abc import ABC, abstractmethod


class AbstractValidator(ABC):
    def __init__(self, err_code: str = 'notfound_command'):
        self.err_code = err_code

    @abstractmethod
    def validate(self, user_entered):
        pass


class RegExValidator(AbstractValidator):
    def __init__(self, regex: str, err_code: str = 'notfound_command'):
        super().__init__(err_code)
        self.regex = regex

    def validate(self, user_entered) -> bool:
        if user_entered == 'exit':
            return True
        return re.search(self.regex, user_entered) is not None


class ValueInValidator(AbstractValidator):
    def __init__(self, options: iter, err_code: str = 'notfound_command'):
        super().__init__(err_code)
        self.options = options

    def validate(self, user_entered: str) -> bool:
        if user_entered == 'exit':
            return True
        return user_entered in self.options


class TypeValidator(AbstractValidator):
    def __init__(self, datatype: callable, err_code: str = 'notfound_command'):
        super().__init__(err_code)
        self.datatype = datatype

    def validate(self, user_entered) -> bool:
        if user_entered == 'exit':
            return True
        try:
            self.datatype(user_entered)
        except ValueError:
            return False
        return True
