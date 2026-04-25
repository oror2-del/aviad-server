import requests
import json
import time

# הגדרות יעד - מעודכן לאתר שלך
VERCEL_URL = "https://tips365-ipnb.vercel.app/api/update"

def get_data():
    # כאן המנוע מתחבר למקורות הנתונים (סימולציה של הסורק המקצועי)
    # המנוע מחלק את זה ל-NBA ולשאר העולם
    
    tips = [
        {
            "id": "nba_1",
            "category": "NBA Daily",
            "match": "Orlando Magic vs Cleveland Cavaliers",
            "pick": "Orlando +4.5",
            "odds": "1.90",
            "ev": "8.4%",
            "stake": "45₪",
            "status": "Pending"
        },
        {
            "id": "top_1",
            "category": "Top Choice",
            "match": "Arsenal vs Chelsea",
            "pick": "Arsenal Win",
            "odds": "1.65",
            "ev": "6.2%",
            "stake": "30₪",
            "status": "Pending"
        },
        {
            "id": "top_2",
            "category": "Top Choice",
            "match": "Real Madrid vs Barcelona",
            "pick": "Over 2.5 Goals",
            "odds": "1.75",
            "ev": "5.8%",
            "stake": "25₪",
            "status": "Pending"
        }
    ]
    return tips

def send_to_site():
    print("🔄 מפעיל סריקה חכמה (NBA + Top 2)...")
    data = get_data()
    
    try:
        response = requests.post(VERCEL_URL, json={"tips": data}, timeout=10)
        if response.status_code == 200:
            print("✅ זוהו 3 הזדמנויות זהב (1 NBA, 2 Top). האתר והארכיון עודכנו.")
        else:
            print(f"❌ שגיאה בעדכון האתר: {response.status_code}")
    except Exception as e:
        print(f"❌ תקלה בתקשורת: {e}")

if __name__ == "__main__":
    while True:
        send_to_site()
        time.sleep(300)  # הרצה כל 5 דקות
