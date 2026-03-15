import telebot

# Aapka Secret API Token
TOKEN = '8663291478:AAGzQNPjb-J1hVcoFKEJ6byKdbwnkVmFblM'
bot = telebot.TeleBot(TOKEN)

# Jab koi /start command dega, toh bot kya bolega:
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello Bhai! 😎 Main aapka naya Telegram Security Bot hoon. Hukum mere aaka!")

# Jab koi kuch aur type karega:
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Abhi main sirf /start samajhta hoon. Akash master mujhe aur commands sikha rahe hain!")

print("-" * 40)
print("[+] System Online!")
print("[+] Akash_Security_Tools_Bot Jinda ho gaya hai! 🤖")
print("Telegram app mein jaakar /start type karo...")
print("-" * 40)

# Bot ko lagatar chalu rakhne ke liye
bot.infinity_polling()
