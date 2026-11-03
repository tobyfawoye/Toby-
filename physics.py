"""Common physics formulas in SI units."""


def speed(distance_m: float, time_s: float) -> float:
    """Return average speed in metres per second (distance / time)."""
    return distance_m / time_s


def acceleration(change_in_velocity_m_s: float, time_s: float) -> float:
    """Return acceleration in metres per second squared (change in velocity / time)."""
    return change_in_velocity_m_s / time_s


def force(mass_kg: float, acceleration_m_s2: float) -> float:
    """Return force in newtons (mass * acceleration)."""
    return mass_kg * acceleration_m_s2


def kinetic_energy(mass_kg: float, velocity_m_s: float) -> float:
    """Return kinetic energy in joules (0.5 * mass * velocity squared)."""
    return 0.5 * mass_kg * velocity_m_s**2


def gravitational_potential_energy(mass_kg: float, height_m: float,
                                   gravity_m_s2: float = 9.80665) -> float:
    """Return gravitational potential energy in joules (mass * gravity * height)."""
    return mass_kg * gravity_m_s2 * height_m
