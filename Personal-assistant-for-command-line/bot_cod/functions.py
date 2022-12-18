from calendar import isleap
from datetime import datetime as dt

from bot_cod.classes import (
    ADDRESS_BOOK,
    NOTE_BOOK,
    Adress,
    Birthday,
    Email,
    Name,
    NoteText,
    Notification,
    Phone,
    Record,
    Tag,
)
from spellchecker import SpellChecker


def hello_message():
    print("How can I help you?")


def create_contact():
    name = input("Enter the name of the new contact\n")
    try:
        name_obj = Name(name)
        phone = input(f"Enter the phone number for {name}\n")
        try:
            phone_obj = Phone(phone)
            new_contact = Record(name=name_obj, phone=phone_obj)
            ADDRESS_BOOK.add_record(new_contact)
            print(f"Contact {name.capitalize()} with phone {phone} added!")
        except ValueError:
            print(
                "Error. Valid number: 7 to 13 digits. Letters cannot be included in the number"
            )
    except ValueError:
        print("Incorrect name, or the name is already in the contact book")


def add_phone():
    name = input("For which contact should I add another number?\n")
    if name not in ADDRESS_BOOK:
        print("No such contact exists!")
    else:
        new_phone = input(f"Enter new phone number for {name.capitalize()}\n")
        try:
            if new_phone not in ADDRESS_BOOK[name].phone.value:
                ADDRESS_BOOK[name].phone.value.append(new_phone)
                print(
                    f"Phone number {new_phone} has been added to contact {name.capitalize()}"
                )
            else:
                print("The number is duplicated")
        except ValueError:
            print("Invalid number")


def add_adress():
    name = input("For which contact should I add an address?\n")
    if name not in ADDRESS_BOOK:
        print("No such contact exists!")
    else:
        address = input(f"Add address for {name.capitalize()}\n")
        address_obj = Adress(address)
        ADDRESS_BOOK[name].adress = address_obj
        print(f"Address {address} is added for contact {name.capitalize()}")


def add_email():
    name = input("For which contact should I add e-mail?\n")
    if name not in ADDRESS_BOOK:
        print("No such contact exists!")
    else:
        email = input(f"Enter e-mail for {name.capitalize()}\n")
        try:
            email_obj = Email(email)
            ADDRESS_BOOK[name].email = email_obj
            print(f"E-mail {email} has been added to contact {name.capitalize()}")
        except ValueError:
            print("Invalid e-mail")


def add_birthday():
    name = input("For which contact should I add a date of birth?\n")
    if name not in ADDRESS_BOOK:
        print("No such contact exists!")
    else:
        birthday = input("Enter YYYY/MM/DD" "\n").split("/")
        if len(birthday) == 3:
            person_birthday = dt(
                year=int(birthday[0]), month=int(birthday[1]), day=int(birthday[2])
            ).date()
            try:
                ADDRESS_BOOK[name].birthday = Birthday(person_birthday)
                print(
                    f"Date of birth {person_birthday} added for the contact {name.capitalize()}"
                )
            except ValueError:
                print("Error validating birth date")
        else:
            print("Invalid date")


def days_to_birthday(birthday) -> int:
    next_birthday = None
    Feb29_birthdate = False
    if birthday.month == 2 and birthday.day == 29 and not isleap(dt.now().year):
        Feb29_birthdate = True
        birthday_this_year = dt(dt.now().year, 2, 28).date()
    else:
        birthday_this_year = dt(dt.now().year, birthday.month, birthday.day).date()
    if birthday_this_year < dt.date(dt.now()):
        next_birthday = birthday_this_year.replace(year=birthday_this_year.year + 1)
        if Feb29_birthdate and isleap(next_birthday.year):
            next_birthday = birthday_this_year.replace(day=birthday_this_year.day + 1)
    else:
        next_birthday = birthday_this_year
    return (next_birthday - dt.now().date()).days


def show_bday_names():
    days_from_today = int(
        input(
            "For what number of days from today should I show contacts with birthday?\n"
        )
    )
    for name, record in ADDRESS_BOOK.items():
        if record.birthday:
            if days_to_birthday(record.birthday.value) <= days_from_today:
                show_contact(record)


