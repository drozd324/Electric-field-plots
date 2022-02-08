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
num_charges = 3
resolution = 25 # ^2 vectors

for i in range(num_charges):
    q = random.randint(2,5)
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

fig, ax = plt.subplots(figsize=(6,6))

ax.set_aspect('equal')
ax.set_title('Stream Plot of Two Point Charges')


for u in range(num_charges):
    i_vector = i_vector + i_part(int(charges[u][0]), int(charges[u][1]), int(charges[u][2]))
    j_vector = j_vector + j_part(int(charges[u][0]), int(charges[u][1]), int(charges[u][2]))

    size = 0
    scale = 3
    if int(charges[u][0])*10 < 0:
        size = -int(charges[u][0])*scale
    else:
        size = int(charges[u][0])*scale

    if int(charges[u][0]) > 0:
        ax.plot(int(charges[u][1]), int(charges[u][2]), "ro", markersize = size )
    else:
        ax.plot(int(charges[u][1]), int(charges[u][2]), "bo", markersize = size )

magnitude = magn(i_vector, j_vector)
i_normalised = i_vector / magnitude
j_normalised = j_vector / magnitude

strm = ax.streamplot(x,y,i_vector,j_vector, density = .9, color = magnitude ,cmap = 'coolwarm')
ax.set_title("Stream Plot of " + str(num_charges) + " Point Charges")
cbar=fig.colorbar(strm.lines)
cbar.draw_all()

plt.show()