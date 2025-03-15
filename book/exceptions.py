class AddressBookError(Exception):
    """Базовий клас для всіх винятків адресної книги."""


class ValidationError(AddressBookError):
    """Помилка валідації полів."""


class DuplicateError(AddressBookError):
    """Помилка дублювання (наприклад, телефонний номер або контакт вже існує)."""


class NotFoundError(AddressBookError):
    """Помилка відсутності об'єкта (наприклад, контакт або телефон не знайдено)."""
