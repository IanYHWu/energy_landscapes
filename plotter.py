"""
A script to plot from a Potential.py output file.
Call with: python plotter.py [filename.txt] [trial number] [show CoM and bonds (1 for yes, 0 for no)]
"""

import sys
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pickle
import numpy as np

FILE = sys.argv[1]
TRIAL = sys.argv[2]
COM = sys.argv[3]

with open(FILE, 'rb') as fp:
    coords_list = pickle.load(fp)
    min_index = pickle.load(fp)
    min_energy = pickle.load(fp)

if TRIAL == 'min':
    TRIAL = min_index
    print("Displaying minimum energy configuration - trial {} with energy {}".format(min_index, min_energy))
else:
    TRIAL = int(TRIAL)
    print("Displaying trial {}".format(TRIAL))

selected_trial = coords_list[TRIAL]

x_data = selected_trial[0]
y_data = selected_trial[1]
z_data = selected_trial[2]

# compute coordinate averages
avg_x = sum(x_data) / float(len(x_data))
avg_y = sum(y_data) / float(len(y_data))
avg_z = sum(z_data) / float(len(z_data))

# plot coordinates, centred
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x_data, y_data, z_data, s=500)
ax.set_aspect('equal')

max_range = np.array([max(x_data) - min(x_data), max(y_data) - min(y_data), max(z_data) - min(z_data)]).max() / 2.0

mid_x = (max(x_data) + min(x_data)) * 0.5
mid_y = (max(y_data) + min(y_data)) * 0.5
mid_z = (max(z_data) + min(z_data)) * 0.5
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

# plot CoM, and bonds to CoM
if int(sys.argv[3]) == 1:
    ax.scatter(avg_x, avg_y, avg_z, c='r', s=200)

    for a, b, c in zip(x_data, y_data, z_data):
        ax.plot3D([a, avg_x], [b, avg_y], [c, avg_z], 'b')

else:
    pass

if __name__ == '__main__':
    plt.show()
