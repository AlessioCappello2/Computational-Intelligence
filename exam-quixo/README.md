# Quixo
I implemented three different agents for Quixo.

### MinMax with Alpha-Beta pruning
A standard MinMax algorithm improved with Alpha-Beta pruning. It's possible to set the preferred value for depth. I tested with depth at most 4, pushing it further can become computationally expensive.
It's possible to choose among three possible final evaluations:
- ```simple```: give reward for winning a game, penalty for losing a game;
- ```rcd```: to the simple one, add positive reward proportional to the length of the maximal sequence of the player and add penalty proportional to the length of the maximal sequence of the opponent;
- ```rcd-enhanced```: it's possible to choose the weights to give to the reward and penalty, while also encouraging configurations with fewer free spots.

### MinMax tuned with GA
Different rules have been used and the respective weights have been tuned using a GA algorithm. Different weights are taken into account basing on the time during the game (early or late game). Here I've
considered the difference between the number of placeholders belonging to the two players, the number of sequences of 4 consecutive elements and the number of sequences of 3 consecutive elements.

### Q-Learning
A standard Q-Learning approach using the Bellman equation. There are a huge number of (state, action), so the combinations met during the training phase were encoded to save some memory. It's possible to save
the q-table and load it for a subsequent test run.

## Performances
I evaluated the agents against the ```RandomPlayer``` provided: for the two MinMax implementations I got a winrate of 100%, while for the Q-Learning here are the best results I got:
- as first player: winrate 68.7 %
- as second player: winrate 58.9 % \
This is due to the huge number of possible configurations: without considering symmetries there are $3^{25}$ combinations. Considering the symmetries wouldn't help so much (just reducing this number of an 8-factor).
I trained the Q-Learning for 300k episodes due to limited computational resources.

### Notes
- After 50 moves, a game it's automatically considered as a tie;
- I changed the move method, I preferred not to invert the row with the column;
- I can't upload the q-table on GitHub since it's a file of several GBs.

### Resources
- Lab10 - Tic-Tac-Toe for Q-Learning;
- MinMax with Alpha-Beta pruning: https://medium.com/@amadi8/tic-tac-toe-agent-using-alpha-beta-pruning-18e8691b61d4;
- ChatGPT for compressing the states;
- I worked with Lorenzo Nikiforos s317616. 
