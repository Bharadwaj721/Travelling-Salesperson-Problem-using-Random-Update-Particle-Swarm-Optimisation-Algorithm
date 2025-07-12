import random
import numpy as np
import copy

# Define the fitness function
def fitness_function(x):
    return np.sum(np.square(x))

# Random update procedure
def random_update(Xg, Xp, Xr, C):
    return Xg + C * (Xp - Xr)


# RUPSO parameters
num_particles = 9    
num_dimensions = 1
max_iterations = 100
inertia_weight = 0.5     #w
cognitive_weight = 0.5   #c1
social_weight = 0.5      #c2
C = 1.0

swarm = [-9.6, -6, -2.6, -1.1, 0.6, 2.3, 2.8, 8.3, 10]

# Initialize particles
particles = np.array([[position, 0, position, fitness_function(position)] for position in swarm])

# Initialize global best
global_best_position = copy.deepcopy(particles[np.argmin(particles[:, 3]), 2])
global_best_fitness = copy.deepcopy(particles[np.argmin(particles[:, 3]), 3])

# RUPSO algorithm
for _ in range(max_iterations):
    randomPosition=copy.deepcopy(swarm[random.randint(0, num_particles-1)])
    for i in range(num_particles):
        position, velocity, best_position, best_fitness = particles[i]
        
        # Update velocity
        cognitive_component = cognitive_weight * np.random.rand() * (best_position - position)
        social_component = social_weight * np.random.rand() * (global_best_position - position)
        velocity = inertia_weight * velocity + cognitive_component + social_component
        
        # Update position
        position = random_update(global_best_position, best_position,randomPosition, C)  
              
        # Update best position and fitness
        fitness = fitness_function(position)
        if fitness < best_fitness:
            best_fitness = fitness
            best_position = position
            particles[i] = [position, velocity, best_position, best_fitness]
            if fitness < global_best_fitness:
                global_best_fitness = fitness
                global_best_position = position

print("Global Best Position:", global_best_position)
print("Global Best Fitness:", global_best_fitness)


 
