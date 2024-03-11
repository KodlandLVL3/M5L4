import telebot
from telebot import types

from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.send_message(message.chat.id, "Какую маску применить?", reply_markup=create_inline_keyboard())

def create_inline_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    buttons = ["Маска 1", "Маска 2", "Маска 3", "Маска 4", "Маска 5"]
    for idx, btn_text in enumerate(buttons, start=1):
        button = types.InlineKeyboardButton(text=btn_text, callback_data=str(idx))
        keyboard.add(button)
    return keyboard

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(call.message.chat.id, f"Выбрана маска {call.data}")

bot.polling()
