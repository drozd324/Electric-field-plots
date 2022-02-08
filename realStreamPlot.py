import numpy as np
import matplotlib.pyplot as plt
# if using a Jupyter notebook, include:


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
x_pos1 = 4
y_pos1 = 0

q2 = -1
x_pos2 = -4
y_pos2 = 0


i_vector = i_part(q1, x_pos1, y_pos1) + i_part(q2, x_pos2, y_pos2)
j_vector = j_part(q1, x_pos1, y_pos1) + j_part(q2, x_pos2, y_pos2)
magnitude = magn(i_vector, j_vector)
i_normalised = i_vector / magnitude
j_normalised = j_vector / magnitude


fig, ax = plt.subplots(figsize=(6,6))
strm = ax.streamplot(x,y,i_vector,j_vector, density = .9, color = magnitude ,cmap = 'coolwarm')

size = 10
ax.set_aspect('equal')
ax.plot(x_pos1, y_pos1, "ro", markersize = size)
ax.plot(x_pos2, y_pos2, "bo", markersize = size)
ax.set_title('Stream Plot of Two Point Charges')
cbar=fig.colorbar(strm.lines)
cbar.draw_all()


plt.show()