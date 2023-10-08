import telebot
from telebot import types
bot=telebot.TeleBot("5270464109:AAGxcNawuHl_yH0Zjnz96Wg8pfEp6JQBKHc")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, старина. Пропиши /button для удобства. ')
@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Что у тебя нового?")
    item2=types.KeyboardButton("Подскажи мне кое-что.")
    item3=types.KeyboardButton("Мне нужен совет.")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(message.chat.id,'Чего тебе сегодня? Не парься, это за счёт заведения.',reply_markup=markup)
    
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == "Что у тебя нового?":
        answer = 'Да, впрочем ничего. Как и хотел, открыл магазинчик. Вроде всё налаживается.'
    elif message.text.strip() == "Привет от Егаша.":
        answer = "Ты откуда это нашёл? Выброси это."
    elif message.text.strip() == "Подскажи мне кое-что.":
        answer = "Погоди, я тут ещё не доделал."
    elif message.text.strip() == "Мне нужен совет.":
        answer = "Всем нам иногда нужен совет. Однажды мне сказали: ''Главное - слушать себя. То, что первое приходит в голову - это то, что надо слушать.''. Не помню, что стало со сказавшим, но советом я пользуюсь до сих пор."
    bot.send_message(message.chat.id, answer)


if __name__ == '__main__':
    bot.infinity_polling()