import random
import copy

class chromosome:
    def __init__(self, items, max_weight):
        self.items = items
        self.max_weight = max_weight
        self.item_picked = self.select_item() #item thief picked
        self.fitness = self.evaluate() # sum the values of item picked by thief
     
    def select_item(self,lst=None):
        items = []
        weight = 0
        if lst == None:
            while True:
                select = random.randint(0,49)
                if weight + self.items[select].weight > self.max_weight:
                    break
                items.append(self.items[select])
                weight += self.items[select].weight
        else:
            sorted(lst, key=lambda x:x.value, reverse= True)
            for i in range(len(lst)):
                if weight + lst[i].weight > self.max_weight:
                    break
                items.append(lst[i])
                weight += lst[i].weight
        
        return items
    
    def evaluate(self):
        fit = 0
        for i in range(len(self.item_picked)):
            fit += self.item_picked[i].value
        
        return fit


class parent_selection:

    def binary_tournament(pop, tour_size, parent_count):
        parent_list = []
        for i in range(parent_count):
            teams = []
            for j in range(tour_size):
                val = random.choice(pop)
                teams.append(val)
                
            sorted(teams, key=lambda x:x.fitness, reverse=True)
            parent_list.append(teams[0])
        
        return parent_list

    def select_best(pop,parent_count):
        pop = sorted(pop, key=lambda x:x.fitness, reverse=True)
        parents = []
        for i in range(parent_count):
            parents.append(pop[i])
        
        return parents
    
    def random(pop, parent_count):
        parents = []
        for i in range(parent_count):
            parents.append(random.choice(pop))
        
        return parents

class crossover:
    def one_point(parent1,parent2):
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)
        crossover1 = random.randint(1,len(parent1.item_picked))
        crossover2 = random.randint(1,len(parent2.item_picked))
        if random.random() < .8:
            child1.item_picked = child1.select_item(parent1.item_picked[:crossover1] + parent2.item_picked[crossover2:])
            child2.item_picked = child2.select_item(parent2.item_picked[:crossover2] + parent1.item_picked[crossover1:])
        
        child1.fitness = child1.evaluate()
        child2.fitness = child2.evaluate()
        return child1, child2


class mutation:
    def mutate(chromo, pop):
        if random.random() < .2:
            select_pop = random.randint(0,len(pop)-1)
            select_pop_item = random.randint(0,len(pop[select_pop].item_picked)-1)
            select_child = random.randint(0,len(chromo.item_picked)-1)
            print(chromo.item_picked[select_child].item)

            chromo.item_picked[select_child] = pop[select_pop].item_picked[select_pop_item]
            print(chromo.item_picked[select_child].item)
            print(pop[select_pop].item_picked[select_pop_item].item)
            chromo.item_picked = chromo.select_item(chromo.item_picked)
            chromo.fitness = chromo.evaluate()
        return chromo

            

class post_select:
    def select_best(pop,count):
        pop = sorted(pop, key=lambda x:x.fitness, reverse=True)
        parents = []
        for i in range(count):
            parents.append(pop[i])
        
        return parents