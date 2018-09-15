import numpy as np
x = np.random.random_integers(0,20,size=15)
print("the array of random vector is", x)
print("Frequent value is:", np.bincount(x).argmax())