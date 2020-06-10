# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS times"

# CREATE TABLES

songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays
(songplay_id SERIAL PRIMARY KEY, start_time bigint, user_id int, level varchar, 
song_id varchar, artist_id varchar, session_id int, location varchar, user_agent varchar);
""")

user_table_create = (""" CREATE TABLE IF NOT EXISTS users
(user_id int, first_name varchar, last_name varchar, gender varchar, level varchar);
""")

song_table_create = (""" CREATE TABLE IF NOT EXISTS songs
(song_id varchar, title varchar, artist_id varchar, year int, duration numeric);
""")

artist_table_create = (""" CREATE TABLE IF NOT EXISTS artists
(artist_id varchar, artist_name varchar, artist_location varchar, artist_latitude float(5), artist_longitude float(5));
""")

time_table_create = (""" CREATE TABLE IF NOT EXISTS time
(start_time bigint, hour int, day int, week int, month int, year int, weekday int);
""")

# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = (""" INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s);
""")

song_table_insert = (""" INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s);
""")

artist_table_insert = (""" INSERT INTO artists (artist_id, artist_name, artist_location, artist_latitude, artist_longitude) VALUES (%s, %s, %s, %s, %s);
""")

time_table_insert = (""" INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = (""" select song_id, a.artist_id from songs a, artists b where a.artist_id = b.artist_id and title = %s and 
artist_name = %s and duration = %s """)


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]