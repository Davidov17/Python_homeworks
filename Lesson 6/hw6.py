#%%

#%%
def decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            return "Denominator can't be zero."
    return wrapper

@decorator
def div(a,b):
    return a/b
print(div(0,-1))
#%%
# task1
import os

FILE_NAME = "employees.txt"

def add_employee():
    with open(FILE_NAME, "a") as f:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        f.write(f"{emp_id}, {name}, {position}, {salary}\n")
        print("Employee added successfully!")

def view_employees():
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    with open(FILE_NAME, "r") as f:
        print(f.read())

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    with open(FILE_NAME, "r") as f:
        for line in f:
            if line.startswith(emp_id + ","):
                print(line.strip())
                return
        print("Employee not found.")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    updated = False
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()
    with open(FILE_NAME, "w") as f:
        for line in lines:
            if line.startswith(emp_id + ","):
                print(f"Current record: {line.strip()}")
                name = input("Enter new Name: ")
                position = input("Enter new Position: ")
                salary = input("Enter new Salary: ")
                f.write(f"{emp_id}, {name}, {position}, {salary}\n")
                updated = True
            else:
                f.write(line)
    if updated:
        print("Employee record updated.")
    else:
        print("Employee not found.")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return
    deleted = False
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()
    with open(FILE_NAME, "w") as f:
        for line in lines:
            if line.startswith(emp_id + ","):
                deleted = True
                continue
            f.write(line)
    if deleted:
        print("Employee deleted.")
    else:
        print("Employee not found.")

def main_menu():
    while True:
        print("\n--- Employee Records Manager ---")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

main_menu()

#%%
# task2
import os
import string
from collections import Counter

FILE_NAME = "sample.txt"
REPORT_FILE = "word_count_report.txt"

# Create sample file if it doesn't exist
if not os.path.exists(FILE_NAME):
    text = input("sample.txt not found. Enter some text to create it:\n")
    with open(FILE_NAME, "w") as f:
        f.write(text)

# Read file and process words
with open(FILE_NAME, "r") as f:
    text = f.read().lower()  # ignore case
    # Remove punctuation
    for p in string.punctuation:
        text = text.replace(p, "")
    words = text.split()

# Count frequency
word_count = Counter(words)
total_words = len(words)

# Ask user for top N words
top_n = int(input("How many top words do you want to see? "))
top_words = word_count.most_common(top_n)

# Display results
print(f"\nTotal words: {total_words}")
print(f"Top {top_n} most common words:")
for word, count in top_words:
    print(f"{word} - {count} times")

# Save to report
with open(REPORT_FILE, "w") as f:
    f.write("Word Count Report\n")
    f.write(f"Total Words: {total_words}\n")
    f.write(f"Top {top_n} Words:\n")
    for word, count in top_words:
        f.write(f"{word} - {count}\n")

print(f"\nReport saved to {REPORT_FILE}")
