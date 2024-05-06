class GetQueryMixin:
    def __init__(self, language, allowed_query_operations: dict[str, tuple[str]]):
        self.allowed_query_operations = allowed_query_operations

    def get_full_query(self):
        """

        Until the user decides to finish, new queries are requested.
        Then the function combines all received requests into one and returns it.

        """
        queries = []
        further = 'y'

        while further == 'y':
            query = self._validate_query_input(self.allowed_query_operations)
            queries.append(query)

            message = self.language.get('add_query', '__ERROR__')
            further = self._validate_input(message, options=['y', 'n'])

        union_query = f'({") & (".join(queries)})'
        return union_query