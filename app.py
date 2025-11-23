from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SECRET_WORD = "abcd1234"  #add secret

@app.route("/quiz", methods=["POST"])
def quiz():
    try:
        data = request.get_json()
    except:
        return jsonify({"error": "Invalid JSON"}), 400

    # 1. Check secret
    if data.get("secret") != SECRET_WORD:
        return jsonify({"error": "Forbidden"}), 403

    # 2. Checking  payload
    if "url" not in data:
        return jsonify({"error": "URL missing"}), 400

    # 3. Basic response
    return jsonify({"status": "ok", "message": "Secret verified"}), 200

if __name__ == "__main__":
    app.run(debug=True)
