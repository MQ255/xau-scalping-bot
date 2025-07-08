import requests

bot_token = "8067398934:AAGvw2oAS-0Y5zgDD-1QUI8EbZppWJIb_NQ"
chat_id = "5956821181"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=data)
    if response.status_code != 200:
        print("فشل في إرسال الرسالة إلى Telegram")