def searcher_people():
    ueser_input = input("Input something that record contains\n")
    search_result = list()
    for record in ADDRESS_BOOK.data.values():

        list_contacts = list()
        if record.name:
            list_contacts.append(record.name.value)

        if record.phone:
            list_contacts.append(", ".join(record.phone.value))

        if record.adress:
            list_contacts.append(record.adress.value)

        if record.email:
            list_contacts.append(record.email.value)

        if record.birthday:
            list_contacts.append(str(record.birthday.value))

        string = "| ".join(list_contacts)

        if ueser_input in string:
            search_result.append(string)
    return print("\n".join(search_result))


def edit_name(record):
    new_name = input("Enter new name\n")
    return record.change_name(new_name)


def edit_phone(record):
    old_phone = input("Enter phone that you want to edit\n")

    if not old_phone in record.phone.value:
        return print("Phone not found")

    new_phone = input("Enter new phone\n")

    return record.change_phone(old_phone, new_phone)


def edit_birthday(record):
    new_birthday = input("Enter YYYY/MM/DD" "\n").split("/")
    return record.change_birthday(new_birthday)


def edit_adress(record):
    new_adress = input("Enter new adress\n")
    return record.change_adress(new_adress)


def edit_email(record):
    new_email = input("Enter new email\n")
    return record.change_email(new_email)


def edit_contact():
    name = input("For which contact I should edit\n")
    if not name in ADDRESS_BOOK.data:
        print("No such contact exists!")
    else:
        record = ADDRESS_BOOK[name]

        parameters_to_edit = ["name", "phone", "birthday", "adress", "email"]

        parameter = input(
            "What you want to edit (name, phone, birthday, address, email)\n"
        ).strip()

        if parameter in parameters_to_edit:

            if parameter == "name":
                output = edit_name(record)

            elif parameter == "phone":
                output = edit_phone(record)

            elif parameter == "birthday":
                output = edit_birthday(record)

            elif parameter == "adress":
                output = edit_adress(record)

            elif parameter == "email":
                output = edit_email(record)

            print(output)

        else:
            print("Incorrect parameter")


def delete_contact():
    user_input = input("Enter contact that you want to delete\n")

    if not user_input in ADDRESS_BOOK:
        return print("Contact not exist")

    del ADDRESS_BOOK[user_input]

    print("Contact successfully delete")


def searcher_notes():
    key_word = input("Enter a keyword or part to search in notes\n...")
    for notes in NOTE_BOOK.values():
        if key_word in notes.tags.value:
            print(f"Found by tags:\n{notes.tags.value}\n\t{notes.notes.value}")
        elif key_word in notes.notes.value:
            print(f"Found in note texts:\n{notes.tags.value}\n\t{notes.notes.value}")
        else:
            print("Not found note or tag")


def show_contact(record: Record):
    print(f"{record.name.get_info()}\n")
    print(f"\tPhones:\t{record.phone.get_info()}\n")
    if record.email:
        print(f"\t{record.email.get_info()}\n")
    if record.adress:
        print(f"\t{record.adress.get_info()}\n")
    if record.birthday:
        print(f"\t{record.birthday.get_info()}\n")


def show_all():
    for record in ADDRESS_BOOK.values():
        show_contact(record)


def notifications():
    action = input(
        "Actions with notes:\nEnter 1 to add a note\nEnter 2 to delete note\nEnter 3 to show all notes\n..."
    )
    if action == "1":
        text_note = input("Enter note text\n...")
        text_note_obj = NoteText(text_note)
        tags = input(
            "Not necessary. Enter tags for the note. (can be several, separated by commas)\n..."
        )
        try:
            tags_obj = Tag(tags)
        except ValueError:
            print("Incorrect tags")
            return False

        note_record = Notification(notes=text_note_obj, tags=tags_obj)
        NOTE_BOOK.add_note(note_record)
        print(f'Added note "{text_note}"')

    if action == "2":
        temp_dict = {}
        items = [notes.notes.value for notes in NOTE_BOOK.values()]
        for i, item in enumerate(items):
            print(i + 1, item)
            temp_dict[i + 1] = item
        number_note_to_del = input("Enter the note number you want to delete\n...")
        try:
            if int(number_note_to_del) in temp_dict:
                for notes in NOTE_BOOK.values():
                    if temp_dict[int(number_note_to_del)] == notes.notes.value:
                        key_for_del = notes.tags.value
            else:
                print("Not found note")
        except ValueError:
            print("Not found note")
            return False

        NOTE_BOOK.pop(key_for_del)
        print("Done!")

    if action == "3":
        for notes in NOTE_BOOK.values():
            print(f"{notes.tags.get_info()}\n\t{notes.notes.get_info()}")

    if action not in ["1", "2", "3"]:
        print("Not found command")


