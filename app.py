from flask import Flask, jsonify
import requests
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

def fetch_social_media_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return len(data)
    except Exception:
        return 0 

@app.route("/social_network_activity")
def social_network_activity():
    social_media_urls = {
        "twitter": "https://takehome.io/twitter",
        "facebook": "https://takehome.io/facebook",
        "instagram": "https://takehome.io/instagram"
    }

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(fetch_social_media_data, social_media_urls.values()))

    json_response = dict(zip(social_media_urls.keys(), results))
    return jsonify(json_response)

if __name__ == "__main__":
    app.run(debug=True)
