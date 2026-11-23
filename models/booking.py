class Booking:
    __tablename__ = "bookings"
    id: int
    user_id: int
    table_id: int
    start_time: str
    end_time: str