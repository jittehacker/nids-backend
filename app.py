from flask import Flask, request, jsonify
import requests
import os

from flask_cors import CORS
app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("API_KEY")
DEPLOYMENT_URL = os.getenv("DEPLOYMENT_URL")


def get_ibm_token():
    response = requests.post(
        "https://iam.cloud.ibm.com/identity/token",
        data={"apikey": API_KEY, "grant_type": "urn:ibm:params:oauth:grant-type:apikey"},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    return response.json()["access_token"]

@app.route("/predict", methods=["POST"])
def predict():
    try:
        token = get_ibm_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        payload = request.get_json()
        ibm_response = requests.post(DEPLOYMENT_URL, json=payload, headers=headers)
        return jsonify(ibm_response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return "🔐 NIDS Backend is Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
