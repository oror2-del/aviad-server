import requests
import json
import time

VERCEL_URL = "https://tips365-ipnb.vercel.app/api/update"

def get_smart_tips():
    # סימולציה של האלגוריתם שמוצא מספר טפסים לכל קטגוריה
    all_tips = [
        {"cat": "nba", "m": "פיניקס - דנבר", "p": "דנבר -2.5", "o": "1.85", "s": "45₪", "r": "9.2"},
        {"cat": "nba", "m": "לייקרס - גולדן סטייט", "p": "אובר 220.5", "o": "1.90", "s": "30₪", "r": "8.8"},
        {"cat": "math", "m": "מנצ'סטר סיטי - ארסנל", "p": "סיטי מנצחת", "o": "1.72", "s": "60₪", "r": "9.8"},
        {"cat": "league", "m": "ריאל מדריד - סוסיאדד", "p": "מעל 2.5 שערים", "o": "1.65", "s": "35₪", "r": "8.5"},
        {"cat": "league", "m": "ליברפול - אברטון", "p": "ליברפול מעל 1.5", "o": "1.55", "s": "40₪", "r": "8.2"}
    ]
    return all_tips

def run():
    data = get_smart_tips()
    try:
        requests.post(VERCEL_URL, json={"tips": data}, timeout=15)
        print("✅ האתר עודכן עם כל הטפסים החדשים.")
    except:
        print("❌ שגיאת תקשורת")

if __name__ == "__main__":
    while True:
        run()
        time.sleep(300)
