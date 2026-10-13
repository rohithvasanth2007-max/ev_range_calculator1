# Python-Based Automotive and Electric Vehicle Engineering Calculators

## Project Overview

This project is a Python-based engineering calculation suite developed to understand fundamental automotive and electric vehicle (EV) performance parameters.

It combines basic engineering formulas, battery calculations, vehicle dynamics, power estimation, braking analysis, and graphical visualizations. The project helps demonstrate how automotive engineering principles can be implemented using Python.

The project is designed as a learning and portfolio project for students interested in automotive engineering, electric vehicles, and vehicle performance analysis.

## Project Objectives

- Understand fundamental automotive engineering calculations.
- Calculate EV battery pack specifications and estimated driving range.
- Analyse rolling resistance and aerodynamic drag.
- Estimate vehicle power requirements under different operating conditions.
- Visualize the relationship between vehicle speed, energy consumption, and performance.
- Develop practical Python programming skills for engineering applications.

## Key Features

- EV battery pack voltage and capacity calculations.
- Nominal and usable battery energy estimation.
- Estimated driving range calculation.
- Rolling resistance and aerodynamic drag analysis.
- Grade resistance and acceleration force calculations.
- Wheel power and estimated motor power calculations.
- Ideal braking distance estimation.
- Battery charging time estimation.
- Speed-based performance graphs.
- Basic calculation testing and validation.

## Technologies Used

- **Python** — engineering calculations and program logic.
- **Matplotlib** — graphical visualization.
- **Jupyter Notebook** — experimentation and learning.
- **Git and GitHub** — version control and project documentation.

## Engineering Formulas

The following fundamental equations are used for automotive and electric vehicle performance calculations.

### 1. Vehicle Resistance Forces

**Aerodynamic Drag**

`Fd = 0.5 × ρ × Cd × A × v²`

Calculates the resistance caused by air acting against a moving vehicle.

**Rolling Resistance**

`Frr = Crr × m × g`

Calculates the resistance caused by tyre deformation and contact with the road.

**Grade Resistance**

`Fg = m × g × sin(θ)`

Calculates the component of vehicle weight acting along an inclined road.

### 2. Vehicle Dynamics and Power

**Acceleration Force**

`Fa = m × a`

Calculates the force required to accelerate the vehicle.

**Total Tractive Force**

`Ft = Frr + Fd + Fg + Fa`

Estimates the total force required to move the vehicle under the modelled conditions.

**Wheel Power**

`Pw = Ft × v`

Calculates the mechanical power required at the wheels.

**Estimated Motor Power**

`Pm = Pw / η`

Estimates the required motor-side power based on drivetrain efficiency.

**Ideal Braking Distance**

`Distance = v² / (2 × μ × g)`

Estimates braking distance under simplified conditions, excluding driver reaction time.

### 3. EV Battery Calculations

**Battery Pack Voltage**

`Vpack = Ns × Vcell`

Calculates the nominal pack voltage using the number of cells connected in series.

**Battery Pack Capacity**

`Cpack = Np × Ccell`

Calculates the battery capacity using the number of parallel strings.

**Nominal Battery Energy**

`Energy (kWh) = Voltage (V) × Capacity (Ah) / 1000`

Estimates the nominal energy stored in the battery pack.

**Usable Battery Energy**

`Usable Energy (kWh) = Nominal Energy (kWh) × Usable Energy Fraction`

Estimates the energy available for driving after accounting for the selected usable-energy limit.

**Estimated Driving Range**

`Range (km) = Usable Energy (Wh) / Consumption (Wh/km)`

Estimates the driving range based on usable battery energy and energy consumption.

**Estimated Charging Time**

`Charging Time (hours) = Energy Added (kWh) / Effective Charging Power (kW)`

Provides a simplified estimate of battery charging time. Charging efficiency and charging-power limitations should be considered when implementing this calculation.

## Example EV Battery Configuration

The following example demonstrates a basic battery pack calculation.

| Parameter | Value |
|---|---:|
| Number of cells in series | 108 |
| Number of parallel strings | 10 |
| Nominal cell voltage | 3.7 V |
| Cell capacity | 5 Ah |
| Battery pack voltage | 399.6 V |
| Battery pack capacity | 50 Ah |
| Nominal battery energy | 19.98 kWh |
| Usable energy at 90% | 17.982 kWh |
| Assumed energy consumption | 150 Wh/km |
| Estimated range | 119.88 km |

**Note:** The estimated range assumes that 150 Wh/km represents battery-side energy consumption. Actual vehicle range depends on driving conditions, speed, temperature, payload, auxiliary loads, and energy losses.

## Project Files

The repository contains Python scripts and supporting files for different stages of development, calculations, testing, and visualization.

Main files include:

- `ev_engineering_suite.py` — automotive and EV engineering calculations.
- `ev_range_physics_graph.py` — physics-based EV energy consumption and range analysis.
- `ev_range_graph.py` — EV range graph experiments.
- `ev_range_graph_design.py` — graph design and visualization experiments.
- `test_ev_calculations.py` — calculation tests.
- `ev_calc.ipynb` — Jupyter Notebook experimentation.
- `ev_calc_ver1.py` and `ev_calc_version1.py` — earlier project versions.
- `Figure_1.png` and `Figure_2.png` — supporting graph images, where applicable.

Other experimental files and earlier versions are retained as part of the development process.

*Note: The filenames above describe their intended roles. Check each script for its actual functionality before relying on it.*

## How to Run the Project

### Requirements

Install Python 3 and the required libraries.

For graph generation, install Matplotlib:

```bash
pip install matplotlib
```

### Run the Engineering Calculator

Open a terminal in the project folder and run:

```bash
python ev_engineering_suite.py
```

### Run the EV Physics and Range Graphs

```bash
python ev_range_physics_graph.py
```

### Run the Calculation Tests

If the test file uses Python's built-in `unittest` framework, run:

```bash
python -m unittest test_ev_calculations.py
```

Run each command from the directory containing the corresponding file. The commands assume that the filenames and required dependencies match your current project.

## Assumptions and Limitations

The calculations are intended for educational purposes and use simplified engineering models.

- Vehicle resistance calculations may assume a flat road or constant road gradient.
- Range estimates depend on the energy-consumption model used.
- Battery usable energy is based on a selected usable-energy fraction.
- Motor power estimates depend on the efficiency value used.
- Ideal braking distance excludes driver reaction time and other real-world braking effects.
- Charging-time estimates do not fully represent real charging curves or battery-management-system limitations.
- The results are estimates and should not be treated as certified vehicle-design values.

## Future Improvements

Potential future developments include:

- Adding a graphical user interface.
- Including more detailed EV battery models.
- Comparing different battery configurations.
- Adding regenerative braking calculations.
- Studying the effects of vehicle mass and road gradient.
- Comparing energy consumption at different speeds.
- Improving automated tests and input validation.
- Adding further vehicle-performance plots and analysis.

## Learning Outcomes

Through this project, I am developing practical skills in:

- Python programming for engineering applications.
- Automotive vehicle dynamics fundamentals.
- Electric vehicle battery calculations.
- Energy consumption and driving-range estimation.
- Engineering formula implementation.
- Data visualization and technical analysis.
- Version control and GitHub project documentation.

## Author

**Rohith Vasanth**

Automobile Engineering Student

This project is part of my ongoing learning journey in automotive engineering, electric vehicles, and Python-based engineering applications.

---

*Disclaimer: This project is intended for educational and portfolio purposes. Its calculations are simplified estimates and should be validated before being used in real vehicle design or safety-critical applications.*