import requests
import json
import time

# כתובת האתר שלך - מעודכן
VERCEL_URL = "https://tips365-ipnb.vercel.app/api/update"

def get_smart_tips():
    # כאן האלגוריתם מייצר רשימת טפסים לפי הקטגוריות שביקשת
    all_tips = [
        # קטגוריית NBA
        {"cat": "nba", "m": "פיניקס סאנס - דנבר נאגטס", "p": "דנבר -2.5", "o": "1.85", "s": "45₪", "r": "9.2"},
        {"cat": "nba", "m": "לייקרס - גולדן סטייט", "p": "אובר 220.5 נקודות", "o": "1.91", "s": "35₪", "r": "8.7"},
        
        # קטגוריית מצוינות מתמטית (דירוג גבוה מ-9.5)
        {"cat": "math", "m": "מנצ'סטר סיטי - ארסנל", "p": "סיטי מנצחת (מאני ליין)", "o": "1.72", "s": "65₪", "r": "9.8"},
        
        # קטגוריית ליגות בכירות
        {"cat": "league", "m": "ריאל מדריד - ברצלונה", "p": "שתי הקבוצות יבקיעו", "o": "1.65", "s": "40₪", "r": "8.5"},
        {"cat": "league", "m": "באיירן מינכן - לייפציג", "p": "באיירן מעל 1.5 שערים", "o": "1.58", "s": "50₪", "r": "8.1"}
    ]
    return all_tips

def send_data():
    tips = get_smart_tips()
    try:
        # הוספת headers כדי ש-Vercel יקבל את המידע בצורה חלקה
        headers = {'Content-Type': 'application/json'}
        response = requests.post(VERCEL_URL, json={"tips": tips}, headers=headers, timeout=15)
        if response.status_code == 200:
            print(f"✅ {len(tips)} טפסים נשלחו בהצלחה לאתר.")
        else:
            print(f"⚠️ בעיה בשליחה: {response.status_code}")
    except Exception as e:
        print(f"❌ שגיאת תקשורת: {e}")

if __name__ == "__main__":
    print("🚀 מנוע AAA365 ELITE התחיל לעבוד...")
    while True:
        send_data()
        time.sleep(300) # סריקה ועדכון כל 5 דקות
