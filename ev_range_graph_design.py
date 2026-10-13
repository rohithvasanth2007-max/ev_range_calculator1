
import matplotlib.pyplot as plt

# =====================================================
# 1. EV VEHICLE PARAMETERS
# =====================================================

mass = 1500                     # Vehicle mass (kg)
gravity = 9.81                  # Gravitational acceleration (m/s^2)
rolling_coefficient = 0.012     # Rolling resistance coefficient
air_density = 1.225             # Air density (kg/m^3)
drag_coefficient = 0.28         # Aerodynamic drag coefficient
frontal_area = 2.2              # Vehicle frontal area (m^2)

# =====================================================
# 2. BATTERY PARAMETERS
# =====================================================

series_cells = 108
parallel_strings = 10
cell_voltage = 3.7              # V
cell_capacity = 5               # Ah

usable_energy_fraction = 0.90   # 90% usable energy
drivetrain_efficiency = 0.90    # 90% drivetrain efficiency

# Battery pack calculations
battery_voltage = series_cells * cell_voltage
battery_capacity = parallel_strings * cell_capacity
battery_energy_kwh = (
    battery_voltage * battery_capacity
) / 1000

usable_battery_energy_wh = (
    battery_energy_kwh * 1000 * usable_energy_fraction
)

# =====================================================
# 3. SPEED PARAMETERS
# =====================================================

speeds = [20, 40, 60, 80, 100, 120]  # km/h

# =====================================================
# 4. RESULT LISTS
# =====================================================

rolling_forces = []
aero_forces = []
total_forces = []
wheel_powers = []
motor_powers = []
consumptions = []
ranges = []

# =====================================================
# 5. ENGINEERING CALCULATIONS
# =====================================================

for speed_kmh in speeds:

    # Convert km/h to m/s
    speed_ms = speed_kmh / 3.6

    # Rolling resistance force (N)
    rolling_force = (
        rolling_coefficient * mass * gravity
    )

    # Aerodynamic drag force (N)
    aero_force = (
        0.5
        * air_density
        * drag_coefficient
        * frontal_area
        * speed_ms**2
    )

    # Total tractive force on a level road (N)
    total_force = rolling_force + aero_force

    # Mechanical power required at the wheels (W)
    wheel_power_w = total_force * speed_ms

    # Approximate motor/battery-side power (W)
    motor_power_w = wheel_power_w / drivetrain_efficiency

    # Battery energy consumption (Wh/km)
    if speed_ms > 0:
        consumption = (
            total_force * 1000
            / (3600 * drivetrain_efficiency)
        )
    else:
        consumption = 0

    # Estimated range (km)
    if consumption > 0:
        estimated_range = (
            usable_battery_energy_wh / consumption
        )
    else:
        estimated_range = 0

    # Store results
    rolling_forces.append(rolling_force)
    aero_forces.append(aero_force)
    total_forces.append(total_force)
    wheel_powers.append(wheel_power_w / 1000)
    motor_powers.append(motor_power_w / 1000)
    consumptions.append(consumption)
    ranges.append(estimated_range)

# =====================================================
# 6. DISPLAY BATTERY PARAMETERS
# =====================================================

print("\n========== EV BATTERY PARAMETERS ==========")
print(f"Series cells              : {series_cells}")
print(f"Parallel strings          : {parallel_strings}")
print(f"Battery voltage           : {battery_voltage:.2f} V")
print(f"Battery capacity           : {battery_capacity:.2f} Ah")
print(f"Nominal battery energy     : {battery_energy_kwh:.2f} kWh")
print(f"Usable battery energy      : {usable_battery_energy_wh:.2f} Wh")
print(f"Drivetrain efficiency      : {drivetrain_efficiency * 100:.0f}%")

# =====================================================
# 7. DISPLAY PERFORMANCE TABLE
# =====================================================

print("\n========== EV PERFORMANCE RESULTS ==========")

print(
    f"{'Speed':>8} {'Rolling N':>12} {'Drag N':>12} "
    f"{'Total N':>12} {'Wheel kW':>12} "
    f"{'Motor kW':>12} {'Wh/km':>12} {'Range km':>12}"
)

