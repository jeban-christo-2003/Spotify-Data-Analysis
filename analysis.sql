
Create database Spotify;
use Spotify;

select * from spotify_analysis;
select count(*) from spotify_analysis;
select track_name,artist_name ,count(artist_name) from spotify_analysis group by track_name,artist_name;
select * from spotify_analysis where artist_name regexp "^[A-Za-z ]+$";
SELECT artist_name, COUNT(DISTINCT track_name) AS unique_tracks, COUNT(*) AS total_plays
FROM spotify_analysis
GROUP BY artist_name;
