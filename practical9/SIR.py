import numpy as np
import matplotlib.pyplot as plt

# 1. Define the basic variables of the model
N = 10000
I = 1
S = N - I
R = 0

beta = 0.3
gamma = 0.05
time_points = 1000

# 2. Create arrays to track variables over time
S_arr = [S]
I_arr = [I]
R_arr = [R]

# 3. Time course loop
for t in range(time_points):
    # Calculate probabilities for this time step
    # Probability of infection depends on the proportion of infected people
    p_infection = beta * (I / N)
    p_recovery = gamma
    
    # Cap probability at 1.0 to avoid numpy errors in extreme edge cases
    p_infection = min(p_infection, 1.0)
    
    # Pick susceptible individuals at random to become infected
    # np.random.choice returns an array of 1s (infected) and 0s (stayed susceptible)
    if S > 0 and p_infection > 0:
        new_infections = np.sum(np.random.choice([1, 0], S, p=[p_infection, 1 - p_infection]))
    else:
        new_infections = 0
        
    # Pick infected individuals at random to become recovered
    if I > 0:
        new_recoveries = np.sum(np.random.choice([1, 0], I, p=[p_recovery, 1 - p_recovery]))
    else:
        new_recoveries = 0
        
    # Update populations
    S -= new_infections
    I = I + new_infections - new_recoveries
    R += new_recoveries
    
    # Record the output of the time step
    S_arr.append(S)
    I_arr.append(I)
    R_arr.append(R)

# 4. Plot the results
plt.figure(figsize=(6, 4), dpi=150)
plt.plot(S_arr, label='susceptible', linewidth=2)
plt.plot(I_arr, label='infected', linewidth=2)
plt.plot(R_arr, label='recovered', linewidth=2)

plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()
plt.tight_layout()

# Save and show
plt.savefig("SIR_model.png")
plt.show()