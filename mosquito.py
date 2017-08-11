# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 14:28:49 2017

@author: thompson
"""

import numpy.random as npr

def main(pop_count_og,infected_count_og,brood_count,only_male_carriers):
    history = []
    parent_pop = []
    child_pop = []
    generation = 0
    
    # this assumes that the death rate is proportional to the brood size 
    # since we have most likely reached some population equilibrium 
    premature_death_rate = 1.0 - (2.0 / float(brood_count))
    
    # member = [is_female, has_male_only_gene]
    for x in range(pop_count_og):
        parent_pop.append([npr.choice([True,False]),False])
    for x in range(infected_count_og):
        parent_pop.append([False,True])
    if only_male_carriers:
        generate = gen_only_male_carriers
    else:
        generate = gen_both_carriers
    
    while (any(member[0] for member in parent_pop)):        
        # the miracle of life
        females = [x for x in parent_pop if x[0]]
        males = [x for x in parent_pop if not x[0]]
        males_only_gene = [x for x in males if not x[1]]
        generation += 1
        stats = [generation, len(parent_pop),float(len(males))/float(len(parent_pop)), 
               float(len(males_only_gene))/float(len(males))]
        print stats
        history.append(stats)
        for x in females:
            male = males[npr.choice(range(len(males)))]
            for y in range(brood_count):
                if npr.random() > premature_death_rate:
                    generate(male, child_pop)
        parent_pop = child_pop
        child_pop = []
        if generation > 1000:
            break
    print stats
        
def gen_only_male_carriers(male, child_pop):
    if male[1]:
        child_pop.append([False,True])
        #parent_pop.append([False,npr.choice([True,False])])
    else:
        child_pop.append([npr.choice([True,False]),False])
        
def gen_both_carriers(male, child_pop):
    if male[1]:
        child_pop.append([False,npr.choice([True,False])])
        #parent_pop.append([False,npr.choice([True,False])])
    else:
        child_pop.append([npr.choice([True,False]),False])
        



'''
class mosquito(object):
    def __init__(self, is_female, has_males_only_gene):
        self.is_female = is_female
        self.has_males_only_gene = has_males_only_gene
'''        
        
if (__name__ == "__main__"):
    #pop_count_og = 1000000
    #infected_count_og = 100
    pop_count_og = 10000
    infected_count_og = 100
    brood_count = 100
    only_male_carriers = False
    main(pop_count_og,infected_count_og,brood_count,only_male_carriers)