from unicodedata import is_normalized
import numpy as np
import matplotlib.pyplot as plt
import math
import random

max = 10
half_max = max/2
epsilon = (8.85418782)*(10**-12)
k = (1/(4*np.pi*epsilon))
charges = []
num_charges = 2
resolution = 15 # ^2 vectors

x,y = np.meshgrid(np.linspace( - max , max , resolution ),np.linspace(-max, max , resolution))

def i_part(q ,x_pos, y_pos):
    i = k * q * (x - x_pos) * (1 / ( (np.sqrt( (x - x_pos)**2 + (y - y_pos)**2 ) )**3 ) )
    return i 

def j_part(q ,x_pos, y_pos):
    i = k * q * (y - y_pos) * (1 / ( (np.sqrt( (x - x_pos)**2 + (y - y_pos)**2 ) )**3 ) )
    return i 

def magn(i, j):
    m = np.sqrt( i**2 + j**2 )
    return m    

q1 = 1
x_pos1 = 5
y_pos1 = 0

q2 = -1
x_pos2 = -5
y_pos2 = 0

# standard plot
i_vector = i_part(q1, x_pos1, y_pos1) + i_part(q2, x_pos2, y_pos2)
j_vector = j_part(q1, x_pos1, y_pos1) + j_part(q2, x_pos2, y_pos2)
magnitude = magn(i_vector, j_vector)
i_normalised = i_vector / magnitude
j_normalised = j_vector / magnitude


plt.scatter(x_pos1, y_pos1, q1*100, "red")
plt.scatter(x_pos2, y_pos2, -q2*100, "blue")
qq = plt.quiver(x ,y ,i_normalised ,j_normalised, magnitude, cmap=plt.cm.coolwarm)
plt.colorbar(qq, cmap=plt.cm.coolwarm)
plt.title("Vector field of two Point Charges")

plt.show()

# looped plot
"""for u in range(5):
    y_pos1 = y_pos1 +1

    i_vector = i_part(q1, x_pos1, y_pos1) + i_part(q2, x_pos2, y_pos2)
    j_vector = j_part(q1, x_pos1, y_pos1) + j_part(q2, x_pos2, y_pos2)
    magnitude = magn(i_vector, j_vector)
    i_normalised = i_vector / magnitude
    j_normalised = j_vector / magnitude

    time.sleep(1)
    plt.scatter(x_pos1, y_pos1, 40, "red")
    plt.scatter(x_pos2, y_pos2, 40, "blue")
    plt.quiver(x ,y ,i_normalised ,j_normalised )
    plt.show()"""
