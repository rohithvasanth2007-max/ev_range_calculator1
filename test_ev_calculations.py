
from ev_engineering_suite import (
    rolling_resistance,
    aerodynamic_drag,
    acceleration_force,
    grade_resistance,
    battery_pack,
    estimated_range,
)


def test_rolling_resistance():
    assert abs(rolling_resistance(1500, 0.012) - 176.58) < 0.01


def test_aerodynamic_drag():
    result = aerodynamic_drag(1.225, 0.28, 2.2, 20)
    assert abs(result - 150.92) < 0.01


def test_acceleration_force():
    assert acceleration_force(1500, 2) == 3000


def test_grade_resistance():
    result = grade_resistance(1500, 5)
    assert abs(result - 1282.4968) < 0.01


def test_battery_pack():
    voltage, capacity, energy = battery_pack(108, 10, 3.7, 5)

    assert abs(voltage - 399.6) < 0.01
    assert abs(capacity - 50) < 0.01
    assert abs(energy - 19.98) < 0.01


def test_estimated_range():
    result = estimated_range(19.98, 0.9, 150)
    assert abs(result - 119.88) < 0.01


if __name__ == "__main__":
    tests = [
        test_rolling_resistance,
        test_aerodynamic_drag,
        test_acceleration_force,
        test_grade_resistance,
        test_battery_pack,
        test_estimated_range,
    ]

    for test in tests:
        test()
        print(f"PASS: {test.__name__}")

    print("\nAll 6 engineering tests passed!")