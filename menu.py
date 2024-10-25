import telebot
import tgKey

bot = telebot.TeleBot(tgKey.priv())

@bot.message_handler(commands=["Rolls"])
def menuRolls(message):
            bot.send_message(message.chat.id,"Роллы :\nРолл с крабом : 250 рублей\nРолл с огурцом : 150 рублей\nРолл со сливочным сыром и лососем : 350 рублей\nНабор из 3 видов ролл : 700 рублей")

@bot.message_handler(commands=["Pizza"])
def menuPizza(message):
            bot.send_message(message.chat.id,"Пиццы :\nПицца 4 сыра : 350 рублей\nПицца Гавайская : 400 рублей\nПицца мясное ассорти : 450 рублей\nНабор из трех пицц : 1100 рублей")

@bot.message_handler(commands=["Drinks"])
def menuDrinks(message):
            bot.send_message(message.chat.id,"Напитки :\nМорс : 110 рублей\nЛимонад в ассортименте(Фанта, Спрайт, Кола) : 150 рублей\nВода(газ/негаз) : 80 рублей")

@bot.message_handler(commands=["Sause"])
def menuSause(message):
            bot.send_message(message.chat.id,"Соусы :\nСырный : 70 рублей\nКетчуп : 50 рублей\nЧесночный : 80 рублей")