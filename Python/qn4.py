import numpy as np 
import random

X = np.random.normal(0,1,(20,20))

Y = np.random.normal(size=(20,1))

theta = np.dot(np.dot(np.linalg.inv(np.dot(X.transpose(),X)),X),Y)

print(theta)