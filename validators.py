def _get_query_obj(options: tuple[str],
                   message_key: str,
                   err_message_key: str,
                   lang_dict: dict[str, str]
                   ) -> str:
    """
    The function compares what the user enters with a list of valid values.

    If there is a discrepancy, it will require you to recheck the entered value.
    If the "options" parameter is None, no check occurs
    """

    message = (lang_dict.get(message_key, '__ERROR__'))

    if options is not None:
        message = message.format(options=', '.join(options))

    arg = input(message).strip()

    while options is not None and arg not in options:
        arg = input(lang_dict.get(err_message_key, '__ERROR__')).strip()

    return arg


def validate_query_input(allowed_operations: dict[str: tuple[str]],
                         lang_dict: dict[str, str]
                         ) -> tuple[str, list[str]]:
    """

    Calls '_get_query_obj' for 3 objects: filtered field, filter operation and filter operation argument
    Returns query string

    """
    main_arg = _get_query_obj(options=list(allowed_operations.keys()),
                              message_key='chose_first_arg',
                              err_message_key='first_arg_err',
                              lang_dict=lang_dict)

    operators = [i for tup in allowed_operations.values() for i in tup]
    operators = set(operators)

    operation = _get_query_obj(options=list(operators),
                               message_key='chose_operator',
                               err_message_key='operator_err',
                               lang_dict=lang_dict)

    sub_arg = _get_query_obj(options=None,
                             message_key='chose_sub_arg',
                             err_message_key='sub_arg_err',
                             lang_dict=lang_dict)

    return f'{main_arg}{operation}"{sub_arg}"'


def validate_change_input(fields: dict[str, str],
                          lang_dict: dict[str, str]
                          ) -> dict[str, str]:
    """

    Receives a raw string from the user, which should list all
    the fields to be changed separated by spaces.
    If at least one field is specified incorrectly, it requires
    you to enter a new value. Next, for each selected field, it
    prompts you to specify a new value.

    """
    raw_input = input(lang_dict.get('change_fields', '__ERROR__').format(fields=', '.join(fields.keys())))
    managed_data = raw_input.split()

    while any(field not in fields for field in managed_data):
        managed_data = input(lang_dict.get('unexpected_field', '__ERROR__')).split()

    result = {}
    for field in managed_data:
        field_value = input(lang_dict.get('change_field', '__ERROR__').format(field_name=fields[field]))
        result[field] = field_value

    return result
