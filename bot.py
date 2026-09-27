import telebot

# ضعِ التوكن الخاص بكِ والرقم الطويل مباشرة هنا بين علامات الاقتباس
TOKEN = "اكتبي_هنا_التوكن_الخاص_بِك_من_BotFather"
CHAT_ID = "اكتبي_هنا_الرقم_الطويل_الخاص_بِك_من_userinfobot"

bot = telebot.TeleBot(TOKEN)

def send_alert():
    try:
        # رسالة تأكيدية تفيد بأن البوت يعمل بنجاح
        message = "🤖 بوت التداول يعمل بنجاح ومستعد للتوصيل الفوري!"
        bot.send_message(CHAT_ID, message)
        print("تم إرسال الرسالة بنجاح إلى تليجرام!")
    except Exception as e:
        print(f"حدث خطأ أثناء الإرسال: {e}")

if __name__ == '__main__':
    send_alert()
