import requests
import time

VERCEL_URL = "https://tips365-ipnb.vercel.app/api/update"

def get_smart_tips():
    return [
        {"cat": "nba", "m": "פיניקס - דנבר", "p": "דנבר -2.5", "o": "1.85", "s": "45₪", "r": "9.2"},
        {"cat": "math", "m": "מנצ'סטר סיטי - ארסנל", "p": "סיטי מנצחת", "o": "1.72", "s": "60₪", "r": "9.8"},
        {"cat": "league", "m": "ריאל מדריד - ברצלונה", "p": "שתי הקבוצות יבקיעו", "o": "1.65", "s": "40₪", "r": "8.5"}
    ]

def run():
    while True:
        try:
            requests.post(VERCEL_URL, json={"tips": get_smart_tips()}, timeout=15)
            print("✅ האתר עודכן")
        except:
            print("❌ שגיאה")
        time.sleep(300)

if __name__ == "__main__":
    run()
