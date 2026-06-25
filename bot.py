from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "8767593090:AAFl5FQE0ViKzetjhjmQVYoYuiDsR-do2oo"

KEYWORDS = {
    ("hello", "hi", "hey"): "Hey! 👋 Busy hoon, baad mein baat karte hain 😊",
    ("urgent",): "Got it! ⚡ Ashish jaldi reply karega",
    ("call", "phone"): "Abhi nahi 📵 Baad mein try karo",
    ("kab", "miloge"): "Pata nahi abhi ⏳ Wait karo",
    ("help",): "Message mila! 🙏 Wait karo",
    ("kya kar rahe", "busy"): "Haan busy hoon 😅 Baad mein baat karte",
    ("ok", "okay", "thik hai"): "👍",
}

DEFAULT_REPLY = "Busy hoon abhi! 🔕 Jaldi reply karunga ✌️"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    reply = DEFAULT_REPLY
    for keywords, response in KEYWORDS.items():
        if any(kw in text for kw in keywords):
            reply = response
            break
    await update.message.reply_text(reply)

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()
