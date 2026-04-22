import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

N = 10000
beta = 0.3
gamma = 0.05
time_points = 1000

# Percentages of vaccination to test
vaccination_rates = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

plt.figure(figsize=(7, 5), dpi=150)

# Set up colors using the viridis color map as suggested in the PDF
colors = cm.viridis(np.linspace(0, 1, len(vaccination_rates)))

# Loop through each vaccination rate
for idx, v_rate in enumerate(vaccination_rates):
    
    # Calculate initial populations based on vaccination
    V = int(N * v_rate) # Vaccinated individuals are immune
    I = 1
    S = N - V - I
    R = 0
    
    # We only need to track Infected for this plot
    I_arr = [I]
    
    # Time course for current vaccination rate
    for t in range(time_points):
        p_infection = beta * (I / N)
        p_infection = min(p_infection, 1.0)
        p_recovery = gamma
        
        if S > 0 and p_infection > 0:
            new_infections = np.sum(np.random.choice([1, 0], S, p=[p_infection, 1 - p_infection]))
        else:
            new_infections = 0
            
        if I > 0:
            new_recoveries = np.sum(np.random.choice([1, 0], I, p=[p_recovery, 1 - p_recovery]))
        else:
            new_recoveries = 0
            
        S -= new_infections
        I = I + new_infections - new_recoveries
        R += new_recoveries
        
        I_arr.append(I)
    
    # Plot the infected curve for this specific vaccination rate
    label_str = f"{int(v_rate * 100)}%"
    plt.plot(I_arr, label=label_str, color=colors[idx])

# Format the plot
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.tight_layout()

# Save and show
plt.savefig("SIR_vaccination.png")
plt.show()

# Question:
# Based on the mathematical formula (1 - gamma/beta) = 1 - (0.05/0.3) ≈ 83.3%.
# Looking at the plot, at 80% to 90% vaccination, the infection curve completely 
# flatlines, preventing the disease from spreading.