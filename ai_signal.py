from tradingview_ta import TA_Handler, Interval

def generate_signal():
    try:
        handler = TA_Handler(
            symbol="XAUUSD",
            screener="forex",
            exchange="OANDA",  # يمكنك تجربته أيضاً: FX_IDC أو FOREXCOM
            interval=Interval.INTERVAL_5_MINUTES
        )

        analysis = handler.get_analysis()
        recommendation = analysis.summary["RECOMMENDATION"]

        if recommendation in ["STRONG_BUY", "BUY"]:
            return "BUY"
        elif recommendation in ["STRONG_SELL", "SELL"]:
            return "SELL"
        else:
            return None

    except Exception as e:
        return f"خطأ في التحليل: {str(e)}"
