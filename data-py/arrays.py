import numpy as np

ventas = np.array([2500, 3000, 4000, 3500, 5000])
gastos = np.array([1500, 1200, 2000, 1800, 2200])


print("gastos:", gastos)

ones = np.ones((5,6), dtype=float)

print("ones:", ones)

zeros = np.zeros(10)
print("zeros:", zeros)

# create an array with values spaced by enters
arange_array = np.arange(5, 20, 3)
print("arange_array:", arange_array)

# Create an array with values linearly spaced between 0 and 1

linspace_array = np.linspace(0, 1, 8)
print("linspace_array:", linspace_array)