# Travelling Salesperson Problem using Random Update Particle Swarm Optimisation Algorithm

## Introduction

The **Travelling Salesman Problem (TSP)** is a foundational problem in the fields of computer science, operations research, and optimization. It involves finding the shortest route that visits a set of cities exactly once and returns to the starting point. Due to its combinatorial complexity, TSP is often used to evaluate and benchmark optimization algorithms. This project explores a novel approach to solving TSP using the **Random Update Particle Swarm Optimization (RUPSO)** algorithm, an enhancement of the classic PSO method. By integrating randomness into the particle update mechanism, RUPSO helps avoid premature convergence and improves overall solution quality.

## Problem Statement

**Input:** List of cities and their coordinates

**Objective:**  
Given a list of cities and the distances between each pair, find the shortest possible route that visits each city exactly once and returns to the starting city. The goal is to minimize the total distance traveled.

---

## Proposed Solution

This project implements a novel algorithm called **Random Update Particle Swarm Optimisation (RUPSO)** — a hybrid approach that combines:
- Particle Swarm Optimisation (PSO)
- A random update mechanism

The random update procedure introduces additional randomness during position updates to help escape local optima and improve exploration of the solution space.

---

## Main Contribution

While the **Random Update Particle Swarm Optimization (RUPSO)** algorithm already exists in literature, our main contribution in this project is its **novel application to the Travelling Salesman Problem (TSP)**.

Specifically, we contribute the following:

- Applied RUPSO to the TSP — a combinatorial optimization problem — and demonstrated its effectiveness.
- Designed a complete pipeline to convert city coordinates into a graph and evaluate paths using a fitness function based on round-trip distance.
- Achieved **better performance** (fitness = 27.463) compared to traditional PSO on a 7-city TSP instance.
- Provided a modular and reusable Python implementation that can be extended for larger TSP instances or integrated with other metaheuristics.

## Tools and Technologies 

- Python3
- VScode
## Results

### Input

The TSP graph is fully connected and undirected. The coordinates of the cities are:

City 0 : [0, 0]
City 1 : [1, 2]
City 2 : [3, 1]
City 3 : [5, 3]
City 4 : [4, 3]
City 5 : [7, 2]
City 6 : [8, 9]


Fitness function = total round-trip path length of TSP.

### Output

- **Best Fitness (Optimal Path Length):** `27.463`  
- **Changed Path (Optimal Route):** `5 → 6 → 3 → 4 → 1 → 0 → 2`

RUPSO outperforms standard PSO by achieving better fitness on this dataset.

---

## Limitations

Despite its strengths, RUPSO has the following limitations:

1. **Local Optima Trap:**  
   May converge prematurely to suboptimal solutions.

2. **Parameter Sensitivity:**  
   Requires careful tuning of parameters (e.g., number of particles, inertia weight, random update rate).

3. **Convergence Speed:**  
   Convergence time can be high for complex TSP instances.

4. **Solution Quality Trade-offs:**  
   In some scenarios, it may favor computational efficiency over optimal accuracy.

---

## Conclusion

The **Random Update Particle Swarm Optimization (RUPSO)** algorithm presents a promising approach to tackle the TSP by leveraging the collective intelligence of a swarm of particles. RUPSO combines random updates with traditional PSO components like inertia, cognitive, and social terms to explore the solution space efficiently. Through our implementation and experimentation with RUPSO on TSP instances, we observed **notable improvements in convergence speed and solution quality** compared to standard PSO and other optimization algorithms.

---

## Contact
Feel free to reach out to me via:

Email: bharadwaj9632@gmail.com

GitHub: [@Bharadwaj721](https://github.com/Bharadwaj721)

I'd be happy to discuss, collaborate, or just hear your thoughts!

## Citation

If you use or refer to this implementation in your work, please cite the original RUPSO paper:

```bibtex
@article{article,
  author = {Dadashi, H. and Mohammadi, M.},
  year = {2023},
  month = {10},
  pages = {104933},
  title = {Random update particle swarm optimizer (RUPSO): A novel robust optimization algorithm},
  volume = {56},
  journal = {Structures},
  doi = {10.1016/j.istruc.2023.104933}
}

```
## License 

This project is licensed under the [MIT License](./LICENSE).
