from abc import ABC, abstractmethod

from book.record import Record


class BaseView(ABC):
    """Абстрактний базовий клас для відображення інформації."""

    @abstractmethod
    def display_message(self, message):
        """Метод для відображення повідомлень."""
        pass
    
    @abstractmethod
    def display_contacts(self, contacts):
        """Метод для відображення списку контактів."""
        pass

    @abstractmethod
    def display_commands(self, commands):
        """Метод для відображення списку доступних команд."""
        pass


class ConsoleView(BaseView):
    """Консольне представлення даних."""

    def display_message(self, message: str):
        """Виводить повідомлення у консоль."""
        print(message)
    
    def display_contacts(self, contacts: dict[str, Record]):
        """Виводить список контактів у консоль."""
        if not contacts:
            print("Address book is empty.")
        
        print("Contact list:")
        for name in sorted(contacts):
            print(str(contacts[name]))
    
    def display_commands(self, commands: dict[str, str]):
        """Виводить список доступних команд у консоль."""
        print("Allowed commands:")
        for i, (command, description) in enumerate(commands.items()):
            print(f"{i + 1:<2} {command:<15} - {description}")
