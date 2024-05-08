from typing import Optional


class PrettyPrintMixin:
    @staticmethod
    def pprint(obj, **kwargs):
        fields, language = kwargs.values()

        for field, field_attrs in fields.items():
            field_value = obj[field]

            if isinstance(language.get(field_attrs['validator_arg_code']), dict):
                field_value = language.get(
                    field_attrs['validator_arg_code']
                )[field_value].capitalize()

            print(f"{language.get(field)}: {field_value}")

        print('\n------------------------------\n')


def translate_dict(func):
    def wrapper(self, message: str, validator: Optional[callable]) -> str:
        if validator and hasattr(validator, 'options') and isinstance(validator.options, dict):
            new_validator = validator.__class__(validator.options.values(), validator.err_code)
            result = func(self, message, new_validator)
            reversed_options = {v: k for k, v in validator.options.items()}
            return reversed_options[result]

        return func(self, message, validator)

    return wrapper