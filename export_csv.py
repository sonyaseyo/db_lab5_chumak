import csv
import psycopg2

# Connect to the database
conn = psycopg2.connect(
    dbname="db_lab3",
    user="sonia",
    password="123",
    host="localhost"
)

cursor = conn.cursor()

# Export financials table
cursor.execute("SELECT * FROM financials")
financials_data = cursor.fetchall()

with open('financials.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['financials_id', 'total_gross', 'inflation_adjusted_gross'])
    csv_writer.writerows(financials_data)

# Export rating table
cursor.execute("SELECT * FROM rating")
rating_data = cursor.fetchall()

with open('rating.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['rating_id', 'mpaa_rating'])
    csv_writer.writerows(rating_data)

# Export movie table
cursor.execute("SELECT * FROM movie")
movie_data = cursor.fetchall()

with open('movie.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['movie_id', 'title', 'release_date', 'genre', 'financials_id', 'rating_id'])
    csv_writer.writerows(movie_data)

# Close the cursor and connection
cursor.close()
conn.close()
