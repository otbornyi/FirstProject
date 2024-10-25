import telebot
import webbrowser

from telebot import types

import tgKey
import menu

bot = telebot.TeleBot(tgKey.priv())
def botCommands():
    @bot.message_handler(commands = ['about'])
    def about(message):
        bot.send_message(message.chat.id, ' Мы крупная федеральная сеть доставки вкуснейших суши и роллов"Koldun-Boldun"\n Мы занимаемся этим делом с 2015 года и готовы предложить вам продукцию из свежайших ингридиентов\n У нас вы можете заказать как через данного бота так и по телефону +7 999 999 99 99 ' )

    @bot.message_handler(commands = ["start"])
    def start(message):
        markup = types.ReplyKeyboardMarkup()
        butn1 = types.KeyboardButton('О нас')
        butn2 = types.KeyboardButton('Адреса доставок')
        butn3 = types.KeyboardButton('Меню')
        butn4 = types.KeyboardButton('Обратная связь')

        markup.row(butn1, butn2, butn3, butn4)
        bot.send_message(message.chat.id, "Выбери из кнопок внизу",reply_markup=markup)
        bot.register_next_step_handler(message, on_click)
    def on_click(message):
        if message.text == 'О нас':
            about(message)
            start(message)

        elif message.text == 'Адреса доставок':
            adress(message)
            start(message)

        elif message.text == 'Меню':
            menu1(message)

        elif message.text == 'Обратная связь':
            feedback(message)
            start(message)



    @bot.message_handler(commands=["adress"])
    def adress(message):
        bot.send_message(message.chat.id, f"Мы осуществляем доставки по:\n Мурино - стоимость доставки 300 рублей(при заказе от 2000 бесплатно)\n Пранас - стоимость доставки 400 рублей(при заказе от 2000 бесплатно)\n Кудрово - стоимость доставки 500 рублей")

    @bot.message_handler(commands=["menu"])
    def menu1(message):
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Роллы', callback_data = 'rolls')
        btn2 = types.InlineKeyboardButton('Пицца', callback_data='pizza')
        btn3 = types.InlineKeyboardButton('Напитки', callback_data='drinks')
        btn4 = types.InlineKeyboardButton('Соусы', callback_data='sause')

        markup.row(btn1,btn2,btn3,btn4)
        bot.reply_to(message, "Выбери нужный раздел",reply_markup = markup)
    @bot.callback_query_handler(func=lambda callback: True)
    def callback_message(callback):
        if callback.data == 'rolls':
            bot.send_message(callback.message.chat.id, menu.menuRolls())
        if callback.data == 'pizza':
            bot.send_message(callback.message.chat.id, menu.menuPizza())
        if callback.data == 'drinks':
            bot.send_message(callback.message.chat.id, menu.menuDrinks())
        if callback.data == 'sause':
            bot.send_message(callback.message.chat.id, menu.menuSause())


    @bot.message_handler(commands=["feedback"])
    def feedback(message):
        bot.send_message(message.chat.id, "Если вам не довезли заказ, нагрубили , вам не понравилась еда или вы хотите оставить хороший отзыв можете сделать это в чате с нашим директором - @otbornyi")

    @bot.message_handler()
    def info(message):
        if message.text.lower() == 'привет' :
            bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}")
        else:
            bot.send_message(message.chat.id, f"Выбери одну из кнопок внизу", start(message))



    bot.polling(non_stop=True)