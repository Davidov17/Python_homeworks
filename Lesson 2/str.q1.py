name = str(input("What is your name? "))
year_of_birth = int(input("What is your year of birth? "))
from datetime import date
today = date.today()
print("Your age is: ", today.year-year_of_birth)
