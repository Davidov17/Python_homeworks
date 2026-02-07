from bs4 import BeautifulSoup

# 1. Load and parse the HTML file
with open("weather.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Find table rows
rows = soup.select("tbody tr")

weather_data = []

# Extract day, temperature, condition
for row in rows:
    day = row.find_all("td")[0].text.strip()
    temp_text = row.find_all("td")[1].text.strip()
    condition = row.find_all("td")[2].text.strip()

    # Parse numeric temperature
    temp = int(temp_text.replace("°C", ""))

    weather_data.append({
        "day": day,
        "temp": temp,
        "condition": condition
    })

# 2. Display weather data
print("Weather Forecast:")
for w in weather_data:
    print(f"{w['day']}: {w['temp']}°C — {w['condition']}")

# 3. Find highest temp and sunny days
max_temp = max(w["temp"] for w in weather_data)
hottest_days = [w["day"] for w in weather_data if w["temp"] == max_temp]
sunny_days = [w["day"] for w in weather_data if w["condition"] == "Sunny"]

print("\nHighest Temperature:")
print(f"{max_temp}°C on {', '.join(hottest_days)}")

print("\nSunny Condition Days:")
print(", ".join(sunny_days))

# 4. Compute average temperature
avg_temp = sum(w["temp"] for w in weather_data) / len(weather_data)
print(f"\nAverage Temperature: {avg_temp:.2f}°C")

import sqlite3, requests, csv
from bs4 import BeautifulSoup

DB_FILE = "jobs.db"
URL = "https://realpython.github.io/fake-jobs/"

# ----------------------
# Database Setup
# ----------------------
conn = sqlite3.connect(DB_FILE)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS jobs(
    id INTEGER PRIMARY KEY,
    title TEXT,
    company TEXT,
    location TEXT,
    description TEXT,
    link TEXT,
    UNIQUE(title, company, location)
)
""")
conn.commit()

# ----------------------
# Scrape Fake Jobs
# ----------------------
resp = requests.get(URL)
soup = BeautifulSoup(resp.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

for job in jobs:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    desc = job.find("p", class_="description").text.strip()
    link = job.find("a")["href"]

    # Check if exists
    cur.execute("""
    SELECT id, description, link
    FROM jobs
    WHERE title=? AND company=? AND location=?
    """, (title, company, location))
    result = cur.fetchone()

    if result:
        # Update if changed
        job_id, old_desc, old_link = result
        if desc != old_desc or link != old_link:
            cur.execute("""
            UPDATE jobs
            SET description=?, link=?
            WHERE id=?
            """, (desc, link, job_id))
            print(f"Updated: {title} at {company}")
    else:
        # Insert new
        cur.execute("""
        INSERT INTO jobs(title, company, location, description, link)
        VALUES (?, ?, ?, ?, ?)
        """, (title, company, location, desc, link))
        print(f"Inserted: {title} at {company}")

conn.commit()

# ----------------------
# Filtering & CSV Export
# ----------------------

def export_filtered_to_csv(location=None, company=None, filename="jobs_export.csv"):
    query = "SELECT title, company, location, description, link FROM jobs WHERE 1=1"
    params = []

    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")
    if company:
        query += " AND company LIKE ?"
        params.append(f"%{company}%")

    cur.execute(query, params)
    rows = cur.fetchall()

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Job Title", "Company", "Location", "Description", "Link"])
        writer.writerows(rows)

    print(f"Exported {len(rows)} jobs to {filename}")

# Example call:
# export_filtered_to_csv(location="New York", company="Company")