print("-" * 105)

for i in range(len(speeds)):
    print(
        f"{speeds[i]:8.0f}"
        f"{rolling_forces[i]:12.2f}"
        f"{aero_forces[i]:12.2f}"
        f"{total_forces[i]:12.2f}"
        f"{wheel_powers[i]:12.2f}"
        f"{motor_powers[i]:12.2f}"
        f"{consumptions[i]:12.2f}"
        f"{ranges[i]:12.2f}"
    )

# =====================================================
# 8. PROFESSIONAL GRAPH STYLE
# =====================================================

plt.style.use("dark_background")

def style_graph(ax, title, xlabel, ylabel):
    ax.set_facecolor("#182630")
    ax.set_title(
        title,
        fontsize=15,
        fontweight="bold",
        color="white",
        pad=18
    )
    ax.set_xlabel(xlabel, fontsize=11, color="white")
    ax.set_ylabel(ylabel, fontsize=11, color="white")
    ax.tick_params(axis="both", colors="white")
    ax.grid(True, linestyle="--", alpha=0.30)

    ax.spines["bottom"].set_color("#00D9FF")
    ax.spines["left"].set_color("#00D9FF")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

def plot_ev_graph(values, title, ylabel, color, unit):
    fig, ax = plt.subplots(figsize=(11, 6))
    fig.patch.set_facecolor("#101820")

    ax.plot(
        speeds,
        values,
        color=color,
        linewidth=3,
        marker="o",
        markersize=8,
        markeredgecolor="white",
        label=ylabel
    )

    style_graph(
        ax,
        title,
        "Vehicle Speed (km/h)",
        ylabel
    )

    ax.legend(facecolor="#263746", edgecolor=color)

    # Display calculated values above each point
    for x, y in zip(speeds, values):
        ax.annotate(
            f"{y:.1f} {unit}",
            (x, y),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
            fontsize=9,
            color=color
        )

    plt.tight_layout()

# =====================================================
# 9. GRAPH 1: ENERGY CONSUMPTION VS SPEED
# =====================================================

plot_ev_graph(
    consumptions,
    "EV ENERGY CONSUMPTION vs VEHICLE SPEED",
    "Battery Energy Consumption (Wh/km)",
    "#00D9FF",
    "Wh/km"
)

# =====================================================
# 10. GRAPH 2: ESTIMATED RANGE VS SPEED
# =====================================================

plot_ev_graph(
    ranges,
    "EV ESTIMATED RANGE vs VEHICLE SPEED",
    "Estimated Range (km)",
    "#FFB000",
    "km"
)

# =====================================================
# 11. GRAPH 3: WHEEL POWER VS SPEED
# =====================================================

plot_ev_graph(
    wheel_powers,
    "EV WHEEL POWER vs VEHICLE SPEED",
    "Wheel Power (kW)",
    "#55E88B",
    "kW"
)

# =====================================================
# 12. GRAPH 4: Rolling resistance and aerodynamic drag vs speed
# =====================================================

# 12. GRAPH 4: Rolling resistance and aerodynamic drag vs speed
# ============================================================


# =====================================================
# 12. GRAPH 4: Rolling Resistance and Aerodynamic Drag
# =====================================================


fig4, ax4 = plt.subplots(figsize=(11, 6))
fig4.patch.set_facecolor("#101820")
ax4.set_facecolor("#182630")

ax4.plot(
    speeds,
    rolling_forces,
    color="#00D9FF",
    linewidth=3,
    marker="o",
    markersize=8,
    label="Rolling Resistance"
)

ax4.plot(
    speeds,
    aero_forces,
    color="#FFB000",
    linewidth=3,
    marker="s",
    markersize=8,
    label="Aerodynamic Drag"
)

style_graph(
    ax4,
    "ROLLING RESISTANCE AND AERODYNAMIC DRAG vs SPEED",
    "Vehicle Speed (km/h)",
    "Resistance Force (N)"
)

ax4.legend(facecolor="#263746", edgecolor="white")
fig4.tight_layout()


# Display all four graphs
plt.show()
