## The problem
Get the highest fitness value for the problem proposed in ```lab9_lib.py```. 
The fitness function should be treated as a black box: focus on the value provided.
A parameter characterizes the problem; four values for that parameter were suggested: 1, 2, 5, 10.
Running the code a few times makes it obvious that the higher the parameter the harder the problem.
I decided to use the Island Method: some populations are left evolving in parallel, and now and again some migrations are made to promote some diversity.

## Problem Initialization
* ```POPULATION_SIZE```: size of population for each island
* ```OFFSPRING_SIZE```: the size of candidates generated at each iteration
* ```TOURNAMENT_SIZE```: number of participants to a tournament
* ```MUTATION_PROBABILITY```: probability to get a mutation, otherwise a crossover is performed
* ```MUTATIONS```: how many mutations (reversing a single bit) are performed
* ```LOCI```: length of the problem
* ```PROBLEM```: the problem parameter quoted in the introduction
* ```GENERATIONS```: how many iterations of the algorithm are performed for each island
* ```MIGRANTS```: how many individuals are selected to migrate
* ```ISLANDS```: number of islands/populations evolving in parallel
* ```MIGRATE```: migration rate (in terms of iterations)

## The class Island
In order to simplify things, I decided to create a class named ```Island```, composed of an ```id``` and the ```population``` (a list of ```Individual```).
Major functions of this class:
* ```step```: this function makes the population evolve and, since islands are not really running in parallel, it's made for ```MIGRATE``` iterations
* ```inject```: the population on the islands claims individuals coming from the other islands
* ```migrate```: this function returns the best ```MIGRANTS``` among the population, in order to make them migrate

Final note: in the ```mutate``` function it is wanted that two positions to reverse could be equal: it's pretty rare to have two instances of the same number over few values in a range from 0 to 999 :)
