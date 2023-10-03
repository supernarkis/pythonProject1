import telebot

from src.Repository.Book_repo import BookingRepository
from src.service.booking import BookingService
#test
if __name__ == '__main__':
    bot = telebot.TeleBot("6597726469:AAGhDP1cK1uS2Zu16h1uJoBtbzonaG7gUOg", parse_mode=None)  # You can set parse_mode by default. HTML or MARKDOWN
    service = BookingService(BookingRepository())


    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Привет. Бронируй ресурсы тут.")

    @bot.message_handler(commands=['book'])
    def send_welcome(message):
        bot.reply_to(message, "Для бронирования укажи дату в формате ГГГГ.ММ.ДД ЧЧ:ММ")

    @bot.message_handler(regexp="\d\d\d\d.\d\d.\d\d\s\d\d:\d\d:\d\d")
    def handle_any_text(message):
        date, time = message.text.replace(".","-").split(" ")
        from datetime import datetime
        booked_at = datetime.fromisoformat(f"{date}T{time}Z")

        service.create(message.from_user.id, booked_at)
        bot.reply_to(message, "Забронировано")

    bot.infinity_polling()
