import random
import numpy as np
import copy

# Define the fitness function
def fitness_function(x):
    return np.sum(np.square(x))

# Random update procedure
def random_update(Xg, Xp, Xr, C):
    return Xg + C * (Xp - Xr)

#Initialization
def initialize_particles(num_particles, num_dimensions):
    particles = []
    for _ in range(num_particles):
        position = np.random.uniform(-5.12, 5.12, size=(num_dimensions))
        velocity = np.zeros(num_dimensions)
        best_position = position.copy()
        best_fitness = float('inf')
        particles.append((position, velocity, best_position, best_fitness))
    return particles

def RUPSO(particles,num_particles = 100,num_dimensions = 2,max_iterations = 1000,inertia_weight = 0.5,cognitive_weight = 0.5,social_weight = 0.5,C = 1.0):
    print("RUPSO")
    print(particles)
    
    global_best_position = np.zeros(num_dimensions)
    global_best_fitness = float('inf')

    # RUPSO algorithm
    for _ in range(max_iterations):
        randomPosition=copy.deepcopy(particles[random.randint(0, num_particles-1)][0])
        for i in range(num_particles):
            position, velocity, best_position, best_fitness = particles[i]
            
            # Update velocity
            cognitive_component = cognitive_weight * np.random.rand() * (best_position - position)
            social_component = social_weight * np.random.rand() * (global_best_position - position)
            velocity = inertia_weight * velocity + cognitive_component + social_component
            
            # Update position
            position = random_update(global_best_position, best_position,randomPosition, C)
            
            position += velocity
            
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


def PSO(particles,num_particles = 100,num_dimensions = 2,max_iterations = 1000,inertia_weight = 0.5,cognitive_weight = 0.5,social_weight = 0.5):
    print("PSO")
    print(particles)
   
    global_best_position = np.zeros(num_dimensions)
    global_best_fitness = float('inf')

    # PSO algorithm
    for _ in range(max_iterations):
        for i in range(num_particles):
            position, velocity, best_position, best_fitness = particles[i]
            
            # Update velocity
            cognitive_component = cognitive_weight * np.random.rand() * (best_position - position)
            social_component = social_weight * np.random.rand() * (global_best_position - position)
            velocity = inertia_weight * velocity + cognitive_component + social_component
            
            # Update position
            position += velocity
            
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

 
# RUPSO parameters
num_particles = 10   
num_dimensions = 2
max_iterations = 100
inertia_weight = 0.5     #w
cognitive_weight = 0.5   #c1
social_weight = 0.5      #c2
C = 1.0

particles = initialize_particles(num_particles, num_dimensions)



# PSO(copy.deepcopy(particles),num_particles,num_dimensions,max_iterations,inertia_weight,cognitive_weight,social_weight)
PSO(copy.deepcopy(particles),num_particles,num_dimensions,max_iterations,inertia_weight,cognitive_weight,social_weight)
RUPSO(copy.deepcopy(particles),num_particles,num_dimensions,max_iterations,inertia_weight,cognitive_weight,social_weight,C)