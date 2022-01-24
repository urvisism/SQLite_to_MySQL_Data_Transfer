import sqlite3
import mysql.connector
import time

start_time = time.time()

conn = sqlite3.connect('music.sqlite')

mysql_db = mysql.connector.connect(host='localhost', user='root', password='123456', database='music')
mysql_cursor = mysql_db.cursor()

mysql_cursor.execute("CREATE TABLE IF NOT EXISTS albums (_id int PRIMARY KEY NOT NULL, name VARCHAR(255) NOT NULL,"
                     "artist int NOT NULL)")
mysql_cursor.execute("CREATE TABLE IF NOT EXISTS artists (_id int PRIMARY KEY NOT NULL, name VARCHAR(255) NOT NULL)")
mysql_cursor.execute("CREATE TABLE IF NOT EXISTS songs (_id int PRIMARY KEY NOT NULL, track int NOT NULL,"
                     "title VARCHAR(255) NOT NULL, album int NOT NULL)")

mysql_cursor.execute("TRUNCATE TABLE albums")
mysql_cursor.execute("TRUNCATE TABLE artists")
mysql_cursor.execute("TRUNCATE TABLE songs")

for _id, name, artist in conn.execute("SELECT * FROM albums"):
    mysql_cursor.execute("INSERT INTO albums VALUES (%s, %s, %s)", (_id, name, artist))
    mysql_db.commit()

for _id, name in conn.execute("SELECT * FROM artists"):
    mysql_cursor.execute("INSERT INTO artists VALUES (%s, %s)", (_id, name))
    mysql_db.commit()

for _id, track, title, album in conn.execute("SELECT * FROM songs"):
    mysql_cursor.execute("INSERT INTO songs VALUES (%s, %s, %s, %s)", (_id, track, title, album))
    mysql_db.commit()

mysql_db.close()
conn.close()

end_time = time.time()
total_time = end_time - start_time
print(f"{total_time} Sec, {total_time/60} Min")