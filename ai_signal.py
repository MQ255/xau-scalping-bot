from tradingview_ta import TA_Handler, Interval

def generate_signal():
    try:
        handler = TA_Handler(
            symbol="XAUUSD",
            screener="forex",
            exchange="FX_IDC",
            interval=Interval.INTERVAL_5_MINUTES
        )
        analysis = handler.get_analysis()
        recommendation = analysis.summary["RECOMMENDATION"]
        current_price = analysis.indicators["close"]
        
        if recommendation in ["BUY", "SELL"]:
            tp1 = round(current_price + (60 if recommendation == "BUY" else -60), 2)
            tp2 = round(current_price + (120 if recommendation == "BUY" else -120), 2)
            tp3 = round(current_price + (180 if recommendation == "BUY" else -180), 2)
            sl = round(current_price - (20 if recommendation == "BUY" else -20), 2)

            return (
                f"🚨 توصية سكالبينغ ({recommendation})\\n"
                f"الرمز: XAUUSD\\n"
                f"السعر الحالي: {current_price}\\n"
                f"الهدف 1️⃣: {tp1}\\n"
                f"الهدف 2️⃣: {tp2}\\n"
                f"الهدف 3️⃣: {tp3}\\n"
                f"وقف الخسارة: {sl}"
            )
        else:
            return None
    except Exception as e:
        print("خطأ في التحليل:", e)
        return None
