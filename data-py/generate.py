#Generating random numbers array from 0 to 1

import numpy as np

rdm = np.random.default_rng(549)
random_array = rdm.random(10)

#print(random_array)


# Igual que arriba pero en 
print(np.random.default_rng(5488).random(10))

