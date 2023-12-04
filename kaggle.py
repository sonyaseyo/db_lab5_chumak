import csv
import psycopg2

# тут підключаємось до бази даних
conn = psycopg2.connect(
    dbname="db_lab3",
    user="sonia",
    password="123",
    host="localhost"
)

cur = conn.cursor()

# тут шлях до цсв файлу
csv_file_path = r"C:\Users\sofiia\Desktop\disney_movies.csv"

# вичитуємо дані з файлу та вставляємо в таблиці
with open(csv_file_path, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # пропускаємо шапку

    for row in reader:
        try:
            # витягуємо дані з рядку
            movie_title, release_date, genre, mpaa_rating, total_gross, inflation_adjusted_gross = row

            # заповнюємо таблицю з фінансуванням + генеруємо айді
            cur.execute("""
                INSERT INTO financials (total_gross, inflation_adjusted_gross)
                VALUES (%s, %s)
                RETURNING financials_id;
            """, (total_gross, inflation_adjusted_gross))

            financials_id = cur.fetchone()[0]

            # заповнюємо таблицю рейтингів + генеруємо айді
            cur.execute("""
                INSERT INTO rating (mpaa_rating)
                VALUES (%s)
                RETURNING rating_id;
            """, (mpaa_rating,))
            rating_id = cur.fetchone()[0]

            # заповнюємо таблицю фільмів + генеруємо айді
            cur.execute("""
                INSERT INTO movie (title, release_date, genre, financials_id, rating_id)
                VALUES (%s, %s, %s, %s, %s);
            """, (movie_title, release_date, genre, financials_id, rating_id))

            # коммітимо зміни
            conn.commit()
        except Exception as e:
            # це чисто для перевірки, якщо якийсь рядок є помилковим - щоб програма не падала
            print(f"Error inserting row: {row}")
            print(f"Error message: {e}")
            conn.rollback()

# закриваємо з'єднання
cur.close()
conn.close()
