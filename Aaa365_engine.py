import requests
import time

# הגדרות המערכת
VERCEL_URL = "https://tips365-ipnb.vercel.app/api/update" # הכתובת של האתר שלך
MIN_SCORE = 8.0 # סף כניסה לאתר

def fetch_all_sports_data():
    """סריקת משחקי כדורגל, NBA, טניס וכדור יד"""
    print("🔄 מריץ סריקה גלובלית על כל תחומי הספורט...")
    # כאן המערכת מתחברת למקורות הנתונים (API)
    # נדמה כאן שליפת נתונים לדוגמה
    return [
        {"match": "Real Madrid vs Bayern", "sport": "Football", "score": 9.2, "pick": "1"},
        {"match": "Lakers vs Denver", "sport": "NBA", "score": 8.5, "pick": "Over 210.5"},
        {"match": "Djokovic vs Alcaraz", "sport": "Tennis", "score": 8.1, "pick": "1"}
    ]

def build_slips(matches):
    """בניית 3 הטפסים לפי אסטרטגיית Aaa365"""
    high_value = [m for m in matches if m['score'] >= MIN_SCORE]
    
    if len(high_value) >= 2:
        return {
            "anchor": high_value[:2],
            "system": high_value[:4],
            "combo": high_value[:4],
            "timestamp": time.strftime("%H:%M:%S")
        }
    return None

def update_website(data):
    """שליחת הנתונים ישירות לאתר ב-Vercel"""
    try:
        response = requests.post(VERCEL_URL, json=data)
        if response.status_code == 200:
            print("✅ האתר עודכן בהצלחה!")
    except:
        print("❌ שגיאה בעדכון האתר - וודא שהאתר באוויר")

# הרצה בלופ אינסופי 24/7
while True:
    all_data = fetch_all_sports_data()
    aaa365_slips = build_slips(all_data)
    
    if aaa365_slips:
        update_website(aaa365_slips)
    
    print("💤 ממתין 10 דקות לסריקה הבאה...")
    time.sleep(600) # סריקה כל 10 דקות
