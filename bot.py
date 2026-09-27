import os
import telebot

# جلب توكن التليجرام ومعرف الشات بأمان من إعدادات جيتهاب
TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

bot = telebot.TeleBot(TOKEN)

def send_alert():
    try:
        # رسالة تأكيدية تفيد بأن البوت متصل بجيتهاب ويعمل بنجاح
        message = "🤖 بوت التداول يعمل بنجاح ومستعد للتوصيل!"
        bot.send_message(CHAT_ID, message)
        print("تم إرسال الرسالة بنجاح!")
    except Exception as e:
        print(f"حدث خطأ أثناء الإرسال: {e}")

if __name__ == '__main__':
    send_alert()
