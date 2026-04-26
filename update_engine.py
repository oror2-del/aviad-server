import os
from datetime import datetime

# נתונים לדוגמה (כאן המערכת תכניס את הנתונים החדשים בעתיד)
today_date = datetime.now().strftime("%d/%m/%Y")
new_football = "הדוח התעדכן אוטומטית"
new_nba = "ממתין לנתוני ערב"

file_path = 'index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. העברת התוכן הישן לארכיון (לפני שמעדכנים)
# אנחנו מחפשים את המקום שבו הארכיון מתחיל
archive_marker = '<div class="card" id="archive-list">'
if archive_marker in content:
    # כאן אנחנו יוצרים שורה חדשה לארכיון עם התאריך של היום
    archive_entry = f'<div class="archive-item">{today_date}: דוח יומי בוצע</div>\n'
    content = content.replace(archive_marker, archive_marker + '\n' + archive_entry)

# 2. עדכון התחזית ב"שידור חי"
# (כאן אפשר להוסיף לוגיקה שתחליף את הטקסט של המשחקים)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Archive updated successfully!")
