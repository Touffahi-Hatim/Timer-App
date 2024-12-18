from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/countdown', methods=['POST'])
def countdown():
    # Extract the JSON data from the request
    data = request.json
    minutes = int(data.get('minutes', 0))
    secondes = minutes * 60
    result = []

    # Perform the countdown
    while secondes:
        mins, secs = divmod(secondes, 60)
        timer = f'{mins:02d}:{secs:02d}'
        result.append(timer)
        time.sleep(1)  # Blocking function, works server-side
        secondes -= 1

    result.append("Compte à rebours terminé!")
    return jsonify({"output": result})

@app.route('/')
def index():
    return open("py.html").read()

if __name__ == '__main__':
    app.run(debug=True)
