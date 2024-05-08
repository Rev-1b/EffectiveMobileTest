ru_lang = {
    'notfound_command': 'Проверьте введенное значение! Введенное "{command}" не соответствует списку допустимых '
                        'значений "{options}".\n',
    'try_again': 'Попробуйте еще раз: ... ',

    # ---------------------------------------- Initial message -------------------------------------------------
    'start': '\nДобро пожаловать в приложение "Личный финансовый кошелёк"!\n\n'
             'Перед тем, как начать, предлагаем пройти короткое обучение, в котором будет показано, как пользоваться '
             'программой.\n\nХотите пройти обучение? "y/n" ... ',

    # ---------------------------------------- Tutorial section ------------------------------------------------
    'short_description': '\nКраткое описание:\n'
                         'Приложение представляет собой интерактивную телефонную книгу.\n'
                         'Вам доступно 4 основных действия: отобразить определенную страницу книги, добавить \n'
                         'новую запись в книгу, а также отобразить или изменить записи по указанному условию.\n\n'

                         'Каждый раз, когда программе будут необходимы значения для работы, вам будут выведены все \n'
                         'доступные команды. Все команды необходимо набирать ровно также, как и в примере.\n\n'

                         'Далее следуют подробные инструкции по использованию каждой функции.'
                         '\nХотите продолжить? "y/n" ... ',

    'show_page': '\nПоказать страницу:\n'
                 'Чтобы отобразить необходимую страницу, вам следует выбрать опцию "show_page" в главном меню.\n'
                 'Далее вам будет необходимо ввести номер требуемой страницы. Вам будет предоставлена возможность\n'
                 'выбора новых страниц до того момента, как вы не введете команду "exit", которая вернет вас\n'
                 'в главное меню.\n\n'
                 'Хотите продолжить? "y/n" ... ',

    'add_note': '\nДобавить запись:\n'
                'Чтобы добавить новую запись в книгу, вам следует выбрать опцию "add_note" в главном меню.\n'
                'Далее вам потребуется ввести значение для каждого поля телефонной книги по очереди. Входные данные\n'
                'при вводе номеров телефона дополнительно проверяются на корректность.\n'
                'Каждый номер должен начинаться со знака "+".\n'
                'После ввода всех требуемых значений, вам будет показана только что созданная запись.\n\n'
                'Хотите продолжить? "y/n" ... ',

    'find_notes': '\nНайти записи:\n'
                  'Чтобы найти записи по условию, вам следует выбрать опцию "find_notes" в главном меню. \n'
                  'Далее вам будет указать три основных аргумента запроса:\n'
                  '1.  Указать поле, по которому будет совершена фильтрация\n'
                  '2.  Указать оператор, который будет использован в сравнении значений выбранного поля\n'
                  '3.  Указать значение, которое оператор будет сравнивать со значением полей записей\n'
                  'Когда все данные будут корректно указаны, вам будет предложено написать еще один запрос. Так вы\n'
                  'можете создавать сложные запросы с несколькими условиями.\n\n'

                  'Хотите продолжить? "y/n" ... ',
    'change_notes': '\nИзменить записи:\n'
                    'Чтобы изменить существующие записи в книге, вам следует выбрать опцию\n'
                    '"change_notes" в главном меню.\n'
                    'Для начала, процесс аналогичен команде "find_notes", однако после составления запроса вам также\n'
                    'будет необходимо указать поля для изменения. Далее вам будет предложено указать новое значение\n'
                    'для всех выбранных полей.\n\n'
                    'Введите "y", чтобы перейти в главное меню ... ',

    'require_input': '\nВыберите действие: "{commands}"\n ... ',

    # ---------------------------------------- Handler messages ------------------------------------------------
    'chosen_show_list': '\n---------- ОТОБРАЖЕНИЕ СТАТИСТИКИ ДОХОДОВ/РАСХОДОВ ----------\n',
    'empty_table': 'На данный момент, в базе данных нет записей\n',
    'bad_command': 'Команда не распознана, проверьте введенное значение! \n ... ',

    'statistic': 'Текущий баланс: {summary}\n'
                 'Доход: {income}\n'
                 'Расход: {outcome}\n\n'
                 '---------- СПИСОК ВСЕХ ТРАНЗАКЦИЙ ПО КАТЕГОРИЯМ ------------\n',
    'filter_by_type': 'Выберите категорию транзакций для отображения: {options}\n ... ',

    'income_message': '---------- Доход ------------\n',
    'outcome_message': '---------- Расход ------------\n',

    'chosen_add_note': '\n---------- ДОБАВЛЕНИЕ НОВОЙ ТРАНЗАКЦИИ ----------',
    'input_note_data': 'Пожалуйста, введите значение поля "{field_name}":\n ... ',
    'note_add_success': 'Вы успешно добавили новую транзакцию в базу: \n',

    'chosen_find_notes': '\n---------- НАХОЖДЕНИЕ ТРАНЗАКЦИЙ ----------:',
    'chose_first_arg': 'Выберите параметр для фильтрации: "{options}"\n ... ',
    'first_arg_err': 'Вы выбрали несуществующее поле, проверьте введенное значение!\n ... ',
    'chose_operator': 'Выберите действие над значением поля: "{options}"\n ... ',
    'operator_err': 'Вы выбрали недопустимый оператор, проверьте введенное значение!\n ... ',
    'chose_sub_arg': 'Выберите значение, по которому выбранное поле будет отфильтровано:\n ... ',
    'sub_arg_err': 'Введено недопустимое значение для поля {field}!\n ... ',
    # at this moment, value is empty due to the lack of operators who care about the type of input data
    'add_query': 'Хотите добавить еще одно условие фильтрации? "y/n" ... ',
    'bad_query': 'По вашему запросу не найдено ни одной записи!',

    'chosen_change_notes': '\n---------- ИЗМЕНЕНИЕ ЗАПИСЕЙ -----------',
    'change_fields': 'Укажите через пробел, какие поля вы хотите изменить: "{fields}"\n ... ',
    'unexpected_field': 'Одно или несколько из указанных полей не существует. Проверьте введенные значения! \n ... ',
    'change_field': 'Введите новое значение для поля "{field_name}"\n ... ',

    # -------------------------------------- Database Fields info ----------------------------------------------
    'date': 'Дата',
    'date_regex': '(?:19|20)[0-9]{2}[-\\/ ]?(0?[1-9]|1[0-2])[-/ ]?(0?[1-9]|[12][0-9]|3[01])',

    'type': 'Категория',
    'values_for_type': {'income': 'доход', 'outcome': 'расход'},

    'amount': 'Сумма',

    'descr': 'Описание',

    'exit_message': 'Хорошего дня!',
}


