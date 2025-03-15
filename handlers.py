from book.addressbook import AddressBook, BIRTHDAY_FIELD, NAME_FIELD
from book.exceptions import AddressBookError
from book.record import Record


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Incorrect format. Please enter a name and phone number (or birth date) separated by a space."
        except IndexError:
            return "Missing arguments. Ensure you have provided all the necessary data."
        except AddressBookError as e:
            # Для вийнятків, пов'язаних з AddressBook, створений окремий клас
            # для запобігання конфлікту з обробкою ValueError вище
            return str(e)
        except Exception as e:
            return f"Unexpected error: {e}."

    return inner


def parse_input(user_input: str):
    # ValueError, якщо користувач натисне enter або введе " "
    if not user_input.strip():
        return "", []
    
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args: list[str], book: AddressBook):
    name, phone, *_ = args  # ValueError, якщо меньше двох аргументів
    record = book.find(name)
    message = f"Contact '{name}' updated."
    
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = f"Contact '{name}' added."
    
    record.add_phone(phone)

    return message

@input_error
def change_number(args: list[str], book: AddressBook):
    name, old_phone, new_phone, *_ = args  # ValueError, якщо меньше трьох аргументів
    record = book.find(name)
    
    if record is None:
        return f"Contact '{name}' not found."
    
    record.edit_phone(old_phone, new_phone)
        
    return f"Contact '{name}' updated."


@input_error
def get_phone_by_name(args: list[str], book: AddressBook):
    name = args[0]  # IndexError, якщо не вказано ім'я
    record = book.find(name)

    if record is None:
        return f"Contact '{name}' not found."

    return str(record)


def show_all_contacts(book: AddressBook):
    return book.data


@input_error
def add_birthday(args: list[str], book: AddressBook):
    name, birhday, *_ = args  # ValueError, якщо меньше двох аргументів
    record = book.find(name)

    if record is None:
        return f"Contact '{name}' not found."
    
    record.add_birthday(birhday)

    return f"Contact '{name}' updated."


@input_error
def show_birthday(args: list[str], book: AddressBook):
    name = args[0]  # IndexError, якщо не вказано ім'я
    record = book.find(name)

    if record is None:
        return f"Contact '{name}' not found."
    
    return f"{name}'s birthday: {record.birthday}"


def birthdays(book: AddressBook):
    return "\n".join(
        f"Contact name: {data[NAME_FIELD]}, congratulation date: {data[BIRTHDAY_FIELD]}" 
        for data in book.get_upcoming_birthdays()
    ) or "No upcoming birthdays."
