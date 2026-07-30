from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8895147185:AAFVV0gnN_bhjJ7PKebm6okpIUWoVa2uePw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🚖 اطلب تك تك"],
        ["📦 توصيل طلب"],
        ["💰 الأسعار"],
        ["☎️ اتصل بي"],
        ["ℹ️ عن الخدمة"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "🚖 أهلاً بك في بغداد تك تك\n\nاختر الخدمة التي تريدها:",
        reply_markup=reply_markup
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
