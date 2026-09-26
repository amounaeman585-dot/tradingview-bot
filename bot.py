import os
from flask import Flask, request, jsonify
import telebot

# إعداد خادم الويب
app = Flask(__name__)

# جلب توكن التليجرام ومعرف الشات من بيئة العمل بأمان
TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

bot = telebot.TeleBot(TOKEN)

@app.route('/')
def home():
    return "البوت يعمل بنجاح ومستعد لاستقبال التنبيهات!"

@app.route('/webhook', methods=['POST'])
def webhook():
    # استقبال التنبيه القادم من TradingView
    data = request.get_data(as_text=True)
    
    try:
        # إرسال التنبيه مباشرة إلى قناتك أو حسابك في تليجرام
        bot.send_message(CHAT_ID, data)
        return jsonify({"status": "success", "message": "تم إرسال التنبيه بنجاح!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # تشغيل السيرفر على البورت المطلوب
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
