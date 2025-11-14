import os
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

words = ["привет", "компьютер", "программа", "телефон", "ботаник", "солнце", "кофе", "музыка", "игра", "книга"]

def generate_word():
    return random.choice(words)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Случайное слово: {generate_word()}")

async def word(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Случайное слово: {generate_word()}")

def main():
    token = os.environ.get('TOKEN')
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("word", word))
    application.run_polling()

if __name__ == "__main__":
    main()
