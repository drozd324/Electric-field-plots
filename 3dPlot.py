from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

max = 10
half_max = max/2
epsilon = (8.85418782)*(10**-12)
k = (1/(4*np.pi*epsilon))
charges = []
num_charges = 2
resolution = 3

fig = plt.figure()
ax = fig.gca(projection='3d')

x, y, z = np.meshgrid(np.arange(-max, max, resolution), np.arange(-max, max, resolution), np.arange(-max, max, resolution))

def i_part(q ,x_pos, y_pos, z_pos):
    i = k * q * (x - x_pos) * (1 / ( (np.sqrt( (x - x_pos)**2 + (y - y_pos)**2 + (z - z_pos)**2) )**3 ) )
    return i 

def j_part(q ,x_pos, y_pos, z_pos):
    i = k * q * (y - y_pos) * (1 / ( (np.sqrt( (x - x_pos)**2 + (y - y_pos)**2 + (z - z_pos)**2) )**3 ) )
    return i 

def k_part(q ,x_pos, y_pos, z_pos):
    i = k * q * (z - z_pos) * (1 / ( (np.sqrt( (x - x_pos)**2 + (y - y_pos)**2 + (z - z_pos)**2) )**3 ) )
    return i 

def magn(i, j, z):
    m = np.sqrt( i**2 + j**2 + z**2)
    return m    

q1 = 1
x_pos1 = 4
y_pos1 = 0
z_pos1 = 0

q2 = -1
x_pos2 = -4
y_pos2 = 0
z_pos2 = 0

# standard plot
i_vector = i_part(q1, x_pos1, y_pos1, z_pos1) + i_part(q2, x_pos2, y_pos2, z_pos1)
j_vector = j_part(q1, x_pos1, y_pos1, z_pos1) + j_part(q2, x_pos2, y_pos2, z_pos1)
k_vector = k_part(q1, x_pos1, y_pos1, z_pos1) + k_part(q2, x_pos2, y_pos2, z_pos1)

magnitude = magn(i_vector, j_vector, k_vector)

i_normalised = i_vector / magnitude
j_normalised = j_vector / magnitude
k_normalised = k_vector / magnitude

size = 100
ax.scatter(x_pos1, y_pos1, z_pos1, c ="red", s = size)
ax.scatter(x_pos2, y_pos2, z_pos2, c = "blue", s = size)
ax.quiver(x, y, z, i_normalised, j_normalised, k_normalised, length=1.5, color = 'black', alpha = .7)
plt.title("Vector field of two Point Charges")
plt.show()
