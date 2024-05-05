ru_lang = {
    'notfound_command': 'Проверьте введенное значение! Введенное "{command}" не соответствует списку допустимых '
                        'значений "{options}".\n',
    'try_again': 'Попробуйте еще раз: ... ',
    'start': '\nДобро пожаловать в приложение "Интерактивная телефонная книга"!\n\n'
             'Перед тем, как начать, предлагаем пройти короткое обучение, в котором будет показано, как пользоваться '
             'программой.\n\nХотите пройти обучение? "y/n" ... ',

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

    'chosen_show_list': '\n---------- ОТОБРАЖЕНИЕ СТАТИСТИКИ ДОХОДОВ/РАСХОДОВ ----------\n',
    'empty_table': 'На данный момент, таблица пуста\n',
    'chose_page': 'Выберите номер страницы (от 1 до {pages}), либо "exit", чтобы выйти: \n ... ',
    'bad_page': 'Введенной страницы не существует. Попробуйте снова:\n ... ',
    'bad_command': 'Команда не распознана, проверьте введенное значение! \n ... ',

    'chosen_add_note': '\n---------- ДОБАВЛЕНИЕ НОВОЙ ЗАПИСИ ----------',
    'input_note_data': 'Пожалуйста, введите значение поля "{field_name}":\n ... ',
    'bad_phone_number': 'Введенный номер некорректен. Попробуйте снова:\n ... ',
    'note_add_success': 'Вы успешно добавили новую запись в книгу: \n',

    'chosen_find_notes': '\n---------- НАХОЖДЕНИЕ ЗАПИСЕЙ ----------:',
    'chose_first_arg': 'Выберите параметр для фильтрации: "{options}"\n ... ',
    'first_arg_err': 'Вы выбрали несуществующее поле, проверьте введенное значение!\n ... ',
    'chose_operator': 'Выберите действие над значением поля: "{options}"\n ... ',
    'operator_err': 'Вы выбрали недопустимый оператор, проверьте введенное значение!\n ... ',
    'chose_sub_arg': 'Выберите значение, по которому выбранное поле будет отфильтровано:\n ... ',
    'sub_arg_err': '',
    # at this moment, value is empty due to the lack of operators who care about the type of input data
    'add_query': 'Хотите добавить еще одно условие фильтрации? "y/n" ... ',
    'bad_query': 'По вашему запросу не найдено ни одной записи!',

    'chosen_change_notes': '\n---------- ИЗМЕНЕНИЕ ЗАПИСЕЙ -----------',
    'change_fields': 'Укажите через пробел, какие поля вы хотите изменить: "{fields}"\n ... ',
    'unexpected_field': 'Одно или несколько из указанных полей не существует. Проверьте введенные значения! \n ... ',
    'change_field': 'Введите новое значение для поля "{field_name}"\n ... ',
    'exit_message': 'Хорошего дня!',
}

