from flask import Flask, jsonify
import asyncio
import aiohttp

app = Flask(__name__)

async def fetch_social_media_data(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            data = await response.json()
            return len(data)
    except Exception:
        return 0  # Return 0 in case of any error

async def get_social_media_activity():
    social_media_urls = [
        "https://takehome.io/twitter",
        "https://takehome.io/facebook",
        "https://takehome.io/instagram"
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_social_media_data(session, url) for url in social_media_urls]
        return await asyncio.gather(*tasks)

@app.route("/social_network_activity")
def social_network_activity():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    results = loop.run_until_complete(get_social_media_activity())
    social_media = ["twitter", "facebook", "instagram"]
    json_response = dict(zip(social_media, results))
    return jsonify(json_response)

if __name__ == "__main__":
    app.run(debug=True)

