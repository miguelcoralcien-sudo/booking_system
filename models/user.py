"""Модель User — пользователь системы бронирования."""

class User:
    def __init__(self, id=None, name=None, phone=None):
        self.id = id
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', phone='{self.phone}')"
