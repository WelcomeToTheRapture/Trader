from django.conf import settings
from django.apps import AppConfig
from django.contrib.auth.models import User
import logging
import telegram.bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from API.models.telegram import TelegramData


class TelegramBotConfig(AppConfig):
    name = "API.Telegram"
    verbose_name = "TelegramBot"

    def ready(self):
        bot = TelegramBot()
        bot.start_bot()


class TelegramBot():
    def start_bot(self):
        token = settings.TOKEN
        updater = Updater(token=token)
        # bot = telegram.Bot(token=TOKEN)
        dispatcher = updater.dispatcher
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

        def help(bot, update):
            bot.send_message(chat_id=update.message.chat_id, text="To register to notifications please use the "
                                                                  "following command: /register [Email]")

        def register(bot, update):
            email = str.strip(update.message.text[10])
            if not email:
                register_text = ("To register to notifications please use the "
                                 "following command: /register [Email]")
            else:
                user = User.objects.filter(email=email)
                if user:
                    register_text = "User successfully registered"
                    TelegramData.objects.create(usuario=user, chat_id=update.message.chat_id)
                else:
                    register_text = "The user does not exist, please verify the email."
            bot.send_message(chat_id=update.message.chat_id, text=register_text)

        def caps(bot, update, args):
            if args:
                text_caps = ' '.join(args).upper()
            else:
                text_caps = 'NO MESSAGE PROVIDED'
            bot.send_message(chat_id=update.message.chat_id, text=text_caps)

        def unknown(bot, update):
            bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

        help_handler = CommandHandler('start', help)
        register_handler = MessageHandler(Filters.text, register)
        caps_handler = CommandHandler('caps', caps, pass_args=True)
        register_help_handler = CommandHandler('register', register)
        unknown_handler = MessageHandler(Filters.command, unknown)
        dispatcher.add_handler(help_handler)
        dispatcher.add_handler(register_handler)
        dispatcher.add_handler(register_help_handler)
        dispatcher.add_handler(caps_handler)
        dispatcher.add_handler(unknown_handler)
        updater.start_polling()
        updater.idle()

    def stop_bot(self):
        token = settings.TOKEN
        updater = Updater(token=token)
        updater.stop()
