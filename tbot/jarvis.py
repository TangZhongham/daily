from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

from functions.sites import SitesInformation
from tbot import start, echo
import os

def main():
    token = open('.token', 'r')
    application = ApplicationBuilder().token(token.readline()).build()

    sites = SitesInformation(os.path.join(
        os.path.dirname(__file__), "functions/resources/data.json"))
    site_data_all = {site.name: site.url for site in sites}
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    application.run_polling()