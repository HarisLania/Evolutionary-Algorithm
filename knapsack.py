print(
"""
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

"""
)

import random
import EA_operators

class SuperMarket:
    def __init__(self, item):
        self.item = item
        self.weight = random.randint(0,50)
        self.value = random.randint(0,50)
    
items = []
for i in range(50):
    items.append(SuperMarket(i))

print('All items with thier weight and value')
for i in range(len(items)):
    print('Item: {}, Weight: {} - Value: {}'.format(items[i].item, items[i].weight, items[i].value))


pop = [_ for _ in range(10)]

for i in range(10):
    pop[i] = EA_operators.chromosome(items, 50)  # passign all the items and maximum weight thief can pick


print('Items thief can pick')
for i in range(len(pop)):
    print('Condition: {} \nItems: {}\nWeigth:{}           -          Fitness:{}'.format(i, [j.item for j in pop[i].item_picked], sum([j.weight for j in pop[i].item_picked]), pop[i].fitness))


for i in range(10):
    new_pop = []
    for i in range(0, len(pop), 2):
        parents = EA_operators.parent_selection.binary_tournament(pop, 4, 2)
        child1, child2 = EA_operators.crossover.one_point(parents[0], parents[1])
        EA_operators.mutation.mutate(child1, pop)
        EA_operators.mutation.mutate(child2, pop)
        new_pop.append(child1)
        new_pop.append(child2)




    print('*********************************')
    print('New Population')
    for i in range(len(new_pop)):
        print('Condition: {} \nItems: {}\nWeigth:{}           -          Fitness:{}'.format(i, [j.item for j in new_pop[i].item_picked], sum([j.weight for j in new_pop[i].item_picked]), new_pop[i].fitness))


    pop = EA_operators.post_select.select_best(new_pop+pop, len(pop))

    print('*********************************')
    print('After Post Select')
    for i in range(len(pop)):
        print('Condition: {} \nItems: {}\nWeigth:{}           -          Fitness:{}'.format(i, [j.item for j in pop[i].item_picked], sum([j.weight for j in pop[i].item_picked]), pop[i].fitness))