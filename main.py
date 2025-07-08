import time
from ai_signal import generate_signal
from send_telegram import send_telegram_message

while True:
    try:
        signal = generate_signal()
        if signal:
            send_telegram_message(signal)
        else:
            print("❌ لا توجد توصية مؤكدة حالياً.")
    except Exception as e:
        print("حدث خطأ:", e)

    time.sleep(300)  # كل 5 دقائق
