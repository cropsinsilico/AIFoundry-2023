import numpy as np
from yggdrasil import units


def growth_rate(t, mass, LAI):
    # Compute the light intercepted
    light = (LAI * units.add_units(4, 'erg/s')
             * ((mass / units.add_units(2500, 'g')) ** 0.33)
             * (0.5 + 0.5 * np.sin(2.0 * np.pi * np.floor(t)
                                   / units.add_units(1, 'yr')))
             * (0.5 + 0.5 * np.cos(2.0 * np.pi
                                   * ((t % 1.0) - units.add_units(12, 'hrs'))
                                   / units.add_units(1, 'day'))))

    # Compute the growth factor for the timestep based on the light
    # (pretend this is a biologically complex calculation)
    growth_rate = (light / units.add_units(2000.0, 'erg*day/s'))

    # Return output
    return growth_rate


def yield_curve(tstart, tend, tstep, mstart, LAI):
    t = tstart
    m = mstart
    times = []
    masses = []
    while t < tend:
        growth = growth_rate(t, m, LAI)
        m = m + growth * m * tstep
        times.append(t)
        masses.append(m)
        t += tstep
    times = np.array(times)
    masses = np.array(masses)
    return times, masses
