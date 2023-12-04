import json
import psycopg2
from psycopg2.extras import RealDictCursor
from decimal import Decimal
from datetime import date

# Custom JSON Encoder to handle Decimal and date serialization
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        elif isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)

# Connect to the database
conn = psycopg2.connect(
    dbname="db_lab3",
    user="sonia",
    password="123",
    host="localhost"
)

# Use RealDictCursor to get rows as dictionaries
cursor = conn.cursor(cursor_factory=RealDictCursor)

# Export financials table
cursor.execute("SELECT * FROM financials")
financials_data = cursor.fetchall()

# Export rating table
cursor.execute("SELECT * FROM rating")
rating_data = cursor.fetchall()

# Export movie table
cursor.execute("SELECT * FROM movie")
movie_data = cursor.fetchall()

# Close the cursor and connection
cursor.close()
conn.close()

# Create a dictionary to store the data
data_dict = {
    "financials": financials_data,
    "rating": rating_data,
    "movie": movie_data
}

# Write the dictionary to a JSON file using the custom encoder
with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data_dict, json_file, ensure_ascii=False, indent=2, cls=CustomEncoder)
