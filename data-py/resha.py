import numpy as np

ventas = np.array([2500, 3000, 4000, 3500, 5000])
gastos = np.array([1500, 1200, 2000, 1800, 2200])

#print(ventas)
echoo = ventas.reshape(5,1)
#print("echoo:", echoo)

reshaped_gastos = np.arange(15).reshape(3, 5)
#print("reshaped_gastos:", reshaped_gastos)


print(np.zeros((10,10)).reshape(2,50))

# Create a 4x4 identity matrix What is
iden = np.identity(4)
print("iden:", iden)

#random_array = np.default_rng().random((3,4))
#print(random_array)



