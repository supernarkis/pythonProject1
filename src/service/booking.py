from datetime import datetime
from src.Repository.Book_repo import BookingRepository


class BookingService:
    def __init__(self, booking_repo: BookingRepository):
        self._booking_repo = booking_repo

    def create (self, user_id: str, book_at: datetime):
        dto = {
            "user_id": user_id,
            "book_at": book_at
        }
        booking = self._booking_repo.create(dto)

        return booking


