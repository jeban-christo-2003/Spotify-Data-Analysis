import os
import mysql.connector
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth


load_dotenv()

sp = Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri="http://127.0.0.1:8080/callback",
    scope="user-library-read user-read-recently-played",
    open_browser=True
))


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jeban",
    database="Spotify"
)
cursor = db.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS spotify_analysis(
    song_no INT AUTO_INCREMENT PRIMARY KEY,
    track_id VARCHAR(100) ,
    track_name VARCHAR(255),
    artist_name VARCHAR(255),
    played_at DATETIME
)
""")

# Get recently played tracks
results = sp.current_user_recently_played(limit=50)

for item in results['items']:
    track = item['track']
    track_id = track['id']
    track_name = track['name']
    artist_name = track['artists'][0]['name']
    played_at = item['played_at'].replace('T', ' ').replace('Z', '')  

    try:
        cursor.execute("""
        INSERT INTO spotify_analysis(track_id, track_name, artist_name, played_at)
        VALUES (%s, %s, %s, %s)
       
        """, (track_id, track_name, artist_name, played_at))
        db.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")


cursor.close()
db.close()
print(f"Number of items returned by Spotify API: {len(results['items'])}")
print("Data inserted into MySQL database successfully.")
