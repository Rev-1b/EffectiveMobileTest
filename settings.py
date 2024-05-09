from typing import NamedTuple, Optional

from handlers import ShowStatisticHandler, FindNotesHandler, ChangeNotesHandler, AddNoteHandler
from validators import AbstractValidator, RegExValidator, ValueInValidator, TypeValidator


class FieldAttrs(NamedTuple):
    operations: tuple[str]
    validator_class: Optional[AbstractValidator]
    validator_arg_code: str
    input_message: str
    query_form: str


database_fields = {
    'date': {
        'operations': ('==', '>', '>=', '<', '<='),
        'validator_class': RegExValidator,
        'validator_arg_code': 'date_regex',
        'input_message': 'date_input',
        'query_form': '{main_arg}{operation}"{sub_arg}"',
    },
    'type': {
        'operations': ('==',),
        'validator_class': ValueInValidator,
        'validator_arg_code': 'values_for_type',
        'input_message': 'type_input',
        'query_form': '{main_arg}{operation}"{sub_arg}"',
    },
    'amount': {
        'operations': ('==', '>', '>=', '<', '<='),
        'validator_class': TypeValidator,
        'validator_arg_code': 'amount_type',
        'input_message': 'amount_input',
        'query_form': '{main_arg}{operation}{sub_arg}',
    },
    'descr': {
        'operations': ('==',),
        'validator_class': None,
        'validator_arg_code': None,
        'input_message': 'descr_input',
        'query_form': '{main_arg}{operation}"{sub_arg}"',
    },
}

# All commands specified in this collection become available to the user in the main menu
commands = {
    'show': ShowStatisticHandler,
    'add': AddNoteHandler,
    'find': FindNotesHandler,
    'change': ChangeNotesHandler,
}