eng_lang = {
    'select_language': 'Good afternoon!\n'
                       'Before you start, select your interface language: {options} ... ',
    'notfound_command': 'Check the entered value! The entered "{command}" does not match the list of valid '
                        'values "{options}".\n',
    'try_again': 'Try again: ...  ',
    'start': '\nWelcome to the Interactive Phone Book application!\n\n'
             'Before you start, we suggest you complete a short training session that will show you how to'
             ' use this program.'
             '\n\nDo you want to get trained? "y/n" ...',

    'short_description': '\nShort description:\n'
                         'The application is an interactive phone book.\n'
                         'There are 4 main actions available to you: display a specific book page, add \n'
                         'a new entry in the book, as well as display or change entries '
                         'based on the specified condition.\n\n'

                         'Every time the program needs values to work, all of them will be displayed to you. \n'
                         'available commands. All commands must be typed exactly as in the example.\n\n'

                         'Detailed instructions for using each function follow.'
                         '\nDo you want to continue?? "y/n" ... ',

    'show_page': '\nShow page:\n'
                 'To display the required page, you should select the "show_page" option in the main menu.\n'
                 'Next you will need to enter the number of the required page. You will be given the opportunity\n'
                 'select new pages until you enter the "exit" command, which will return you\n'
                 'to the main menu.\n\n'
                 'Do you want to continue? "y/n" ...',

    'add_note': '\nAdd entry:\n'
                'To add a new entry to the book, you should select the "add_note" option from the main menu.\n'
                'Next you will need to enter a value for each phone book field in turn. Input data\n'
                'When entering phone numbers, they are additionally checked for correctness.\n'
                'Each number must begin with a "+" sign.\n'
                'Once you have entered all the required values, you will be shown the newly created entry.\n\n'
                'Do you want to continue? "y/n" ... ',

    'find_notes': '\nFind notes:\n'
                  'To find notes by condition, you should select the "find_notes" option from the main menu. \n'
                  'Next you will be given three main request arguments:\n'
                  '1. Specify the field by which filtering will be performed\n'
                  '2. Specify the operator that will be used to compare the values of the selected field\n'
                  '3. Specify the value that the operator will compare with the value of the record fields\n'
                  'When all the data is entered correctly, you will be asked to write another request. So you\n'
                  'you can create complex queries with multiple conditions.\n\n'

                  'Do you want to continue? "y/n" ... ',
    'change_notes': '\nEdit notes:\n'
                    'To change existing notes in the book, you should select the option\n'
                    '"edit_notes" in the main menu.\n'
                    'To begin with, the process is similar to the "find_notes" command, '
                    'but after making a request you also\n'
                    'it will be necessary to specify the fields to change.'
                    'Next you will be asked to specify a new value\n'
                    'for all selected fields.\n\n'
                    'Enter "y" to go to the main menu...',

    'require_input': '\nChoose an action: "{commands}"\n ... ',

    'chosen_show_list': '\n--------- PAGE DISPLAY ----------\n',
    'empty_table': ' At this moment, the table is empty\n',
    'chose_page': 'Select page number (from 1 to {pages}), or "exit" to exit: \n ... ',
    'bad_page': 'The entered page does not exist. Try again:\n ... ',
    'bad_command': 'The command is not recognized, check the entered value! \n... ',

    'chosen_add_note': '\n--------- ADDING A NEW NOTE ----------',
    'input_note_data': 'Please enter the value of the field "{field_name}":\n ... ',
    'bad_phone_number': 'The number entered is incorrect. Try again:\n ... ',
    'note_add_success': 'You have successfully added a new entry to the book:\n',

    'chosen_find_notes': '\n--------- FINDING NOTES ----------:',
    'chose_first_arg': 'Select an option to filter: "{options}"\n ... ',
    'first_arg_err': 'You have selected a non-existent field, check the entered value!\n ... ',
    'chose_operator': 'Choose an action on the field value: "{options}"\n ... ',
    'operator_err': 'You have selected an invalid operator, check the value you entered!\n ... ',
    'chose_sub_arg': 'Choose the value by which the selected field will be filtered:\n ... ',
    'sub_arg_err': '',
    # at this moment, value is empty due to the lack of operators who care about the type of input data
    'add_query': 'Do you want to add another filter condition? "y/n" ... ',
    'bad_query': 'No records were found for your query!',

    'chosen_change_notes': '\n--------- CHANGE NOTES -----------',
    'change_fields': 'Specify, separated by a space, which fields you want to change: "{fields}"\n ... ',
    'unexpected_field': 'One or more of the specified fields does not exist. Check the entered values! \n... ',
    'change_field': 'Enter a new value for the field "{field_name}"',
    'exit_message': 'Have a nice day!',
}

# When adding a new language pack, you must register the new language here
registered_languages = {
    'ru': ru_lang,
    'en': eng_lang,
}


def get_lang_codes() -> list[str]:
    return [code for code in registered_languages]
