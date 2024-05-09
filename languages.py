ru_lang = {
    'select_language': 'Перед началом работы, выберите язык интерфейса: {options}:\n ... ',
    'notfound_command': 'Команда не распознана! Проверьте ввод и попробуйте еще раз.\n ... ',

    # ---------------------------------------- Initial message -------------------------------------------------
    'start': '\nДобро пожаловать в приложение "Личный финансовый кошелёк"!\n\n'
             'Перед тем, как начать, предлагаем пройти короткое обучение, в котором будет показано, как пользоваться '
             'программой.\n'
             'Хотите пройти обучение? "y/n"\n ... ',

    # ---------------------------------------- Tutorial section ------------------------------------------------
    'short_description': '\nКраткое описание:\n\n'

                         'Приложение представляет собой базу данных, в которой содержится информация о ваших \n'
                         'доходах и расходах.\n'
                         'Вам доступно 4 основных действия: отобразить статистику доходов/расходов, добавить \n'
                         'новую запись в базу, а также отобразить или изменить записи по указанному условию.\n\n'

                         'Каждый раз, когда программе будут необходимы значения для работы, вам будут выведены\n'
                         'все доступные команды. Все команды необходимо набирать ровно также, как и в примере.\n\n'

                         'В любой момент вам доступна команда "exit", которая вернет вас в главное меню.\n\n'

                         'Далее следуют подробные инструкции по использованию каждой функции.\n\n'

                         'Хотите продолжить? "y/n"\n ... ',

    'show': '\nПоказать статистику:\n\n'

            'Чтобы отобразить статистику, вам следует выбрать опцию "show" в главном меню.\n'
            'Далее вам будет отображена краткая сводка о вашем балансе, доходах и расходах.\n'
            'После этого вам будет предложено выбрать, какую категорию транзакций отобразить подробно.\n'
            'В зависимости от выбора, будут отображены все записи из категории "Доход" или "Расход".\n\n'

            'Хотите продолжить? "y/n"\n ... ',

    'add': '\nДобавить запись:\n\n'

           'Чтобы добавить новую запись в базу, вам следует выбрать опцию "add" в главном меню.\n'
           'Далее вам потребуется ввести значение для каждого поля транзакции по очереди.\n'
           'Для каждого поля вам будет указано, данные в каком формате от вас ожидает программа.\n'
           'После ввода всех требуемых значений, вам будет показана только что созданная запись.\n\n'

           'Хотите продолжить? "y/n"\n ... ',

    'find': '\nНайти записи:\n\n'

            'Чтобы найти записи по условию, вам следует выбрать опцию "find" в главном меню. \n'
            'Далее вам  нужно будет указать три основных аргумента запроса:\n'
            '1.  Указать поле, по которому будет совершена фильтрация\n'
            '2.  Указать оператор, который будет использован в сравнении значений выбранного поля\n'
            '3.  Указать значение, которое оператор будет сравнивать со значением полей записей\n\n'

            'Когда все данные будут корректно указаны, вам будут отображены все записи, полученные\n'
            'по вашему запросу. После этого вам будет предложено добавить еще одно условие к запросу.\n'
            'Так вы cможете создавать сложные запросы с несколькими условиями.\n\n'

            'Хотите продолжить? "y/n"\n ... ',
    'change': '\nИзменить записи:\n\n'

              'Чтобы изменить существующие записи в базе, вам следует выбрать опцию "change" в главном меню.\n'
              'Для начала, процесс аналогичен команде "find", однако после составления запроса вам также\n'
              'будет необходимо указать поля для изменения. Далее вам будет предложено указать новое значение\n'
              'для всех выбранных полей.\n\n'

              'Введите "y", чтобы перейти в главное меню \n ... ',

    'require_input': '\nВыберите действие: "{commands}"\n ... ',

    # ---------------------------------------- Handler messages ------------------------------------------------
    'chosen_show_list': '\n---------- ОТОБРАЖЕНИЕ СТАТИСТИКИ ДОХОДОВ/РАСХОДОВ ----------\n',
    'empty_table': 'На данный момент, в базе данных нет записей\n',
    'bad_command': 'Команда не распознана, проверьте введенное значение! \n ... ',

    'statistic': 'Текущий баланс: {summary}\n'
                 'Доход: {income}\n'
                 'Расход: {expense}\n\n'
                 '---------- СПИСОК ВСЕХ ТРАНЗАКЦИЙ ПО КАТЕГОРИЯМ ------------\n',
    'filter_by_type': 'Выберите категорию транзакций для отображения: {options} либо "exit" для выхода\n ... ',

    'income_message': '---------- ДОХОДЫ ------------\n',
    'expense_message': '---------- РАСХОДЫ ------------\n',

    'chosen_add_note': '\n---------- ДОБАВЛЕНИЕ НОВОЙ ТРАНЗАКЦИИ ----------',
    'input_error': 'Некорректное значение! Проверьте введенную информацию и попробуйте снова:\n ... ',
    'note_add_success': '\nВы успешно добавили новую транзакцию в базу: \n',

    'chosen_find_notes': '\n---------- НАХОЖДЕНИЕ ТРАНЗАКЦИЙ ----------:',
    'chose_first_arg': 'Выберите параметр для фильтрации: "{options}"\n ... ',
    'first_arg_err': 'Вы выбрали несуществующее поле, проверьте введенное значение!\n ... ',
    'chose_operator': 'Выберите действие над значением поля: "{options}"\n ... ',
    'operator_err': 'Вы выбрали недопустимый оператор, проверьте введенное значение!\n ... ',
    'chose_sub_arg': 'Выберите значение, по которому выбранное поле будет отфильтровано:\n ... ',
    'add_query': 'Хотите добавить еще одно условие фильтрации? "y/n"\n ... ',
    'bad_query': 'По вашему запросу не найдено ни одной записи!',
    'n_notes_found': 'По вашему запросу найдено {number} записей:\n',

    'chosen_change_notes': '\n---------- ИЗМЕНЕНИЕ ЗАПИСЕЙ -----------',
    'choose_field_to_change': 'Выберите поле, которое хотите изменить: {fields}\n ... ',
    'add_field': 'Хотите добавить в список для изменения еще поля?: "y/n"\n ... ',
    'unexpected_field': 'Одно или несколько из указанных полей не существует. Проверьте введенные значения! \n ... ',
    'change_field': 'Введите новое значение для поля "{field_name}"\n ... ',

    # -------------------------------------- Database Fields info ----------------------------------------------
    'date': 'Дата',
    'date_regex': '(?:19|20)[0-9]{2}[-\\/ ]?(0?[1-9]|1[0-2])[-/ ]?(0?[1-9]|[12][0-9]|3[01])',
    'date_input': 'Введите дату транзакции (формат ГГГГ-ММ-ДД):\n ... ',

    'type': 'Категория',
    'values_for_type': {'income': 'Доход', 'expense': 'Расход'},
    'type_input': 'Введите категорию транзакции (Доход или Расход):\n ... ',

    'amount': 'Сумма',
    'amount_type': int,
    'amount_input': 'Введите сумму транзакции (числовое значение):\n ... ',

    'descr': 'Описание',
    'descr_input': 'Введите описание к транзакции:\n ... ',
}

