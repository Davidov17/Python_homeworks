import sqlite3
import pandas as pd

# Load database
conn = sqlite3.connect("chinook.db")

customers = pd.read_sql("SELECT CustomerId, FirstName, LastName FROM customers", conn)
invoices = pd.read_sql("SELECT InvoiceId, CustomerId FROM invoices", conn)

conn.close()

# Inner join
merged = customers.merge(invoices, on="CustomerId", how="inner")

# Count invoices per customer
invoice_counts = (
    merged
    .groupby(["CustomerId", "FirstName", "LastName"])
    .size()
    .reset_index(name="Total_Invoices")
)

invoice_counts.head()
movies = pd.read_csv("movie.csv")

df1 = movies[["director_name", "color"]]
df2 = movies[["director_name", "num_critic_for_reviews"]]

# Left join
left_join = df1.merge(df2, on="director_name", how="left")

# Full outer join
outer_join = df1.merge(df2, on="director_name", how="outer")

# Row counts
left_count = left_join.shape[0]
outer_count = outer_join.shape[0]

left_count, outer_count
titanic = pd.read_csv("titanic.csv")

titanic_grouped = (
    titanic
    .groupby("Pclass")
    .agg(
        Average_Age=("Age", "mean"),
        Total_Fare=("Fare", "sum"),
        Passenger_Count=("PassengerId", "count")
    )
    .reset_index()
)

titanic_grouped

movie_grouped = (
    movies
    .groupby(["color", "director_name"])
    .agg(
        Total_Critic_Reviews=("num_critic_for_reviews", "sum"),
        Avg_Duration=("duration", "mean")
    )
    .reset_index()
)

movie_grouped.head()

flights = pd.read_csv("flights.csv")

flights_grouped = (
    flights
    .groupby(["Year", "Month"])
    .agg(
        Total_Flights=("FlightNum", "count"),
        Avg_ArrDelay=("ArrDelay", "mean"),
        Max_DepDelay=("DepDelay", "max")
    )
    .reset_index()
)

flights_grouped.head()


def age_classifier(age):
    if pd.isna(age):
        return None
    return "Child" if age < 18 else "Adult"

titanic["Age_Group"] = titanic["Age"].apply(age_classifier)

titanic[["Age", "Age_Group"]].head()
employees = pd.read_csv("employee.csv")

employees["Normalized_Salary"] = (
    employees
    .groupby("Department")["Salary"]
    .transform(lambda x: (x - x.mean()) / x.std())
)

employees.head()
def duration_category(duration):
    if duration < 60:
        return "Short"
    elif duration <= 120:
        return "Medium"
    else:
        return "Long"

movies["Duration_Type"] = movies["duration"].apply(duration_category)

movies[["duration", "Duration_Type"]].head()
titanic_pipeline = (
    titanic
    .pipe(lambda df: df[df["Survived"] == 1])
    .pipe(lambda df: df.assign(Age=df["Age"].fillna(df["Age"].mean())))
    .pipe(lambda df: df.assign(Fare_Per_Age=df["Fare"] / df["Age"]))
)

titanic_pipeline.head()
flights_pipeline = (
    flights
    .pipe(lambda df: df[df["DepDelay"] > 30])
    .pipe(lambda df: df.assign(
        Delay_Per_Hour=df["DepDelay"] / (df["AirTime"] / 60)
    ))
)

flights_pipeline.head()
