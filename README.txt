
LENNARD JONES POTENTIAL FOR ATOMIC CLUSTERS

Introduction: This script employs the Metropolis Monte Carlo algorithm in conjunction with basin-hopping to explore the energy minima of Lennard Jones (LJ) clusters.

Theory: The LJ model, first proposed by John Lennard-Jones in 1924, describes the pairwise-interactions of atoms or molecules. The potential is a function of the interatomic distance, and is given by:

            V(r) = 4E[(s/r)**12 - (s/r)**6]

where r is the interatomic distance, s is the length scale and R is the well-depth. Minimising V(r) allows us to find the most stable configuration of the cluster.

An interesting problem arises when considering multiatomic systems. Whereas an analytical solution exists for a pairwise system, the multiatomic system possesses multiple interatomic distances and the potential energy landscape becomes significantly more complex. As far as I am aware, an analytical solution for three body and higher systems does not exist, and so a numerical approach e.g. Metropolis-Hastings, becomes necessary.

Larger clusters possess multiple local minima, and so finding the global minimum requires searching the landscape several times. This incentivises the use of "basin-hopping", whereby we exmploy multiple Metropolis searches in order to maximise the likelihood of identifying the global minimum.


Use: There are two scripts included the LJ folder - one (Lennard_Jones.py) initialises the system and performs Metropolis and basin-hopping. The results are saved in a .txt file. The script also outputs a binary file (FILE_coords) containing the final coordinates of the cluster. This can be read by plotter.py, which outputs a plot of the desired cluster. 

To perform the computation, call python Lennard_Jones.py [save_file]

Parameters can be edited within the script itself:
    n: the no. of atoms in the cluster
    Trials: the no. of searches conducted. (>10 recommended, more for larger clusters)
    Cycles: the no. of MC steps within each search (> 50000 recommended, more for larger clusters)
    Amplitude: step size in the MC search (0.1 recommended)
    Temperature: sensitivity to uphill movements (10 recommended)
    Precision: used for division of random integer. Set really high
    L: Range of starting geometries. (4 recommended, higher for bigger clusters)


To plot, call python plotter.py [binary file] [trial number] [CoM]

Trial number refers to the search trial. CoM can take values of 0 or 1, where 0 plots without the centre of mass, while 1 will plot the centre of mass. This may help visualisation of the structure. 


Results: We will analyse the results of 5_LJ and 8_LJ, as included in the folder, as a demonstration of the script's functionality.

In 5_LJ.txt, all trials have converged to an energy minima of -9.10, which corresponds to the D3h trigonal bipyramidal structure, as expected, as this is the most stable 5-coordinate cluster configuration.

In 8_LJ.txt, we have identified 3 minima: -19.8 is the most stable minima (trial 6), followed by -19.7 (trials 1, 4, 7 and 10), and then by -18.8. Trial 6 corresponds to the known Cs sytmmetry configuration, which is indeed the global minimum. As the minima are all of similar energy, it is no surprise that multiple searches were required to generate the global minima. 

For a list of known energy minimia, see: 

http://doye.chem.ox.ac.uk/jon/structures/LJ/tables.150.html 








 










 




 
