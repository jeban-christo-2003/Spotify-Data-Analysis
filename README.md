📊 Spotify Data Analysis
This project collects your recently played tracks from the Spotify Web API and stores them in a MySQL database for analysis.

🚀 Features
Connects securely to Spotify using OAuth 2.0

Fetches recently played tracks (user-read-recently-played)

Stores track metadata (track name, artist name, played time) in MySQL

Prevents duplicate entries using primary keys

Ready for data analysis using SQL or Python

🛠️ Technologies Used
Python 3.11+

Spotipy - Python client for Spotify Web API

MySQL (local or remote)

python-dotenv for environment variable management

📁 Project Structure
graphql
Copy
Edit
spotify_data_Analysis/
│
├── spotify_analysis.py       # Main script to fetch and store data
├── schema.sql                # SQL file to create the required table
├── .env                      # Stores API and DB credentials (not committed)
├── requirements.txt          # List of Python dependencies
└── README.md                 # Project documentation
✅ Setup Instructions
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/spotify_data_Analysis.git
cd spotify_data_Analysis
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Create a .env file
Create a .env file in the root folder and add:

env
Copy
Edit
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
SPOTIFY_REDIRECT_URI=http://127.0.0.1:8080

MYSQL_HOST=localhost
MYSQL_USER=your_mysql_username
MYSQL_PASSWORD=your_mysql_password
MYSQL_DATABASE=spotify_data
⚠️ Never commit your .env file to GitHub.

4. Set up your MySQL database
Run the schema.sql file in your MySQL server:

sql
Copy
Edit
CREATE DATABASE IF NOT EXISTS spotify_data;

USE spotify_data;

CREATE TABLE IF NOT EXISTS recently_played (
    track_id VARCHAR(100) PRIMARY KEY,
    track_name VARCHAR(255),
    artist_name VARCHAR(255),
    played_at DATETIME
);
▶️ Run the Script
bash
Copy
Edit
python spotify_analysis.py
You will be prompted to log in via Spotify (only on the first run). The script will fetch the last 50 played tracks and insert them into your database.

📊 Example Query for Analysis
sql
Copy
Edit
SELECT artist_name, COUNT(DISTINCT track_name) AS unique_tracks
FROM recently_played
GROUP BY artist_name
ORDER BY unique_tracks DESC;
🧪 Future Ideas
Add top tracks & artists (user-top-read scope)

Export data to CSV or Pandas for visualization

Build a Streamlit dashboard or use Tableau/Power BI

Schedule daily updates via cron or Task Scheduler

🤝 Contributing
Feel free to open issues or pull requests! Bug fixes and feature ideas welcome.


