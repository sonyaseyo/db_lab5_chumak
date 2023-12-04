import json
import psycopg2
from psycopg2.extras import RealDictCursor
from decimal import Decimal
from datetime import date

# для уникнення помилок з типом даних date, decimal) у джсон
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        elif isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)

# з'єднання з базою даних
conn = psycopg2.connect(
    dbname="db_lab3",
    user="sonia",
    password="123",
    host="localhost"
)

# зчитуємо рядки як словники
cursor = conn.cursor(cursor_factory=RealDictCursor)

# експорт таблиці фінансування
cursor.execute("SELECT * FROM financials")
financials_data = cursor.fetchall()

# експорт таблиці рейтингів
cursor.execute("SELECT * FROM rating")
rating_data = cursor.fetchall()

# експорт таблиці фільмів
cursor.execute("SELECT * FROM movie")
movie_data = cursor.fetchall()

# закриваємо з'єднання
cursor.close()
conn.close()

# створення словника для зберігання даних
data_dict = {
    "financials": financials_data,
    "rating": rating_data,
    "movie": movie_data
}

# записуємо словник в джсон файл + використовуємо ф-цію з кастомними типами даних 
with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data_dict, json_file, ensure_ascii=False, indent=2, cls=CustomEncoder)
