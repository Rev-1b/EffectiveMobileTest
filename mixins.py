from handlers import AbstractHandler


class GetQueryMixin(AbstractHandler):
    def __init__(self, language: dict[str, str], database_fields: dict[str, dict]):
        super().__init__(language)
        self.database_fields = database_fields

    def operate(self):
        pass

    def get_full_query(self):
        """

        Until the user decides to finish, new queries are requested.
        Then the function combines all received requests into one and returns it.

        """
        queries = []
        further = True

        while further:
            query = self._validate_entered_query()
            queries.append(query)

            message = self.language.get('add_query', '__ERROR__')
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
            message=self.language.get('chose_first_arg', '__ERROR__'),
            options=list(self.database_fields.keys()),
            err_message_key='first_arg_err'
        )

        operation = self._validate_entered(
            message=self.language.get('chose_operator', '__ERROR__'),
            options=self.database_fields[main_arg]['operations'],
            err_message_key='operator_err'
        )

        sub_arg = self._validate_entered(
            message=self.language.get('chose_sub_arg', '__ERROR__'),
            options=None,
            err_message_key='sub_arg_err'
        )

        return f'{main_arg}{operation}"{sub_arg}"'
