"""
A script to compute the energy minima of Lennard-Jones clusters.
Call with: python energy_landscapes.py [save file name]
"""

import math
import random
import numpy as np
import pickle


def LJ(r):
    """Returns the LJ energy"""

    return 4 * (((1 / r) ** 12) - ((1 / r) ** 6))


def get_length(l):
    """Returns the length of a vector"""

    return math.sqrt(l[0] * l[0] + l[1] * l[1] + l[2] * l[2])


def vector_difference(a, b):
    """Returns the vector subtraction of two vectors"""

    return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]


def generate_particles(n, L):
    """Generates random coordinates for n particles. Returns a dictionary mapping particle ID to coordinates"""

    vec_dict = {}

    # create n particles 
    for i in range(0, n):
        particle_coords = []

        # randomise their coordinates
        for j in range(0, 3):
            coord = random.uniform(0, L)
            particle_coords.append(coord)

        vec_dict[i] = particle_coords

    return vec_dict


def generate_energy_dict(vec_dict):
    """Generates a dictionary mapping particle ID to the sum of all pairwise interaction energies
    involving the given particle"""

    energy_dict = {}

    for key_i, val_i in vec_dict.items():
        energy = 0
        for key_j, val_j in vec_dict.items():
            if key_j != key_i:
                diff = vector_difference(val_i, val_j)
                length = get_length(diff)
                energy += LJ(length)
        energy_dict[key_i] = energy

    return energy_dict


def update_energy_dict(energy_dict, vec_dict, index):
    """Re-computes the sum of pairwise interactions involving a particle with ID = index.
    Returns the modified energy_dict"""

    energy = 0
    for key, val in vec_dict.items():
        if key != index:
            diff = vector_difference(vec_dict[index], val)
            length = get_length(diff)
            energy += LJ(length)
    energy_dict[index] = energy

    return energy_dict


def metropolis(n, cycles, amplitude, temperature, L, anneal, alpha):
    """Performs Metropolis Monte Carlo on the system to locate minima, with the option to perform simulated annealing"""

    count = 0
    # initialise the appropriate dictionaries
    vec_dict = generate_particles(n, L)  # Generate particle coordinates
    energy_dict = generate_energy_dict(vec_dict)
    # compute the starting energy
    init_energy = 0.5 * sum(energy_dict.values())  # factor of 0.5 to account for double counting

    while count < cycles:
        # initialise exponential cooling curve if annealing in use
        if anneal:
            temperature = temperature * alpha ** count

        move = (-0.5 * amplitude) + amplitude * (random.uniform(0, 1))  # Generate random perturbation
        random_particle = random.randint(0, n - 1)  # Select random particle to perturb
        random_coordinate = random.randint(0, 2)  # Select random cartesian coordinate to perturb

        # Update coordinates and energy after perturbation
        init_value = vec_dict[random_particle][random_coordinate]
        vec_dict[random_particle][random_coordinate] = init_value + move
        energy_dict = update_energy_dict(energy_dict, vec_dict, random_particle)
        update_energy = 0.5 * sum(energy_dict.values())

        count += 1

        # If new energy < old energy, accept update
        if update_energy <= init_energy:
            init_energy = update_energy

        # If new energy > old energy, accept update with probability P
        else:
            P = np.exp(-(update_energy - init_energy) / temperature)
            uniform_no = random.uniform(0, 1)

            if P < uniform_no:
                init_energy = update_energy

            # if move is rejected, reverse the move and then re-compute the energy dictionary
            else:
                vec_dict[random_particle][random_coordinate] = init_value - move
                energy_dict = update_energy_dict(energy_dict, vec_dict, random_particle)

    # lists to record final coordinates
    x_data = []
    y_data = []
    z_data = []

    # Record x, y and z coordinates corresponding to energy minima
    for val in vec_dict.values():
        x_data.append(val[0])
        y_data.append(val[1])
        z_data.append(val[2])

    return x_data, y_data, z_data, init_energy


def run_el(n, trials, cycles, amplitude, temperature, L, output, anneal, alpha):
    """Driver function for metropolis. Repeats the caclulation and writes the results to file"""

    # sys.argv inputs
    output_txt = output + '.txt'
    output_pckl = output + '_coords'

    # Write to file
    f = open(output_txt, 'w+')
    f.write('Exploring Energy Surfaces: ' + str(n) + '-coordinate system' + '\n')
    if anneal:
        f.write('Using Simulated Annealing')
    f.close()

    # Perform multiple optimisations and write to file. Also create pickled object containing final coordinates
    output_coords_list = []
    min_energy = 0
    min_index = 0
    for i in range(0, trials):
        met_output = metropolis(n, cycles, amplitude, temperature, L, anneal, alpha)
        if met_output[3] <= min_energy:
            min_energy = met_output[3]
            min_index = i
        print('Iteration {} out of {} complete. Writing to file...'.format(i, trials))
        f = open(output_txt, 'a')
        f.write('\n TRIAL {}  \n  Energy: {} \n \n Coordinates (x,y,z) \n'.format(i + 1, met_output[3]))

        for xyz in zip(met_output[0], met_output[1], met_output[2]):
            f.write('\n' + '\t'.join([str(m) for m in xyz]))

        output_coords = [met_output[0], met_output[1], met_output[2]]
        output_coords_list.append(output_coords)

        f.write('\n')
        f.close()

    # write coordinates to the pickle file
    with open(output_pckl, 'wb') as fp:
        pickle.dump(output_coords_list, fp)
        pickle.dump(min_index, fp)
        pickle.dump(min_energy, fp)


