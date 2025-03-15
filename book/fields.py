from .exceptions import ValidationError
from .helpers import string_to_date

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value: str):
        self._validate_phone(value) 
        super().__init__(value)
    
    def _validate_phone(self, value: str):
        """Перевіряє коректність номера телефону."""
        if not (len(value) == 10 and value.isdigit()):
            raise ValidationError(f"Invalid phone number: '{value}'. The number must be 10 digits long.")
        

class Birthday(Field):
    def __init__(self, value: str):
        try:
            string_to_date(value)  # Спроба преведення дати до формату 'DD.MM.YYYY'
            super().__init__(value)
        except ValueError:
            raise ValidationError(f"Invalid date format: '{value}'. The date must be in 'DD.MM.YYYY' format.")
