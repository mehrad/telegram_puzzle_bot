import logging
import random
import sys

from telegram.ext import Updater, CommandHandler

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

mode = 'prod'
if mode == "dev":
    def run(updater):
        updater.start_polling()
elif mode == "prod":
    def run(updater):
        logger.info('here')
        updater.start_webhook(listen='0.0.0.0', port=, url_path=TOKEN)
        updater.bot.set_webhook(webhook_url='https://url/token',
                                certificate=open('/etc/ssl/certs/nginx-selfsigned.crt', 'rb'))
else:
    logger.error("No MODE specified!")
    sys.exit(1)


def start_handler(bot, update):
    logger.info("User {} started bot".format(update.effective_user["id"]))
    update.message.reply_text("Hello from Python!\nPress /random to get random number")


def random_handler(bot, update):
    number = random.randint(0, 10)
    logger.info("User {} randomed number {}".format(update.effective_user["id"], number))
    update.message.reply_text("Random number: {}".format(number))


if __name__ == '__main__':
    logger.info("Starting bot")
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler("start", start_handler))
    updater.dispatcher.add_handler(CommandHandler("random", random_handler))

    run(updater)
