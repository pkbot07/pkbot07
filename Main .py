from telegram.ext import Updater, CommandHandler
import os

TOKEN = os.environ.get("TOKEN")

def start(update, context):
    update.message.reply_text("Extractor Bot Live Hai! 🔥")

def stats(update, context):
    update.message.reply_text(
        "📊 Total Links: 681\n"
        "🎬 Total Videos: 372\n"
        "📄 Total PDFs: 309\n"
        "🔒 DRM Videos: 0\n"
        "🎞️ Perospero Videos: 299"
    )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("stats", stats))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
