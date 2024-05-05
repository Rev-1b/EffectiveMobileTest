from handlers import SetLanguageHandler, StartHandler, ShowTutorialHandler, ChooseCommandHandler, commands, \
    database_fields
from languages import eng_lang, ru_lang


def run(tutorial_steps):
    # select_language_handler = SetLanguageHandler(eng_lang)
    # language = select_language_handler.operate()

    language = ru_lang

    # start_handler = StartHandler(language)
    # show_tutorial = start_handler.operate()
    # if show_tutorial:
    #     show_tutorial_handler = ShowTutorialHandler(language, tutorial_steps)
    #     show_tutorial_handler.operate()

    while True:
        choose_command_handler = ChooseCommandHandler(language, commands)
        command_class = choose_command_handler.operate()(language, database_fields)
        command_class.operate()


if __name__ == '__main__':
    tutorial = ()
    run(tutorial)
