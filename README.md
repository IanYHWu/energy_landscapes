# Exploring Energy Landscapes for Particle Clusters

This Python program computes the energy minima and corresponding structures of molecular clusters, employing either the Lennard-Jones or the Morse potentials to model intermolecular interations. Exploration of the energy landscape is done using Metropolis Monte Carlo, with the option of employing simulated annealing to help locate global energy minima.


# Introduction

Several empirical models for intermolecular potentials exist, including the Lennard Jones potential and the Morse potential. These describe the interaction between two molecules or neutral atoms in a qualitatively accurate manner, and possess a single energy minimum corresponding to the most stable molecular geometry. This idea can be extended to systems containing more than two molecules by assuming pairwise interactions, giving rise to a complex, high-dimensional energy landscapes. These energy landscapes may contain many energy minima, and thus many different stable structures are possible. For example, with four molecules, both the tetrahedral and the square-planar geometries are stable, although the tetrahedron corresponds to the global minimum and is thus the most stable.

Exploring such high-dimensional energy landscapes is a challenging task, and one possible approach involves the use of Markov Chain Monte Carlo methods such as Metropolis-Hastings, which uses importance sampling to extract the most probable - and thus most stable - particle configurations. There is no guarentee that the minima found will be the global minimum, so repeating the search many times may be necessary. Another approach to locating the global minimum involves using simulated annealing, where the temperature parameter is decreased throughout the experiment in order to increase convergence to the global minimum. 

The ```samples``` folder contains the results for two experiments - one for a four-particle cluster, and another for a seven-particle cluster. 

A database containing an extensive set of results can be found here: http://doye.chem.ox.ac.uk/jon/structures/LJ/tables.150.html 


# Installation

Clone the repository into your local system using

I may eventually add support for installation via pip.


# Usage

The Python files are contained within the ```src``` folder, and the main program is ```energy_landscapes.py```. The main program is run from the command line using ```$ run_energy_landscapes.py INPUT_FILE.txt output_name```

The input file contains the input parameters of the run. These parameters include: 

     PARTICLES: the no. of atoms in the cluster
     TRIALS: the no. of searches conducted (>10 recommended, more for larger clusters)
     CYCLES: the no. of MC steps within each search (> 50000 recommended, more for larger clusters, default = 100000)
     AMPLITUDE: step size in the MC search (default = 0.1)
     TEMPERATURE: sensitivity to uphill movements (default = 10)
     L: Box size (default = 4)
     POTENTIAL: the interatomic pairwise potential the use (either Morse or Lennard Jones)

Additional parameters can be specified for simulated annealing:

     ANNEAL: use simulated annealing (TRUE/FALSE, default = FALSE)
     ALPHA: parameter for exponential cooling curve (default = 0.9999)
     
The exponential cooling curve takes the form ```T = alpha**t```, where ```T``` is the temperature of the MC step ```t```. You may need to play around with ALPHA, TEMPERATURE and CYCLES to get good results from using simulated annealing.

Example input files can be found in the ```samples``` folder.

The main program outputs a text file containing the results of the search and a binary coords file containing the geometry information of the minima. The minima can be visualised from the command line using ```$ plotter.py [binary coords file] [trial] [CoM]```, with ```[trial]``` corresponding to the selected trial number, and ```[CoM]``` taking either 1 or 0, which toggles displaying the centre of mass and individual bonds. ```min``` can also be used in place of ```[trial]```, which selects for the geometry of lowest energy.

