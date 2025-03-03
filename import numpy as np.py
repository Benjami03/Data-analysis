import numpy as np
import matplotlib.pyplot as plt

# Data storage for visualization
time_values = []
population_values = []

def bacteria_growth(env, initial_population, time_limit):
    """Simulates bacteria population growth over time."""
    population = initial_population
    for t in range(time_limit + 1):
        print(f'Time {t}: Population = {population}')
        
        # Store data for plotting
        time_values.append(t)
        population_values.append(population)

        yield env.timeout(1)  # Simulate 1-hour step
        population *= 2  # Double the population

# Set up SimPy environment
env = simpy.Environment()
env.process(bacteria_growth(env, initial_population=100, time_limit=10))

# Run the simulation
env.run()

# Plot the results
plt.figure(figsize=(8, 5))
plt.plot(time_values, population_values, marker='o', linestyle='-', color='b', label="Bacteria Population")
plt.xlabel("Time (hours)")
plt.ylabel("Population")
plt.title("Bacteria Population Growth Over Time")
plt.legend()
plt.grid(True)
plt.show()
