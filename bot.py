import telebot

TOKEN = "8767593090:AAFl5FQE0ViKzetjhjmQVYoYuiDsR-do2oo"
bot = telebot.TeleBot(TOKEN)

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

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()
    reply = DEFAULT_REPLY
    for keywords, response in KEYWORDS.items():
        if any(kw in text for kw in keywords):
            reply = response
            break
    bot.reply_to(message, reply)

bot.infinity_polling()