eng_lang = {
    'select_language': 'Before you start, select the interface language: {options}:\n ... ',
    'notfound_command': 'The command is not recognized! Check your input and try again.\n ... ',

    # ---------------------------------------- Initial message -------------------------------------------------
    'start': '\nWelcome to the Personal Financial Wallet application!\n\n'
             'Before you start, we suggest you complete a short training session that will show you how to use '
             'a program.\n\nDo you want to get trained? "y/n" ... ',

    # ---------------------------------------- Tutorial section ------------------------------------------------
    'short_description': '\nShort description:\n\n'

                         'The application is a database that contains information about your income and expenses.\n'
                         'You have 4 main actions available to you: display income/expense statistics, add \n'
                         'a new record in the database, as well as display or change records according to the\n'
                         'specified condition.\n\n'

                         'Every time the program needs values to work, you will be shown all available commands.\n'
                         'All commands must be typed exactly as in the example.\n\n'

                         'At any time you have access to the "exit" command, which will return you to the main menu.\n'

                         'Detailed instructions for using each function follow.\n\n'

                         'Do you want to continue? "y/n"\n ... ',

    'show': '\nShow statistics:\n\n'

            'To display statistics, you should select the "show" option from the main menu.\n'
            'Next, you will be shown a brief summary of your balance, income and expenses.\n'
            'You will then be asked to select which category of transactions to display in detail.\n'
            'Depending on your selection, all entries from the "Income" or "Expense" categories will be displayed.\n\n'

            'Do you want to continue? "y/n"\n ... ',

    'add': '\nAdd a note:\n\n'

           'To add a new entry to the database, you should select the "add" option in the main menu.\n'
           'Next you will need to enter a value for each transaction field in turn.\n'
           'For each field you will be told in what format the program expects the data from you.\n'
           'Once you have entered all the required values, you will be shown the newly created entry.\n\n'

           'Do you want to continue? "y/n"\n ... ',

    'find': '\nFind transactions:\n\n'

            'To find records by condition, you should select the "find" option in the main menu. \n'
            'Next you will be given three main request arguments:\n'
            '1. Specify the field by which filtering will be performed\n'
            '2. Specify the operator that will be used to compare the values of the selected field\n'
            '3. Specify the value that the operator will compare with the value of the record fields\n\n'

            'When all data is entered correctly, all records received will be displayed to you\n'
            'at your request. You will then be prompted to add another condition to the request.\n'
            'This way you can create complex queries with multiple conditions.\n\n'

            'Do you want to continue? "y/n"\n ... ',
    'change': '\nEdit transactions:\n\n'

              'To change existing records in the database, you should select the "change" option in the main menu.\n'
              'To begin with, the process is similar to the "find" command, but after composing the request you also\n'
              'it will be necessary to specify the fields to change. Next you will be asked to specify a new value\n'
              'for all selected fields.\n\n'

              'Enter "y" to go to main menu \n ... ',

    'require_input': '\nChoose an action: "{commands}"\n ... ',

    # ---------------------------------------- Handler messages ------------------------------------------------
    'chosen_show_list': '\n---------- DISPLAYING INCOME/EXPENSES STATISTICS ----------\n',
    'empty_table': 'There are currently no entries in the database\n',
    'bad_command': 'The command is not recognized, check the entered value! \n ... ',

    'statistic': 'Current balance: {summary}\n'
                 'Income: {income}\n'
                 'Expense: {expense}\n\n'
                 '---------- LIST OF ALL TRANSACTIONS BY CATEGORIES ------------\n',
    'filter_by_type': 'Select the transaction category to display: {options} or "exit" to exit\n ... ',

    'income_message': '---------- INCOMES ------------\n',
    'expense_message': '---------- EXPENSES ------------\n',

    'chosen_add_note': '\n---------- ADDING A NEW TRANSACTION ----------',
    'input_error': 'Incorrect value! Check the information you entered and try again:\n ... ',
    'note_add_success': '\nYou have successfully added a new transaction to the database: \n',

    'chosen_find_notes': '\n---------- FINDING TRANSACTIONS ----------:',
    'chose_first_arg': 'Select an option to filter: "{options}"\n ... ',
    'first_arg_err': 'You have selected a non-existent field, check the entered value!\n ... ',
    'chose_operator': 'Select action on field value: "{options}"\n ... ',
    'operator_err': 'You selected an invalid operator, check the entered value!\n ... ',
    'chose_sub_arg': 'Select the value by which the selected field will be filtered:\n ... ',
    'add_query': 'Do you want to add another filter condition?? "y/n"\n ... ',
    'bad_query': 'No records were found for your request!',
    'n_notes_found': '{number} records found for your request:\n',

    'chosen_change_notes': '\n---------- CHANGING ENTRIES -----------',
    'choose_field_to_change': 'Select the field you want to change: {fields}\n ... ',
    'add_field': 'Do you want to add more fields to the list to change?: "y/n"\n ... ',
    'unexpected_field': 'One or more of the specified fields does not exist. Check the entered values! \n ... ',
    'change_field': 'Enter a new value for the field "{field_name}"\n ... ',

    # -------------------------------------- Database Fields info ----------------------------------------------
    'date': 'Date',
    'date_regex': '(?:19|20)[0-9]{2}[-\\/ ]?(0?[1-9]|1[0-2])[-/ ]?(0?[1-9]|[12][0-9]|3[01])',
    'date_input': 'Enter the transaction date (format YYYY-MM-DD):\n ... ',

    'type': 'Type',
    'values_for_type': {'income': 'Income', 'expense': 'Expense'},
    'type_input': 'Enter the transaction category (Income or Expense):\n ... ',

    'amount': 'Amount',
    'amount_type': int,
    'amount_input': 'Enter the transaction amount (numeric value):\n ... ',

    'descr': 'Description',
    'descr_input': 'Enter a description for the transaction:\n ... ',
}

# When adding a new language pack, you must register the new language here
registered_languages = {
    'ru': ru_lang,
    'en': eng_lang,
}


def get_lang_codes() -> list[str]:
    return [code for code in registered_languages]
