import numpy as np
import random
import copy
from math import floor

def distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i][j] = np.linalg.norm(cities[i] - cities[j])  #Calculating the euclidian distance between two cities
    return dist_matrix

def fitness_function(path, dist_matrix):
    n=len(path)
    notVisited_cities=[i for i in range(n)]
    temp_path = []
    for i in path:
        if abs(floor(i)) % n in notVisited_cities:
            temp_path.append(abs(floor(i)) % n) 
            notVisited_cities.remove(abs(floor(i)) % n)
        else:
            k=np.random.choice(notVisited_cities)
            notVisited_cities.remove(k)
            temp_path.append(k)
        
    path=temp_path
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += dist_matrix[path[i]][path[i + 1]]
    total_distance += dist_matrix[path[-1]][path[0]]  # Complete the cycle
    return temp_path,total_distance


def random_update(global_best_position, best_position, random_position, C):
    updated_position =  global_best_position + C * ( best_position - random_position)
    return updated_position

def RUPSO_TSP(cities, num_particles=100, max_iterations=1000, inertia_weight=0.5,
              cognitive_weight=0.5, social_weight=0.5, C=1.0):
    num_cities = len(cities)
    dist_matrix = distance_matrix(cities)
    print(dist_matrix)
    
    #path velocity bestpath bestfitness are the fields a particle contains 
    particles = [[np.array(np.random.permutation(num_cities)), np.zeros(num_cities), [], float('inf')] for _ in range(num_particles)]
    
    for par in particles:
        par[2]=par[0]
    
    global_best_position = list(np.random.permutation(num_cities))
    global_best_fitness = float('inf')
    final_best_path=[]
    
    for _ in range(max_iterations):
        random_position = list(np.random.permutation(num_cities))
        for i in range(num_particles):
            path, velocity, best_path, best_fitness = particles[i]
            
            cognitive_component = cognitive_weight * np.random.rand() * np.subtract(best_path, path)
            social_component = social_weight * np.random.rand() * np.subtract(global_best_position, path)
            velocity = inertia_weight * velocity + cognitive_component + social_component
            
            path = random_update(global_best_position, best_path, random_position, C)
            path += velocity
            
            opt_path,path_fitness = fitness_function(copy.deepcopy(path), dist_matrix)
            if path_fitness < best_fitness:
                best_fitness = path_fitness
                best_path = path
                particles[i] = [path, velocity, best_path, best_fitness]
                if path_fitness < global_best_fitness:
                    global_best_fitness = path_fitness
                    global_best_position = path
                    final_best_path=opt_path
    
    return global_best_position, global_best_fitness,final_best_path

# Sample testcase
cities = np.array([[0, 0], [1, 2], [3, 1], [5, 3], [4, 3], [7, 2], [8, 9]])  #cities coordinates in x-y plane
best_path, best_fitness,final_best_path = RUPSO_TSP(cities)
print("Best Path:", best_path)
print("Best Fitness:", best_fitness)
print("Changed Path: ",final_best_path)