def edit_note():
    action = input(
        "What do you want to edit?\nEnter 1 - tags\nEnter 2 - note text\n..."
    )

    if action == "1":
        temp_dict = {}
        items_for_user = [
            f"{notes.tags.value} | {notes.notes.value}" for notes in NOTE_BOOK.values()
        ]
        for i, item in enumerate(items_for_user):
            print(i + 1, item)
        items_for_program = [notes.tags.value for notes in NOTE_BOOK.values()]
        for i, item in enumerate(items_for_program):
            temp_dict[i + 1] = item
        number_note_to_edit = input("Enter the note number you want to edit tags\n...")
        try:
            if int(number_note_to_edit) in temp_dict:
                for notes in NOTE_BOOK.values():
                    if temp_dict[int(number_note_to_edit)] == notes.tags.value:
                        note_text_obj = notes.notes
                        key_for_edit = notes.tags.value
            else:
                print("Not found note")
                return False
        except ValueError:
            print("Not found note")
            return False

        new_tags = input("Enter new tags for your note\n...")

        try:
            tags_obj = Tag(new_tags)
        except ValueError:
            print("Incorrect tags")

        edited_note_obj = Notification(notes=note_text_obj, tags=tags_obj)
        NOTE_BOOK.pop(key_for_edit)
        NOTE_BOOK.add_note(edited_note_obj)
        print("Tags have been changed!")

    if action == "2":
        temp_dict = {}
        items = [notes.notes.value for notes in NOTE_BOOK.values()]
        for i, item in enumerate(items):
            print(i + 1, item)
            temp_dict[i + 1] = item
        number_note_to_edit = input("Enter the note number you want to edit\n...")
        try:
            if int(number_note_to_edit) in temp_dict:
                for notes in NOTE_BOOK.values():
                    if temp_dict[int(number_note_to_edit)] == notes.notes.value:
                        key_for_edit = notes.tags.value
                        tags_obj = notes.tags
            else:
                print("Not found note")
                return False
        except ValueError:
            print("Not found note")
            return False

        new_notetext = input("Enter new note text:\n...")
        new_notetext_obj = NoteText(new_notetext)
        edited_note_obj = Notification(notes=new_notetext_obj, tags=tags_obj)
        NOTE_BOOK.pop(key_for_edit)
        NOTE_BOOK.add_note(edited_note_obj)
        print("Done!")

    if action not in ["1", "2"]:
        print("Not found command")


def recreate_contacts():
    contacts_in_file = ADDRESS_BOOK.read_contacts_from_file("data_phonebook.bin")
    if contacts_in_file:
        for key, value in contacts_in_file.items():
            ADDRESS_BOOK.data[key] = value


def recreate_notes():
    notes_in_file = NOTE_BOOK.read_contacts_from_file("data_notebook.bin")
    if notes_in_file:
        for key, value in notes_in_file.items():
            NOTE_BOOK.data[key] = value


def get_help(instructions: str):
    print(instructions)


def incorrect_input(user_message: str, user_input: dict):
    my_functions = list(user_input.keys())
    my_functions.extend(["good bye", "close", "exit"])
    spell = SpellChecker()
    suggestions = spell.candidates(user_message)
    if suggestions:
        for suggest in suggestions:
            if suggest in my_functions:
                print(
                    f"{user_message} is not a right function, maybe you mean: '{suggest}'?"
                )
                break
            if len(user_message) <= 2:
                print(
                    f"{user_message} is not a right function, maybe you mean: 'add' or 'all'?"
                )
                break
        else:
            print(f"Sorry can't execute this function: {user_message}.")
    else:
        print(f"Sorry don't know this command: {user_message}")


def only_save():
    ADDRESS_BOOK.write_contacts_to_file("data_phonebook.bin")
    NOTE_BOOK.write_contacts_to_file("data_notebook.bin")
    print("Data saved successfully")
