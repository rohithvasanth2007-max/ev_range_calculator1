
"""
Python-Based Automotive and Electric Vehicle Engineering Suite

Purpose:
    Perform simplified automotive force, power, braking,
    charging, battery-pack and EV-range calculations.

Units:
    Mass              : kg
    Speed             : km/h (converted internally to m/s)
    Force             : N
    Power             : kW
    Battery energy    : kWh
    Energy consumption: Wh/km

This is an educational model, not a validated vehicle-design tool.
"""

import math


# -------------------- CONSTANTS --------------------

GRAVITY = 9.81  # m/s^2


# -------------------- INPUT VALIDATION --------------------

def read_float(prompt: str, minimum: float | None = None) -> float:
    """Read a number and optionally enforce a minimum value."""

    while True:
        try:
            value = float(input(prompt))

            if not math.isfinite(value):
                print("Please enter a finite number.")
                continue

            if minimum is not None and value < minimum:
                print(f"Value must be at least {minimum}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def read_percentage(prompt: str, allow_zero: bool = False) -> float:
    """Read a percentage and return it as a decimal fraction."""

    minimum = 0 if allow_zero else 0.01

    while True:
        value = read_float(prompt, minimum)

        if value <= 100:
            return value / 100

        print("Percentage must not exceed 100.")


# -------------------- AUTOMOTIVE CALCULATIONS --------------------

def rolling_resistance(mass_kg: float,
                       coefficient: float) -> float:
    """Calculate rolling resistance force in newtons."""
    return coefficient * mass_kg * GRAVITY


def aerodynamic_drag(density: float,
                     drag_coefficient: float,
                     frontal_area: float,
                     speed_ms: float) -> float:
    """Calculate aerodynamic drag force in newtons."""
    return (
        0.5
        * density
        * drag_coefficient
        * frontal_area
        * speed_ms ** 2
    )


def acceleration_force(mass_kg: float,
                       acceleration_ms2: float) -> float:
    """Calculate force required for acceleration in newtons."""
    return mass_kg * acceleration_ms2


def grade_resistance(mass_kg: float,
                     angle_degrees: float) -> float:
    """Calculate grade force; uphill angle is positive."""
    angle_radians = math.radians(angle_degrees)
    return mass_kg * GRAVITY * math.sin(angle_radians)


def calculate_wheel_power(force_n: float,
                          speed_ms: float) -> float:
    """Calculate signed wheel power in kilowatts."""
    return force_n * speed_ms / 1000


def calculate_battery_power(wheel_power_kw: float,
                            efficiency: float) -> float:
    """Estimate battery power for positive traction power."""
    return max(0.0, wheel_power_kw) / efficiency


def braking_distance(speed_ms: float,
                     friction_coefficient: float) -> float:
    """Ideal level-road braking distance in metres."""
    if friction_coefficient == 0:
        raise ValueError("Friction coefficient must be above zero.")

    return speed_ms ** 2 / (
        2 * friction_coefficient * GRAVITY
    )


# -------------------- BATTERY CALCULATIONS --------------------

def battery_pack(series_cells: int,
                 parallel_strings: int,
                 cell_voltage: float,
                 cell_capacity_ah: float) -> tuple[float, float, float]:
    """Return pack voltage, capacity in Ah and energy in kWh."""

    pack_voltage = series_cells * cell_voltage
    pack_capacity_ah = parallel_strings * cell_capacity_ah
    pack_energy_kwh = (
        pack_voltage * pack_capacity_ah / 1000
    )

    return pack_voltage, pack_capacity_ah, pack_energy_kwh


def estimated_range(battery_energy_kwh: float,
                    usable_fraction: float,
                    consumption_wh_km: float) -> float:
    """Estimate range when consumption is measured at the battery."""

    usable_energy_wh = battery_energy_kwh * 1000 * usable_fraction
    return usable_energy_wh / consumption_wh_km


def charging_time(energy_added_kwh: float,
                  charger_power_kw: float,
                  charging_efficiency: float) -> float:
    """Estimate charging time in hours using average charger power."""

    return energy_added_kwh / (
        charger_power_kw * charging_efficiency
    )


# -------------------- MAIN PROGRAM --------------------

def main() -> None:
    print("\nAUTOMOTIVE & EV ENGINEERING CALCULATOR")
    print("=" * 45)

    print("\nVEHICLE INPUTS")
    mass = read_float("Vehicle mass (kg): ", 0.01)
    crr = read_float("Rolling resistance coefficient: ", 0)
    density = read_float("Air density (kg/m^3): ", 0)
    cd = read_float("Drag coefficient: ", 0)
    area = read_float("Frontal area (m^2): ", 0)
    speed_kmh = read_float("Vehicle speed (km/h): ", 0)
    acceleration = read_float("Acceleration (m/s^2): ")
    angle = read_float("Road angle (degrees; uphill +): ")

    efficiency = read_percentage(
        "Drivetrain efficiency (%): "
    )

    speed_ms = speed_kmh / 3.6

    # Calculate force components.
    f_rr = rolling_resistance(mass, crr)
    f_drag = aerodynamic_drag(density, cd, area, speed_ms)
    f_acc = acceleration_force(mass, acceleration)
    f_grade = grade_resistance(mass, angle)

    # Simplified signed force required at the wheels.
    f_total = f_rr + f_drag + f_acc + f_grade

    wheel_power_kw = calculate_wheel_power(
        f_total, speed_ms
    )
    battery_power_kw = calculate_battery_power(
        wheel_power_kw, efficiency
    )

    print("\nBATTERY PACK INPUTS")
    series = int(read_float("Cells in series: ", 1))
    parallel = int(read_float("Parallel strings: ", 1))
    cell_voltage = read_float("Nominal cell voltage (V): ", 0.01)
    cell_capacity = read_float("Cell capacity (Ah): ", 0.01)

    pack_v, pack_ah, pack_kwh = battery_pack(
        series, parallel, cell_voltage, cell_capacity
    )

    usable_fraction = read_percentage(
        "Usable battery energy (%): "
    )
    consumption = read_float(
        "Battery energy consumption (Wh/km): ", 0.01
    )
    range_km = estimated_range(
        pack_kwh, usable_fraction, consumption
    )

    print("\nCHARGING INPUTS")
    energy_added = read_float("Energy to add (kWh): ", 0.01)
    charger_power = read_float("Average charger power (kW): ", 0.01)
    charge_efficiency = read_percentage(
        "Charging efficiency (%): "
    )
    charge_hours = charging_time(
        energy_added, charger_power, charge_efficiency
    )

    print("\nRESULTS")
    print("=" * 45)
    print(f"Speed:                    {speed_ms:.2f} m/s")
    print(f"Rolling resistance:       {f_rr:.2f} N")
    print(f"Aerodynamic drag:         {f_drag:.2f} N")
    print(f"Acceleration force:       {f_acc:.2f} N")
    print(f"Grade resistance:         {f_grade:.2f} N")
    print(f"Total wheel force:        {f_total:.2f} N")
    print(f"Wheel power:              {wheel_power_kw:.2f} kW")
    print(f"Estimated battery power:  {battery_power_kw:.2f} kW")
    print("-" * 45)
    print(f"Battery pack voltage:     {pack_v:.2f} V")
    print(f"Battery pack capacity:    {pack_ah:.2f} Ah")
    print(f"Nominal battery energy:   {pack_kwh:.2f} kWh")
    print(f"Estimated range:          {range_km:.2f} km")
    print(f"Estimated charging time:  {charge_hours:.2f} hours")
    print("=" * 45)
    print("Note: Results use simplified engineering assumptions.")


if __name__ == "__main__":
    main()