from handlers import SetLanguageHandler, WelcomeHandler, ShowTutorialHandler, ChooseCommandHandler, \
    commands, database_fields
from languages import eng_lang
from signals import ExitSignal


def run(tutorial_steps):
    # Setting the interface language
    select_language_handler = SetLanguageHandler(eng_lang)
    language = select_language_handler.operate()

    start_handler = WelcomeHandler(language)
    show_tutorial = start_handler.operate()
    if show_tutorial:  # Training is optional
        show_tutorial_handler = ShowTutorialHandler(language, tutorial_steps)
        show_tutorial_handler.operate()

    # An infinite loop that prompts the user for a command to execute.
    # After receiving a command in string representation, calls the corresponding handler from the commands dictionary

    while True:
        try:
            choose_command_handler = ChooseCommandHandler(language, commands)
            command_class = choose_command_handler.operate()(language, database_fields)
            command_class.operate()
        except ExitSignal:  # Waits for an 'exit' signal from the user to terminate the command early
            pass


if __name__ == '__main__':
    tutorial = ('short_description', 'show', 'add', 'find', 'change')
    run(tutorial)
