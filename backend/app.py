import os
from flask import Flask, jsonify, send_from_directory

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FRONTEND = os.path.join(ROOT, "frontend")

app = Flask(__name__, static_folder=FRONTEND, static_url_path="")

# Clearly labelled sample data. Connect a licensed cricket API for real live scores.
MATCHES = [
    {
        "id": 1, "status": "DEMO • COMPLETED", "format": "T20",
        "tournament": "Sample Premier League", "venue": "Demo Cricket Ground",
        "team1": "Hyderabad Hawks", "team2": "Mumbai Mariners",
        "score1": "186/5 (20 ov)", "score2": "179/8 (20 ov)",
        "result": "Hyderabad Hawks won by 7 runs",
        "summary": "A sample match for demonstrating the dashboard."
    },
    {
        "id": 2, "status": "DEMO • UPCOMING", "format": "ODI",
        "tournament": "Sample International Series", "venue": "National Demo Stadium",
        "team1": "India", "team2": "Australia",
        "score1": "—", "score2": "—",
        "result": "Demo fixture • no live score available",
        "summary": "Connect a cricket data provider to show verified fixtures."
    },
    {
        "id": 3, "status": "DEMO • COMPLETED", "format": "TEST",
        "tournament": "Sample Test Championship", "venue": "Central Demo Oval",
        "team1": "England", "team2": "South Africa",
        "score1": "312 & 205", "score2": "280 & 190/6",
        "result": "South Africa won by 4 wickets",
        "summary": "Illustrative score only; not an official historical result."
    }
]

@app.get("/")
def home():
    return send_from_directory(FRONTEND, "index.html")

@app.get("/api/health")
def health():
    return jsonify({"ok": True, "app": "Cricket Analytics Pro"})

@app.get("/api/matches")
def matches():
    return jsonify({
        "data_type": "DEMO DATA — not live or verified match data",
        "matches": MATCHES
    })

@app.get("/api/analysis")
def analysis():
    return jsonify({
        "notice": "Illustrative analysis only. No AI model or live match feed is connected yet.",
        "insights": [
            "Compare powerplay, middle-over and death-over scoring once ball-by-ball data is connected.",
            "Player predictions require verified historical data and a trained model.",
            "Venue and pitch insights require reliable match and ground records."
        ]
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
