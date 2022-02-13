from unicodedata import is_normalized
import numpy as np
import matplotlib.pyplot as plt
import random

max = 10 # change amount of charges here
half_max = max/2
epsilon = (8.85418782)*(10**-12)
k = (1/(4*np.pi*epsilon))
charges = []
num_charges = 3
resolution =17 # ^2 vectors

for i in range(num_charges):
    q = random.randint(1,5)
    if random.randint(0,1) == 0:
        q = -q
    x = random.randint(-half_max, half_max)
    y = random.randint(-half_max, half_max)

    charge = [q,x,y]  
    charges.append(charge)

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


i_vector = 0
j_vector = 0

for u in range(num_charges):
    i_vector = i_vector + i_part(int(charges[u][0]), int(charges[u][1]), int(charges[u][2]))
    j_vector = j_vector + j_part(int(charges[u][0]), int(charges[u][1]), int(charges[u][2]))

    size = 0
    scale = 15
    if int(charges[u][0])*10 < 0:
        size = -int(charges[u][0])*scale
    else:
        size = int(charges[u][0])*scale

    if int(charges[u][0]) > 0:
        plt.scatter(int(charges[u][1]), int(charges[u][2]), size, "red")
    else:
        plt.scatter(int(charges[u][1]), int(charges[u][2]), size, "blue")

magnitude = magn(i_vector, j_vector)
i_normalised = i_vector / magnitude
j_normalised = j_vector / magnitude

qq = plt.quiver(x ,y ,i_normalised ,j_normalised, magnitude, cmap=plt.cm.coolwarm)
plt.colorbar(qq, cmap=plt.cm.coolwarm)
plt.title("Vector Field of " + str(num_charges) + " Point Charges")
plt.show()
