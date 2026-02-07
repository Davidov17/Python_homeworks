import sqlite3

# 1. Create / connect to database
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

# 2. Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# 3. Insert data
cursor.executemany("""
INSERT INTO Roster (Name, Species, Age)
VALUES (?, ?, ?)
""", [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])

# 4. Update Jadzia → Ezri
cursor.execute("""
UPDATE Roster
SET Name = ?
WHERE Name = ?
""", ("Ezri Dax", "Jadzia Dax"))

# 5. Query Bajoran characters
print("Bajoran characters:")
cursor.execute("""
SELECT Name, Age FROM Roster
WHERE Species = 'Bajoran'
""")
for row in cursor.fetchall():
    print(row)

# 6. Delete characters older than 100
cursor.execute("""
DELETE FROM Roster
WHERE Age > 100
""")

# 7. Bonus: add Rank column
cursor.execute("""
ALTER TABLE Roster
ADD COLUMN Rank TEXT
""")

# 8. Update ranks
cursor.execute("UPDATE Roster SET Rank='Captain' WHERE Name='Benjamin Sisko'")
cursor.execute("UPDATE Roster SET Rank='Lieutenant' WHERE Name='Ezri Dax'")
cursor.execute("UPDATE Roster SET Rank='Major' WHERE Name='Kira Nerys'")

# 9. Advanced query: sort by age DESC
print("\nRoster sorted by age (DESC):")
cursor.execute("""
SELECT * FROM Roster
ORDER BY Age DESC
""")
import sqlite3

# 1. Create / connect to database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# 2. Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)
""")

# 3. Insert data
cursor.executemany("""
INSERT INTO Books (Title, Author, Year_Published, Genre)
VALUES (?, ?, ?, ?)
""", [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
])

# 4. Update year of 1984
cursor.execute("""
UPDATE Books
SET Year_Published = ?
WHERE Title = ?
""", (1950, "1984"))

# 5. Query dystopian books
print("Dystopian books:")
cursor.execute("""
SELECT Title, Author FROM Books
WHERE Genre = 'Dystopian'
""")
for row in cursor.fetchall():
    print(row)

# 6. Delete books published before 1950
cursor.execute("""
DELETE FROM Books
WHERE Year_Published < 1950
""")

# 7. Bonus: add Rating column
cursor.execute("""
ALTER TABLE Books
ADD COLUMN Rating REAL
""")

# 8. Update ratings
cursor.execute("UPDATE Books SET Rating=4.8 WHERE Title='To Kill a Mockingbird'")
cursor.execute("UPDATE Books SET Rating=4.7 WHERE Title='1984'")
cursor.execute("UPDATE Books SET Rating=4.5 WHERE Title='The Great Gatsby'")

# 9. Advanced query: sort by year ASC
print("\nBooks sorted by year (ASC):")
cursor.execute("""
SELECT * FROM Books
ORDER BY Year_Published ASC
""")
for row in cursor.fetchall():
    print(row)

# Save & close
conn.commit()
conn.close()
for row in cursor.fetchall():
    print(row)

# Save & close
conn.commit()
conn.close()

# Task2
