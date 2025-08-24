
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8282174001:AAHIDJ-BBJoRJ_G1rf04O6PcF8xFKcHKvgA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello 👋! I am your PharmCare Bot. How can I help you today?")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You can use /start to begin chatting with me.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
