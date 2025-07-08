from ai_signal import generate_signal
import time

def main():
    signal = generate_signal()
    
    print("✅ التوصية الحالية:", signal)
    
    if signal == "BUY":
        print("📈 توصية شراء مؤكدة للذهب.")
    elif signal == "SELL":
        print("📉 توصية بيع مؤكدة للذهب.")
    elif signal is None:
        print("❌ لا توجد توصية مؤكدة حالياً.")
    elif "خطأ" in signal:
        print("⚠️", signal)

if __name__ == "__main__":
    main()
