from bot_cod.classes import ADDRESS_BOOK, NOTE_BOOK
from bot_cod.functions import get_help, incorrect_input, recreate_contacts, recreate_notes
from bot_cod.technical import USER_INPUT, instructions


def main():

    get_help(instructions)
    recreate_contacts()
    recreate_notes()

    while True:
        user_message = input("...\n").lower()

        if user_message.endswith(" "):
            user_message = user_message.rstrip()
        if not user_message or user_message.startswith(" "):
            continue

        if user_message in ("good bye", "close", "exit"):
            print("Good bye!")
            ADDRESS_BOOK.write_contacts_to_file("data_phonebook.bin")
            NOTE_BOOK.write_contacts_to_file("data_notebook.bin")
            break

        if user_message == "help":
            get_help(instructions)
        if user_message in USER_INPUT:
            USER_INPUT[user_message]()

        if user_message not in USER_INPUT:
            incorrect_input(user_message, USER_INPUT)


if __name__ == "__main__":
    main()
