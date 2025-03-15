from .exceptions import DuplicateError, NotFoundError
from .fields import Name, Phone, Birthday


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Birthday = None

    def add_phone(self, phone: str):
        """Додає новий телефон до запису."""
        if self.find_phone(phone) is not None:
            raise DuplicateError(f"Phone number '{phone}' already exists.")
        
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        """Видаляє телефон із запису."""
        found_phone = self.find_phone(phone)
        if found_phone is None:
            raise NotFoundError(f"Phone number '{phone}' not found.")
        
        self.phones.remove(found_phone)

    def edit_phone(self, old: str, new: str):
        """Замінює телефон на нове значення."""
        for i, phone in enumerate(self.phones):
            if phone.value == old:
                self.phones[i] = Phone(new)
                return
        
        raise NotFoundError(f"Phone number '{old}' not found.")

    def find_phone(self, phone: str) -> Phone | None:
        """Шукає телефон у записі."""
        for p in self.phones:
            if p.value == phone:
                return p
        
        return None
    
    def add_birthday(self, date: str):
        """Додає дату дня народження для запису."""
        current_birthday = Birthday(date)
        
        if self.birthday is not None and self.birthday.value == current_birthday.value:
            raise DuplicateError(f"Date of birth '{current_birthday}' is already set.")
        
        self.birthday = current_birthday

    def remove_birthday(self):
        """Видаляє дату дня народження із запису."""
        if self.birthday is None:
            raise NotFoundError("Date of birth is not set.")
        
        self.birthday = None

    def __str__(self):
        birthday_str = self.birthday or "'empty'"
        phones_str = '; '.join("({0}{1}{2})-{3}{4}{5}-{6}{7}-{8}{9}".format(*p.value) for p in self.phones)
        return f"Contact name: {self.name.value}, birthday: {birthday_str}, phones: {phones_str}"
