import numpy as np

def fahrenheit_to_celsius(F):
    return (F - 32) * 5 / 9

temps_f = np.array([32, 68, 100, 212, 77])

vectorized_ftc = np.vectorize(fahrenheit_to_celsius)
temps_c = vectorized_ftc(temps_f)

print("Celsius temperatures:", temps_c)

def power_func(x, p):
    return x ** p

numbers = np.array([2, 3, 4, 5])
powers  = np.array([1, 2, 3, 4])

vectorized_power = np.vectorize(power_func)
result = vectorized_power(numbers, powers)

print("Power results:", result)

A = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])

b = np.array([7, 4, 5])

solution = np.linalg.solve(A, b)

print("Solution (x, y, z):", solution)

A = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])

b = np.array([12, -5, 15])

currents = np.linalg.solve(A, b)

print("Currents (I1, I2, I3):", currents)
