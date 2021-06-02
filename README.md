# Evolutionary-Algorithm

Knapsack Problem algorithm
In the supermarket there are n items (n ≤ 50) the item i has weight W[i] ≤ 50 and value V[i] ≤ 50. A thief breaks into the supermarket, the thief cannot carry weight exceeding M (M ≤ 50). The problem to be solved here is: which packages the thief will take away to get the highest value?

Thief will randomly select item unitl it reaches maximum weight
Then we will evaluate fitness by taking the sum of value in picked item list

Parent Selection
selecting parents from binary tournament


Crossover
I took two crossover points, 
cross1 = randomly select from 0 to length of parent1 
cross2 = randomly select from 0 to length of parent2
so child1 will get items [0:cross1] of parent1 + [cross2:] of parent2
and child2 will get items [0:cross2] of parent2 + [cross1:] of parent1
then we will sort them first by thier value and then select items until it reaches its maximum weight
and then I am evaluating fitness


Mutation
I am taking an item from my chromosome and replacing it with population's chromosome item


Survival Selection
To select the new population I am simply picking best from the overall population
