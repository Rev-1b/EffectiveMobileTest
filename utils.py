from typing import Optional


class PrettyPrintMixin:
    @staticmethod
    def pprint(obj, **kwargs):
        """
        The function is passed as an argument to the apply function.
        Beautifully displays records from the database, delimiting them with lines
        """
        fields, language = kwargs.values()

        for field, field_attrs in fields.items():
            field_value = obj[field]

            # If field value from the database have its alias, displays that
            if isinstance(language.get(field_attrs.validator_arg_code), dict):
                field_value = language.get(field_attrs.validator_arg_code)[field_value].capitalize()

            print(f"{language.get(field)}: {field_value}")
        print('\n------------------------------\n')


def translate_dict(func: callable) -> callable:
    """
    The function is intended to be used as a decorator.
    For some fields, the values stored in the database have aliases that are more user-friendly.
    This function detects the entry of such fields and performs a double translation.
    First, the value from the database is replaced with its alias.
    After the user selects an alias, the reverse translation occurs and the database structure does not change.
    """
    def wrapper(self, message: str, validator: Optional[callable]) -> str:
        if validator and hasattr(validator, 'options') and isinstance(validator.options, dict):
            new_validator = validator.__class__(validator.options.values(), validator.err_code)
            result = func(self, message, new_validator)
            reversed_options = {v: k for k, v in validator.options.items()}
            return reversed_options[result]

        return func(self, message, validator)

    return wrapper
