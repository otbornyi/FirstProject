import telebot

import commands
import tgKey

bot = telebot.TeleBot(tgKey.priv())

commands.botCommands()

bot.polling(non_stop=True)
