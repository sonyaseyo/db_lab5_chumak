import psycopg2
import matplotlib.pyplot as plt

# параметри для з'єднання з сервером
db_params = {
    'host': 'localhost',
    'database': 'db_lab3',
    'user': 'sonia',
    'password': '123'
}

# функція з sql запитами
def execute_query(query):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()
    cursor.execute(query)

    # For SELECT queries, fetch the data
    if query.strip().upper().startswith('SELECT'):
        result = cursor.fetchall()
    else:
        result = None

    conn.commit()
    conn.close()
    return result

# запит A: дохід для кожного фільму
query_a = """
    DROP VIEW IF EXISTS MovieFinancialsView;
    CREATE VIEW MovieFinancialsView AS
    SELECT movie.movie_id, movie.title, financials.total_gross
    FROM movie
    JOIN financials ON movie.financials_id = financials.financials_id;
"""

# Execute the CREATE VIEW query
execute_query(query_a)

# стовпчикова діаграма до запиту А
bar_data = execute_query("SELECT * FROM MovieFinancialsView;")
bar_labels = [item[1] for item in bar_data]
bar_values = [item[2] for item in bar_data]

plt.bar(bar_labels, bar_values)
plt.xlabel('Movie Title')
plt.ylabel('Total Gross')
plt.title('Total Gross Income for Each Movie')
plt.xticks(rotation=90, ha='right', fontsize=6)
plt.show()


# запит B: розподіл фільмів по жанрах
query_b = """
    DROP VIEW IF EXISTS GenreCountView;
    CREATE VIEW GenreCountView AS
    SELECT genre, COUNT(*) as count
    FROM movie
    GROUP BY genre;
"""

pie_chart_data = execute_query(query_b)


# Кругова діаграма до запиту B
pie_data = execute_query("SELECT * FROM GenreCountView;")
pie_labels = [item[0] for item in pie_data]
pie_counts = [item[1] for item in pie_data]

plt.pie(pie_counts, labels=pie_labels, autopct='%1.1f%%')
plt.title('Distribution of Movies by Genre')
plt.show()


# запит C: Фільми та їх рейтинг
query_c = """
    DROP VIEW IF EXISTS MovieRatingView;
    CREATE VIEW MovieRatingView AS
    SELECT movie.title, rating.mpaa_rating
    FROM movie
    JOIN rating ON movie.rating_id = rating.rating_id;
"""

dependencies_data = execute_query(query_c)


# Графік залежності до запиту С
dependency_data = execute_query("SELECT * FROM MovieRatingView;")
dependency_labels = [item[0] for item in dependency_data]
dependency_ratings = [item[1] for item in dependency_data]

plt.scatter(dependency_labels, dependency_ratings)
# закоментувала з'єднання точок тому що через завелику кількість фільмів негарне з'єднання :(
# plt.plot(dependency_labels, dependency_ratings, linestyle='-', color='gray', alpha=0.5)  # Connect the dots with lines
plt.xlabel('Movie Title')
plt.ylabel('MPAA Rating')
plt.title('Movies and Their MPAA Ratings')
plt.xticks(rotation=90, ha='right', fontsize=6)
plt.show()
