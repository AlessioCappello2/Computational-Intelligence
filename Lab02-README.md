## Adaptive strategy
A genome is a pair of float numbers, in my code encoded as a dict, with two fields: 
  - `row`: represents the "percentage" of row to take (i.e. `row`=0.5 and #rows=6, elements will be taken from the third row)
  -  `elements`: represents the percentage of elements to take (i.e. `elements`=0.6 and the considered row has 5 elements, 3 elements will be taken)

The code is written such that empty rows are discarded in the computation.
Three slightly different versions:
  - basic: the sigma used to get new individuals is fixed and shared between the float values of the genome
  - self_adaptive 1: the sigma used to get new individuals changes, and for each generation the value related to the winning candidate is saved and used for the next generation
  - self_adaptive 2: similar to the previous one, but each value of the genome has its sigma value


## Fitness 
It's simply defined as the win rate over a certain number of games versus the other strategy (default, #games=1000).
For each generation, we select the candidate with the highest fitness value.

## Tweak
Sample two random numbers and add them to the current genome to get a new candidate. It checks that the values are in the range [0, 1).

## Training 
Since there is no clue at the beginning, a random genome is initialized. If we adopt a self-adaptive strategy, also the sigma is randomly initialized.
It's also possible to decide between a comma or a plus strategy.
