
import matplotlib.pyplot as plt

# ==================================
# EV VEHICLE AND BATTERY PARAMETERS
# ==================================

mass = 1500                  # Vehicle mass (kg)
gravity = 9.81                # Gravitational acceleration (m/s^2)
rolling_coefficient = 0.012
air_density = 1.225           # kg/m^3
drag_coefficient = 0.28
frontal_area = 2.2            # m^2

battery_energy_kwh = 19.98    # 108S10P battery
usable_energy = 0.90          # 90% usable battery energy
drivetrain_efficiency = 0.90  # 90% efficiency

# Speeds to analyse (km/h)
speeds = [20, 40, 60, 80, 100, 120]

# Store calculated results
rolling_forces = []
aero_forces = []
total_forces = []
wheel_powers = []
consumptions = []
ranges = []

usable_battery_wh = battery_energy_kwh * 1000 * usable_energy

# ==================================
# ENGINEERING CALCULATIONS
# ==================================

for speed_kmh in speeds:

    # Convert speed to m/s
    speed_ms = speed_kmh / 3.6

    # 1. Rolling resistance (N)
    rolling_force = (
        rolling_coefficient * mass * gravity
    )

    # 2. Aerodynamic drag (N)
    aero_force = (
        0.5 * air_density * drag_coefficient
        * frontal_area * speed_ms**2
    )

    # 3. Total tractive force on level road (N)
    total_force = rolling_force + aero_force

    # 4. Wheel power (W)
    wheel_power = total_force * speed_ms

    # 5. Battery energy consumption (Wh/km)
    # Force (N) x 1000 m/km gives J/km.
    # Divide by 3600 to convert J to Wh.
    # Divide by efficiency for battery-side energy.
    if speed_ms > 0:
        consumption = (
            total_force * 1000
            / (3600 * drivetrain_efficiency)
        )
    else:
        consumption = 0

    # 6. Estimated range (km)
    if consumption > 0:
        estimated_range = usable_battery_wh / consumption
    else:
        estimated_range = 0

    rolling_forces.append(rolling_force)
    aero_forces.append(aero_force)
    total_forces.append(total_force)
    wheel_powers.append(wheel_power / 1000)
    consumptions.append(consumption)
    ranges.append(estimated_range)

# ==================================
# DISPLAY RESULTS
# ==================================

print("\nEV PERFORMANCE RESULTS")
print("-" * 85)
print(
    f"{'Speed':>8} {'Rolling N':>12} {'Drag N':>12} "
    f"{'Total N':>12} {'Power kW':>12} "
    f"{'Wh/km':>12} {'Range km':>12}"
)
print("-" * 85)

for i in range(len(speeds)):
    print(
        f"{speeds[i]:8.0f} "
        f"{rolling_forces[i]:12.2f} "
        f"{aero_forces[i]:12.2f} "
        f"{total_forces[i]:12.2f} "
        f"{wheel_powers[i]:12.2f} "
        f"{consumptions[i]:12.2f} "
        f"{ranges[i]:12.2f}"
    )

# ==================================
# PLOT 1: RANGE VS SPEED
# ==================================

plt.figure(figsize=(9, 5))
plt.plot(speeds, ranges, marker="o")
plt.title("EV Estimated Range vs Vehicle Speed")
plt.xlabel("Vehicle Speed (km/h)")
plt.ylabel("Estimated Range (km)")
plt.grid(True)
plt.tight_layout()

# ==================================
# PLOT 2: ENERGY CONSUMPTION VS SPEED
# ==================================

plt.figure(figsize=(9, 5))
plt.plot(speeds, consumptions, marker="s")
plt.title("EV Energy Consumption vs Vehicle Speed")
plt.xlabel("Vehicle Speed (km/h)")
plt.ylabel("Battery Energy Consumption (Wh/km)")
plt.grid(True)
plt.tight_layout()

# ==================================
# PLOT 3: WHEEL POWER VS SPEED
# ==================================

plt.figure(figsize=(9, 5))
plt.plot(speeds, wheel_powers, marker="^")
plt.title("EV Wheel Power vs Vehicle Speed")
plt.xlabel("Vehicle Speed (km/h)")
plt.ylabel("Wheel Power (kW)")
plt.grid(True)
plt.tight_layout()

plt.show()
