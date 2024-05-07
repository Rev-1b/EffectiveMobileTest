class PrettyPrintMixin:
    @staticmethod
    def pprint(obj, **kwargs):
        fields, language = kwargs.values()

        for field, field_attrs in fields.items():
            field_value = obj[field]

            if field_attrs['valid_values_key'] is not None:
                field_value = language.get(field_attrs['valid_values_key']).get(field_value)

            print(f"{language.get(field)}: {field_value}")

        print('\n------------------------------\n')
