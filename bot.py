import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Токен вашего бота (уже вставлен)
BOT_TOKEN = "8923333975:AAGRvM-xKKZqMfzF8N5x1MMGb5G4lQTqAYE"

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Текст автоответа
AUTO_REPLY_TEXT = (
    "Я — бот-заменитель! Владелец сейчас недоступен "
    "(возможно, он спит, ест или спасает галактику). "
    "Я передам ему твоё сообщение, как только он появится!"
)

# Обработчик всех личных сообщений (не команд)
@dp.message(lambda message: message.chat.type == "private")
async def auto_reply(message: types.Message):
    # Создаём инлайн-кнопку
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="✅ Понятно", callback_data="understood"))

    # Отправляем ответ с кнопкой
    await message.answer(AUTO_REPLY_TEXT, reply_markup=builder.as_markup())

# Обработчик нажатия на кнопку
@dp.callback_query(lambda c: c.data == "understood")
async def process_understood(callback: types.CallbackQuery):
    # Редактируем сообщение – убираем кнопку и меняем текст
    await callback.message.edit_text(
        "Сообщение будет передано владельцу. Спасибо!",
        reply_markup=None
    )
    # Закрываем уведомление о нажатии
    await callback.answer()

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
