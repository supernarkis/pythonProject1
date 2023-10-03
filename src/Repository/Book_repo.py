from typing import List

class BookingRepository:
    _bookings = []

    def create(self,dto:dict)->dict:
        self._bookings.append(dto)

        return dto
    def get_by_user_id(self, user_id) -> List[dict]:
        result=[]

        for book in self._bookings:
            if book.user_id ==user.id:
                result.append(book)

            return result

