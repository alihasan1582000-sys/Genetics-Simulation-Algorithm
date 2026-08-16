import random
import string
from math import floor
import os
import time

# ==========================================
# 1. THE DNA & BUILDING BLOCKS
# ==========================================

def randomCharacter():
    # FIX 1: Included string.ascii_letters so capital 'T' is in the gene pool
    character = random.choice(string.ascii_letters + " ")
    return character

class DNA:
    def __init__(self, length):
        self.genes = []
        self.fitness = 0
        for i in range(length):
            self.genes.append(randomCharacter())
    
    def crossover(self, partner):
        child = DNA(len(self.genes))
        midpoint = random.randint(0, len(self.genes))
        for i in range(len(child.genes)):
            if i > midpoint:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]
        return child

# ==========================================
# 2. EVOLUTIONARY FUNCTIONS
# ==========================================

def generateRandomPopulation(n, target):
    population = []
    for i in range(n):
        population.append(DNA(len(target)))
    return population

def calculateFitness(target, pop):
    for i in pop:
        score = 0
        for j in range(len(target)):
            if i.genes[j] == target[j]:
                score += 1
        i.fitness = score / len(target)

def generateMatingPool(pop):
    mating_pool = []
    for e in pop:
        n = floor(e.fitness * 100)
        for i in range(n):
            mating_pool.append(e)
            
    # FIX 2: Prevent crash on Generation 0 if no one gets a single letter right
    if len(mating_pool) == 0:
        mating_pool = pop[:]
        
    return mating_pool

def breedNewPopulation(n, mating_pool):
    new_pop = []
    for i in range(n):
        parent_a = random.choice(mating_pool)
        parent_b = random.choice(mating_pool)
        child = parent_a.crossover(parent_b)
        new_pop.append(child)
    return new_pop

def mutatePopulation(population, mutation_rate):
    for e in population:
        for c in range(len(e.genes)):
            if random.random() < mutation_rate:
                e.genes[c] = randomCharacter()
    return population

def checkForWinners(population, target):
    # FIX 3: Removed the old print statements that flooded the console
    for e in population:
        if "".join(e.genes) == target:
            return True
    return False

# ==========================================
# 3. ANIMATION & VISUALIZATION ENGINE
# ==========================================

def animateEvolutionTree(generation, population, target):
    # Clear the terminal for animation effect (works on Windows/Mac/Linux)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Sort population to find the best strings
    sorted_pop = sorted(population, key=lambda x: x.fitness, reverse=True)
    best = sorted_pop[0]
    
    # Grab the top two parents to show a "mating event"
    parent_a = sorted_pop[0]
    parent_b = sorted_pop[1] if len(sorted_pop) > 1 else sorted_pop[0]
    demo_child = parent_a.crossover(parent_b)
    
    print(f"=====================================================")
    print(f" EVOLUTION MATRIX | Generation: {generation:4d}")
    print(f"=====================================================")
    print(f" TARGET   : [{target}]")
    print(f" BEST FIT : [{''.join(best.genes)}] ({best.fitness * 100:.1f}%)\n")
    
    print(" --- LIVE CROSSOVER TREE ---")
    print(f" Parent A : [{''.join(parent_a.genes)}]")
    print(f"              \\       /")
    print(f"               \\     /")
    print(f" Parent B : [{''.join(parent_b.genes)}]")
    print(f"                  |")
    print(f"                  V")
    print(f" New Child: [{''.join(demo_child.genes)}]\n")
    
    print(" --- TOP 5 GENE POOL LEADERBOARD ---")
    for i in range(min(5, len(sorted_pop))):
        dna_string = "".join(sorted_pop[i].genes)
        fitness_score = sorted_pop[i].fitness * 100
        print(f" {i+1}. {dna_string}  ->  {fitness_score:.1f}%")
        
    print("=====================================================")
    
    # Pause briefly to create a smooth framerate (adjust to make it faster/slower)
    time.sleep(0.05) 

# ==========================================
# 4. MAIN EXECUTION LOOP
# ==========================================

if __name__ == "__main__":
    target = "Cats Are Cute"
    n = 400 # Increased population size slightly so it evolves faster
    population = generateRandomPopulation(n, target)
    mutation_rate = 0.01
    generation = 0

    while not checkForWinners(population, target):
        # Grade the current generation
        calculateFitness(target, population)
        
        # Draw the animation frame
        animateEvolutionTree(generation, population, target)
        
        # Create the next generation
        mating_pool = generateMatingPool(population)
        population = breedNewPopulation(n, mating_pool)
        population = mutatePopulation(population, mutation_rate)
        generation += 1

    # Final frame when target is reached
    calculateFitness(target, population)
    animateEvolutionTree(generation, population, target)