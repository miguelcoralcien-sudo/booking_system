"""Модель Table — стол в ресторане."""

class Table:
    def __init__(self, id=None, table_number=None, capacity=None):
        self.id = id
        self.table_number = table_number
        self.capacity = capacity

    def __repr__(self):
        return f"Table(id={self.id}, number={self.table_number}, capacity={self.capacity})"
