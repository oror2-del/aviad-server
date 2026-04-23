import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get-odds')
def get_odds():
    # כאן אנחנו מגדירים את היחסים שימשכו מהשרת
    # בשלב הבא נחבר את זה לסורק האוטומטי של Bet365
    live_odds = [1.85, 2.10, 1.90, 1.55] 
    return jsonify({"success": True, "odds": live_odds})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
