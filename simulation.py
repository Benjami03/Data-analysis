import numpy as np
import matplotlib.pyplot as plt
# Parameters
T_a = 20  # Ambient temperature (°C)
k = 0.1   # Cooling constant (per minute)
T_0 = 80  # Initial temperature (°C)
def temperature(t):
    return T_a + (T_0 - T_a) * np.exp(-k * t)
# Time range (0 to 60 minutes)
t = np.linspace(0, 60, 100)
T = temperature(t)
# Plot
plt.figure(figsize=(8, 5))
plt.plot(t, T, label='Temperature of Object', color='b')
plt.axhline(T_a, linestyle='--', color='r', label='Ambient Temperature (20°C)')
plt.xlabel('Time (minutes)')
plt.ylabel('Temperature (°C)')
plt.title("Newton's Law of Cooling Simulation")
plt.legend()
plt.grid()
plt.show()