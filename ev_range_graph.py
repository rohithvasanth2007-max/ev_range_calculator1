
import matplotlib.pyplot as plt

# Battery parameters
battery_energy_kwh = 19.98
usable_energy = 0.90

# Vehicle speed (km/h)
speeds = [20, 40, 60, 80, 100, 120]

# Illustrative energy consumption (Wh/km)
consumption = [100, 115, 130, 150, 180, 220]

# Calculate estimated driving range
usable_energy_wh = battery_energy_kwh * 1000 * usable_energy

ranges = []
for energy in consumption:
    ranges.append(usable_energy_wh / energy)

# Print results
for speed, distance in zip(speeds, ranges):
    print(f"{speed} km/h -> {distance:.2f} km")

# Draw graph
plt.plot(speeds, ranges, marker="o")
plt.title("EV Battery Range vs Vehicle Speed")
plt.xlabel("Vehicle Speed (km/h)")
plt.ylabel("Estimated Range (km)")
plt.grid(True)
plt.tight_layout()
plt.show()
