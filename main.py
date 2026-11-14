from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "ضع_توكن_البوت_هنا"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 أهلاً بك في الصافي الذكي PRO\n\n"
        "🤖 بوت تحليل الذهب XAUUSD\n"
        "📊 تحليل فريم 5 و15 دقيقة\n\n"
        "قريباً إشارات البيع والشراء."
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
