from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8895147185:AAHKDtP3QULgi3OmZZI4uYOuzlASHupSmIk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚖 أهلاً بك في بوت بغداد تك تك!\n"
        "البوت اشتغل بنجاح ✅"
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
