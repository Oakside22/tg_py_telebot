import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Тесты")
    button2 = types.KeyboardButton("Проверить ответы")
    markup.add(button1, button2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}, я бот для решения тестов!".format(message.from_user),
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Проверить ответы"):
        bot.send_message(message.chat.id, text="<ответы>")
    elif (message.text == "Тесты"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("<тест 1>")
        button2 = types.KeyboardButton("<тест 2>")
        back = types.KeyboardButton("Вернуться назад")
        markup.add(button1, button2, back)
        bot.send_message(message.chat.id, text="Ты можешь выбрать тест", reply_markup=markup)

    elif (message.text == "<тест 1>"):
        bot.send_message(message.chat.id, "<отправить тест 1>")

    elif message.text == "<тест 2>":
        bot.send_message(message.chat.id, text="<отправить тест 2>")

    elif (message.text == "Вернуться назад"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Проверить ответы")
        button2 = types.KeyboardButton("Тесты")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись назад", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="wwhat ?")


bot.polling(none_stop=True)