eng_lang = {
    'notfound_command': 'Проверьте введенное значение! Введенное "{command}" не соответствует списку допустимых '
                        'значений "{options}".\n',
    'try_again': 'Попробуйте еще раз: ... ',

    # ---------------------------------------- Initial message -------------------------------------------------
    'start': '\nДобро пожаловать в приложение "Личный финансовый кошелёк"!\n\n'
             'Перед тем, как начать, предлагаем пройти короткое обучение, в котором будет показано, как пользоваться '
             'программой.\n\nХотите пройти обучение? "y/n" ... ',

    # ---------------------------------------- Tutorial section ------------------------------------------------
    'short_description': '\nКраткое описание:\n'
                         'Приложение представляет собой интерактивную телефонную книгу.\n'
                         'Вам доступно 4 основных действия: отобразить определенную страницу книги, добавить \n'
                         'новую запись в книгу, а также отобразить или изменить записи по указанному условию.\n\n'

                         'Каждый раз, когда программе будут необходимы значения для работы, вам будут выведены все \n'
                         'доступные команды. Все команды необходимо набирать ровно также, как и в примере.\n\n'

                         'Далее следуют подробные инструкции по использованию каждой функции.'
                         '\nХотите продолжить? "y/n" ... ',

    'show_page': '\nПоказать страницу:\n'
                 'Чтобы отобразить необходимую страницу, вам следует выбрать опцию "show_page" в главном меню.\n'
                 'Далее вам будет необходимо ввести номер требуемой страницы. Вам будет предоставлена возможность\n'
                 'выбора новых страниц до того момента, как вы не введете команду "exit", которая вернет вас\n'
                 'в главное меню.\n\n'
                 'Хотите продолжить? "y/n" ... ',

    'add_note': '\nДобавить запись:\n'
                'Чтобы добавить новую запись в книгу, вам следует выбрать опцию "add_note" в главном меню.\n'
                'Далее вам потребуется ввести значение для каждого поля телефонной книги по очереди. Входные данные\n'
                'при вводе номеров телефона дополнительно проверяются на корректность.\n'
                'Каждый номер должен начинаться со знака "+".\n'
                'После ввода всех требуемых значений, вам будет показана только что созданная запись.\n\n'
                'Хотите продолжить? "y/n" ... ',

    'find_notes': '\nНайти записи:\n'
                  'Чтобы найти записи по условию, вам следует выбрать опцию "find_notes" в главном меню. \n'
                  'Далее вам будет указать три основных аргумента запроса:\n'
                  '1.  Указать поле, по которому будет совершена фильтрация\n'
                  '2.  Указать оператор, который будет использован в сравнении значений выбранного поля\n'
                  '3.  Указать значение, которое оператор будет сравнивать со значением полей записей\n'
                  'Когда все данные будут корректно указаны, вам будет предложено написать еще один запрос. Так вы\n'
                  'можете создавать сложные запросы с несколькими условиями.\n\n'

                  'Хотите продолжить? "y/n" ... ',
    'change_notes': '\nИзменить записи:\n'
                    'Чтобы изменить существующие записи в книге, вам следует выбрать опцию\n'
                    '"change_notes" в главном меню.\n'
                    'Для начала, процесс аналогичен команде "find_notes", однако после составления запроса вам также\n'
                    'будет необходимо указать поля для изменения. Далее вам будет предложено указать новое значение\n'
                    'для всех выбранных полей.\n\n'
                    'Введите "y", чтобы перейти в главное меню ... ',

    'require_input': '\nВыберите действие: "{commands}"\n ... ',

    # ---------------------------------------- Handler messages ------------------------------------------------
    'chosen_show_list': '\n---------- ОТОБРАЖЕНИЕ СТАТИСТИКИ ДОХОДОВ/РАСХОДОВ ----------\n',
    'empty_table': 'На данный момент, в базе данных нет записей\n',
    'bad_command': 'Команда не распознана, проверьте введенное значение! \n ... ',

    'statistic': 'Текущий баланс: {summary}\n'
                 'Доход: {income}\n'
                 'Расход: {outcome}\n\n'
                 '---------- СПИСОК ВСЕХ ТРАНЗАКЦИЙ ПО КАТЕГОРИЯМ ------------\n',

    'income_message': '---------- Доход ------------\n',
    'outcome_message': '---------- Расход ------------\n',

    'chosen_add_note': '\n---------- ДОБАВЛЕНИЕ НОВОЙ ТРАНЗАКЦИИ ----------',
    'input_note_data': 'Пожалуйста, введите значение поля "{field_name}":\n ... ',
    'note_add_success': 'Вы успешно добавили новую транзакцию в базу: \n',

    'chosen_find_notes': '\n---------- НАХОЖДЕНИЕ ТРАНЗАКЦИЙ ----------:',
    'chose_first_arg': 'Выберите параметр для фильтрации: "{options}"\n ... ',
    'first_arg_err': 'Вы выбрали несуществующее поле, проверьте введенное значение!\n ... ',
    'chose_operator': 'Выберите действие над значением поля: "{options}"\n ... ',
    'operator_err': 'Вы выбрали недопустимый оператор, проверьте введенное значение!\n ... ',
    'chose_sub_arg': 'Выберите значение, по которому выбранное поле будет отфильтровано:\n ... ',
    'sub_arg_err': 'Введено недопустимое значение для поля {field}!\n ... ',
    # at this moment, value is empty due to the lack of operators who care about the type of input data
    'add_query': 'Хотите добавить еще одно условие фильтрации? "y/n" ... ',
    'bad_query': 'По вашему запросу не найдено ни одной записи!',

    'chosen_change_notes': '\n---------- ИЗМЕНЕНИЕ ЗАПИСЕЙ -----------',
    'change_fields': 'Укажите через пробел, какие поля вы хотите изменить: "{fields}"\n ... ',
    'unexpected_field': 'Одно или несколько из указанных полей не существует. Проверьте введенные значения! \n ... ',
    'change_field': 'Введите новое значение для поля "{field_name}"\n ... ',

    # -------------------------------------- Database Fields info ----------------------------------------------
    'date': 'Дата',
    'date_regex': '(?:19|20)[0-9]{2}[-\\/ ]?(0?[1-9]|1[0-2])[-/ ]?(0?[1-9]|[12][0-9]|3[01])',

    'type': 'Категория',
    'values_for_type': {'income': 'Доход', 'outcome': 'Расход'},

    'amount': 'Сумма',

    'descr': 'Описание',

    'exit_message': 'Хорошего дня!',
}



# When adding a new language pack, you must register the new language here
registered_languages = {
    'ru': ru_lang,
}


def get_lang_codes() -> list[str]:
    return [code for code in registered_languages]
