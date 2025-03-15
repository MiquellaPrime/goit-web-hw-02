from collections import UserDict
from datetime import date

from .exceptions import DuplicateError, NotFoundError
from .helpers import adjust_for_weekend, date_to_string, string_to_date
from .record import Record

NAME_FIELD = "name"
BIRTHDAY_FIELD = "birhday"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        """Додає запис до адресної книги."""
        if record.name.value in self.data:
            raise DuplicateError(f"Record for '{record.name}' already exists.")
        
        self.data[record.name.value] = record
    
    def find(self, name: str) -> Record | None:
        """Знаходить запис за ім'ям контакта."""
        return self.data.get(name)

    def delete(self, name: str) -> Record:
        """Видаляє запис, повертаючи видалене значення."""
        if self.find(name) is None:
            raise NotFoundError(f"Name '{name}' not found.")
        
        return self.data.pop(name)
    
    def get_upcoming_birthdays(self, days: int = 7) -> list[dict[str, str]]:
        """Повертає список контактів, у яких день народження відбудеться протягом найближчих днів."""
        upcoming_birthdays = []
        today = date.today()

        for name, record in self.data.items():
            if record.birthday is None:
                continue
            
            birthday = string_to_date(record.birthday.value)
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            if 0 <= (birthday_this_year - today).days <= days:
                congratulation_date = adjust_for_weekend(birthday_this_year)

                upcoming_birthdays.append({
                    NAME_FIELD: name, 
                    BIRTHDAY_FIELD: date_to_string(congratulation_date)
                })

        # Сортування словників по даті привітання
        upcoming_birthdays.sort(key=lambda d: string_to_date(d[BIRTHDAY_FIELD]))
        return upcoming_birthdays
    
    def __str__(self):
        return "\n".join(str(self.data[name]) for name in sorted(self.data)) or "Address book is empty."
