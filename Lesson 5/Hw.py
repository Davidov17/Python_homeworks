#%%
import numbers
import statistics


def convert_cel_to_faren(cel):
    return cel*9/5+32
print(f"{convert_cel_to_faren(int(input("Enter a celsius "))):.2f}")
def convert_faren_to_cel(faren):
    return faren*9/5+32
print(f"{convert_faren_to_cel(int(input("Enter a faren "))):.2f}")

#%%
# Task2
def invest(principal, rate, years):
    for i in range (1,years+1):
        print("Year ",i, ":", f"{principal*(1+rate)**i:.2f}")

invest(100,0.05,4)
#%%
# Task3
number = int(input("Enter a number: "))
def factor(number):
    for i in range (1, number+1):
        if number % i == 0:
            print(i, "is a factor of", number)
factor(number)

#%%
python_universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
def _enrollment_stats(python_universities):
    enrollments = []
    tuitions = []
    for university in python_universities:
        enrollments.append(university[1])
        tuitions.append(university[2])
    return enrollments, tuitions
enrolments, tuitions = _enrollment_stats(python_universities)
print("Total students: ",sum(enrolments))
print("Total tuitions:  $", sum(tuitions))
def a_mean(list):
    return sum(list)/len(list)
print("Student mean: ", f"{a_mean(enrolments):.2f}", "Tuition mean: ", f"{a_mean(tuitions):.2f}")

def a_median(list):
    import statistics
    return statistics.median(list)
print("Student median: ", f"{a_median(enrolments):.2f}", "Tuition median: ", f"{a_median(tuitions):.2f}")




#%%
n = int(input("Enter a number: "))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if is_prime(n):
    print("Prime number")
else:
    print("Not a prime number")
#%%

#%%

