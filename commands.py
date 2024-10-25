import telebot
import webbrowser
import tgKey
bot = telebot.TeleBot(tgKey.priv())
def botCommands():
    @bot.message_handler(commands = ['about'])
    def about(message):
        bot.send_message(message.chat.id, ' Мы крупная федеральная сеть доставки вкуснейших суши и роллов"Koldun-Boldun"\n Мы занимаемся этим делом с 2015 года и готовы предложить вам продукцию из свежайших ингридиентов\n У нас вы можете заказать как через данного бота так и по телефону +7 999 999 99 99 ' )

    @bot.message_handler(commands = ["start"])
    def main(message):
        bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}, жмакай понравившуюся кнопку")

    @bot.message_handler(commands=["adress"])
    def main(message):
        bot.send_message(message.chat.id, f"Мы осуществляем доставки по:\n Мурино - стоимость доставки 300 рублей(при заказе от 2000 бесплатно)\n Пранас - стоимость доставки 400 рублей(при заказе от 2000 бесплатно)\n Кудрово - стоимость доставки 500 рублей")

    @bot.message_handler(commands=["menu"])
    def main(message):
        bot.send_message(message.chat.id," Бла-бла - 300р\n Бла-бла - 300р\n Бла-бла - 300р\n Бла-бла - 300р\n")

    @bot.message_handler(commands=["feedback"])
    def main(message):
        bot.send_message(message.chat.id, "Если вам не довезли заказ, нагрубили , вам не понравилась еда или вы хотите оставить хороший отзыв можете сделать это в чате с нашим директором - @otbornyi")

    @bot.message_handler()
    def info(message):
        if message.text.lower() == 'привет' :
            bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}")
        else:
            bot.send_message(message.chat.id, f"Тебе нужно выбрать одну из кнопок :)")

    bot.polling(non_stop=True)