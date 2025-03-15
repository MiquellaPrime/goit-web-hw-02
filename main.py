from book.view import ConsoleView
from handlers import (
    parse_input,
    add_contact,
    change_number,
    get_phone_by_name,
    show_all_contacts,
    add_birthday,
    show_birthday,
    birthdays,
)
from storage import load_data, save_data

ALLOWED_COMMANDS = {
    "hello": "Displays a greeting and offers help.",
    "add": "Adds a new contact to the phone book. Format: add <name> <phone>.",
    "change": "Changes the phone number of an existing contact. Format: change <name> <old_phone> <new_phone>.",
    "phone": "Returns the phone number(s) associated with a name. Format: phone <name>.",
    "all": "Displays all contacts in the phone book.",
    "add-birthday": "Adds a birthday for a contact. Format: add-birthday <name> <date(dd.mm.yyyy)>.",
    "show-birthday": "Shows the birthday of a contact. Format: show-birthday <name>.",
    "birthdays": "Displays a list of people who have upcoming birthdays.",
    "help": "Displays a list of available commands and their descriptions.",
    "close": "Saves changes and exits the program. You can also use the commands 'exit' or 'stop'.",
}


def main():
    book = load_data()
    view = ConsoleView()

    view.display_message("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "stop"]:
            save_data(book)
            view.display_message("Good bye!")
            break

        elif command == "hello":
            view.display_message("Hey there! Need help? Just type 'help' to see what I can do!")
        
        elif command == "help":
            view.display_commands(ALLOWED_COMMANDS)
        
        elif command == "add":
            view.display_message(add_contact(args, book))
        
        elif command == "change":
            view.display_message(change_number(args, book))
        
        elif command == "phone":
            view.display_message(get_phone_by_name(args, book))
        
        elif command == "all":
            view.display_contacts(show_all_contacts(book))

        elif command == "add-birthday":
            view.display_message(add_birthday(args, book))

        elif command == "show-birthday":
            view.display_message(show_birthday(args, book))

        elif command == "birthdays":
            view.display_message(birthdays(book))
        
        else:
            view.display_message("Invalid command.")


if __name__ == "__main__":
    main()
