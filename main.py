from handlers import SetLanguageHandler, StartHandler, ShowTutorialHandler, ChooseCommandHandler
from languages import eng_lang


def run(tutorial_steps):
    select_language_handler = SetLanguageHandler(eng_lang)
    language = select_language_handler.operate()

    start_handler = StartHandler(language)
    show_tutorial = start_handler.operate()
    if show_tutorial:
        show_tutorial_handler = ShowTutorialHandler(language, tutorial_steps)
        show_tutorial_handler.operate()

    while True:
        choose_command_handler = ChooseCommandHandler(language, tutorial_steps)
        command_class = choose_command_handler.operate()(language)
        command_class.operate(language)


if __name__ == '__main__':
    tutorial = ()
    run(tutorial)