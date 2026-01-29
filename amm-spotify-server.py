import time
from flask import Flask, jsonify, request, abort
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = 'redirect_ui”

# esp32 specialized api key to access api
API_KEY = ""  

# interval between pings to Spotify’s API
POLL_INTERVAL = 

# localhost port this “server” will run on
PORT = 

app = Flask(__name__)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="user-read-playback-state",
        cache_path=".spotify_cache",
        open_browser=True
    )
)

sp.current_playback()

state = {
    "title": None,
    "artist": None,
    "playing": False,
    "image": None,
    "updated": 0
}

def pick_image(images):
    """
    Prefer ~300x300 image, otherwise first available.
    """
    if not images:
        return None

    for img in images:
        if img.get("width") == 300:
            return img.get("url")

    return images[0].get("url")

def poll_spotify():
    global state
    while True:
        try:
            playback = sp.current_playback()

            if playback is None or playback.get("item") is None:
                state.update({
                    "title": None,
                    "artist": None,
                    "playing": False,
                    "image": None,
                    "updated": int(time.time())
                })
            else:
                item = playback["item"]
                album = item.get("album", {})
                images = album.get("images", [])

                state.update({
                    "title": item.get("name"),
                    "artist": ", ".join(a["name"] for a in item.get("artists", [])),
                    "playing": playback.get("is_playing", False),
                    "image": pick_image(images),
                    "updated": int(time.time())
                })
	
	# exception handling
        except Exception as e:
            print("Spotify error:", e)

        time.sleep(POLL_INTERVAL)

@app.route("/now-playing")
def now_playing():
    if request.args.get("k") != API_KEY:
        abort(403)

    return jsonify(state)

if __name__ == "__main__":
    import threading
    threading.Thread(target=poll_spotify, daemon=True).start()
	# localhost ip this “server” runs on
    app.run(host="127.0.0.1", port=PORT)
