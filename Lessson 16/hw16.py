import pandas as pd
import sqlite3

# 1. sqlite3 (chinook.db)
conn = sqlite3.connect('chinook.db')
df_customers = pd.read_sql_query("SELECT * FROM customers", conn)
print(df_customers.head(10))
conn.close()

# 2. JSON (iris.json)
df_iris = pd.read_json('iris.json')
print(df_iris.shape, df_iris.columns)

# 3. Excel (titanic.xlsx)
df_titanic = pd.read_excel('titanic.xlsx')
print(df_titanic.head())

# 4. Parquet (flights.parquet)
df_flights = pd.read_parquet('flights.parquet')
print(df_flights.info())

# 5. CSV (movie.csv)
df_movie = pd.read_csv('movie.csv')
print(df_movie.sample(10))

# 1. Iris processing
df_iris.columns = [col.lower() for col in df_iris.columns]
iris_subset = df_iris[['sepal_length', 'sepal_width']]

# 2. Titanic processing
titanic_over_30 = df_titanic[df_titanic['Age'] > 30]
gender_counts = df_titanic['Sex'].value_counts()

# 3. Flights processing
flights_subset = df_flights[['origin', 'dest', 'carrier']]
unique_dest_count = df_flights['dest'].nunique()

# 4. Movie processing
long_movies = df_movie[df_movie['duration'] > 120].sort_values(by='director_facebook_likes', ascending=False)

# Iris stats
iris_stats = df_iris.describe().loc[['mean', '50%', 'std']] # 50% bu median

# Titanic age stats
age_min = df_titanic['Age'].min()
age_max = df_titanic['Age'].max()
age_sum = df_titanic['Age'].sum()

# Movie insights
top_director = df_movie.groupby('director_name')['director_facebook_likes'].sum().idxmax()
top_5_longest = df_movie.nlargest(5, 'duration')[['movie_title', 'director_name', 'duration']]

# Flights missing values
missing_vals = df_flights.isnull().sum()
# Misol uchun 'dep_delay' ustunini to'ldirish
df_flights['dep_delay'] = df_flights['dep_delay'].fillna(df_flights['dep_delay'].mean())
