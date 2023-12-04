import csv
import psycopg2

# з'єднання з базою даних
conn = psycopg2.connect(
    dbname="db_lab3",
    user="sonia",
    password="123",
    host="localhost"
)

cursor = conn.cursor()

# експорт таблиці фінансування
cursor.execute("SELECT * FROM financials")
financials_data = cursor.fetchall()

with open('financials.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['financials_id', 'total_gross', 'inflation_adjusted_gross'])
    csv_writer.writerows(financials_data)

# експорт таблиці рейтингів
cursor.execute("SELECT * FROM rating")
rating_data = cursor.fetchall()

with open('rating.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['rating_id', 'mpaa_rating'])
    csv_writer.writerows(rating_data)

# експорт таблиці фільмів
cursor.execute("SELECT * FROM movie")
movie_data = cursor.fetchall()

with open('movie.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['movie_id', 'title', 'release_date', 'genre', 'financials_id', 'rating_id'])
    csv_writer.writerows(movie_data)

# закриваємо з'єднання
cursor.close()
conn.close()
