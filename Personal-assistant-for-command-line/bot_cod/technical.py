from bot_cod.functions import (
    add_adress,
    add_birthday,
    add_email,
    add_phone,
    create_contact,
    delete_contact,
    edit_contact,
    edit_note,
    hello_message,
    notifications,
    searcher_notes,
    searcher_people,
    show_all,
    show_bday_names,
    only_save,
)
from bot_cod.sorter_files import main_sortuvalka

instructions = """
Phone book:
Add a new contact: "add" 
Add other phone for contact: "phone"
Add contact address: "address"
Add e-mail: "email"
Add date of birth: "birthday"
Birthday alerts for your contacts:"bdays"
Edit contact: "edit"
Show all records: "all"
Search in records: "search"
Delete record: "delete"

Note book:
Operations with notes: "note"
Edit tags or note text: "noteedit"
Search in notes: "findnote"

Files on PC:
For sorting files on you PC: "sort"

See this message again: "help"

Save contacts and notes: "save"
Save and exit: "good bye", "close", "exit"
"""


USER_INPUT = {
    "hello": hello_message,
    "add": create_contact,
    "phone": add_phone,
    "address": add_adress,
    "email": add_email,
    "birthday": add_birthday,
    "all": show_all,
    "edit": edit_contact,
    "sort": main_sortuvalka,
    "note": notifications,
    "findnote": searcher_notes,
    "delete": delete_contact,
    "search": searcher_people,
    "bdays": show_bday_names,
    "noteedit": edit_note,
    "save": only_save,
}
