import numpy as np
import matplotlib.pyplot as plt

'''
PSEUDOCODE PLAN:
1. Initialize a 100x100 grid with 0s (Susceptible).
2. Pick a random x, y coordinate and set it to 1 (Infected).
3. Set beta = 0.3, gamma = 0.05. Define times to plot: 0, 10, 50, 100.
4. Loop through time t from 1 to 100:
    a. Make a copy of the grid to hold updates for the next step (to avoid domino effects in a single step).
    b. Find all current infected points using np.where(grid == 1).
    c. Loop through each infected point:
        - Determine if it recovers (random chance < gamma). If so, update next_grid to 2.
        - Look at its 8 neighbors (row - 1 to row + 1, col - 1 to col + 1).
        - Ensure neighbor coordinates are inside grid boundaries.
        - If neighbor is Susceptible (0), determine if it gets infected (random chance < beta). 
          If so, update next_grid to 1.
    d. Overwrite old grid with next_grid.
    e. If t is in plotting times, generate a subplot using imshow().
'''

# 1. Setup grid and parameters
grid_size = 100
population = np.zeros((grid_size, grid_size))
beta = 0.3
gamma = 0.05

# 2. Start with exactly one infected person randomly placed
outbreak = np.random.choice(range(grid_size), 2)
population[outbreak[0], outbreak[1]] = 1

# Prepare subplots for visualization at different time points
times_to_plot = [0, 10, 50, 100]
fig, axes = plt.subplots(2, 2, figsize=(8, 8), dpi=150)
axes = axes.flatten()
plot_idx = 0

# 3. Time course simulation
for t in range(101):
    
    # Plot if it's one of the targeted time points
    if t in times_to_plot:
        ax = axes[plot_idx]
        ax.imshow(population, cmap='viridis', interpolation='nearest', vmin=0, vmax=2)
        ax.set_title(f"Time: {t}")
        plot_idx += 1

    # Create a copy of the grid to update simultaneously
    next_population = population.copy()
    
    # Find all currently infected cells
    infected_x, infected_y = np.where(population == 1)
    
    for i in range(len(infected_x)):
        r = infected_x[i]
        c = infected_y[i]
        
        # Chance to recover
        if np.random.rand() < gamma:
            next_population[r, c] = 2
            
        # Chance to infect neighbors
        # Iterate over the 3x3 block around the infected cell
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                # Skip the center cell (itself)
                if dr == 0 and dc == 0:
                    continue
                    
                nr = r + dr
                nc = c + dc
                
                # Check boundaries
                if 0 <= nr < grid_size and 0 <= nc < grid_size:
                    # Check if neighbor is susceptible
                    if population[nr, nc] == 0 and next_population[nr, nc] == 0:
                        # Attempt infection
                        if np.random.rand() < beta:
                            next_population[nr, nc] = 1
                            
    # Apply updates for the next time step
    population = next_population

plt.tight_layout()
plt.savefig("spatial_SIR.png")
plt.show()