import requests
import random
import time

# بيانات التليجرام
bot_token = "8067398934:AAGaxKaM0nr85x7YEM6Mu9B7TFuvCDS1h04"
chat_id = "8067398934"  # تأكد أنه هو نفس معرفك أو معرف المجموعة

# سحب السعر الحالي للذهب من Binance
def get_gold_price():
    try:
        url = "https://api.binance.com/api/v3/ticker/price?symbol=XAUUSDT"
        response = requests.get(url)
        data = response.json()
        return float(data['price'])
    except Exception as e:
        print("❌ خطأ في جلب السعر:", e)
        return None

# توليد توصية وهمية (BUY أو SELL) مع تحديد SL و TP
def generate_signal(price):
    direction = random.choice(["BUY", "SELL"])
    entry = price
    sl = round(price - 3 if direction == "BUY" else price + 3, 2)
    tp1 = round(price + 2 if direction == "BUY" else price - 2, 2)
    tp2 = round(price + 4 if direction == "BUY" else price - 4, 2)
    tp3 = round(price + 6 if direction == "BUY" else price - 6, 2)

    signal = f"""
🚀 توصية سكالبينغ على الذهب (XAUUSD)
الاتجاه: {direction}
السعر الحالي: {entry}
وقف الخسارة (SL): {sl}
الاهداف:
🎯 TP1: {tp1}
🎯 TP2: {tp2}
🎯 TP3: {tp3}
"""
    return signal

# إرسال رسالة إلى تليجرام
def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("✅ تم إرسال التوصية!")
    else:
        print("❌ فشل الإرسال:", response.text)

# تنفيذ كل شيء
def main():
    price = get_gold_price()
    if price:
        signal = generate_signal(price)
        send_to_telegram(signal)

if __name__ == "__main__":
    main()
