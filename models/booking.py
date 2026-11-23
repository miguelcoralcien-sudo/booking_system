"""Модель Booking — бронирование стола."""

class Booking:
    def __init__(self, id=None, user_id=None, table_id=None, booking_date=None, start_time=None, end_time=None):
        self.id = id
        self.user_id = user_id
        self.table_id = table_id
        self.booking_date = booking_date
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"Booking(id={self.id}, user={self.user_id}, table={self.table_id}, date={self.booking_date})"
