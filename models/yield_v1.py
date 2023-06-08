import numpy as np
from yggdrasil import units
from yggdrasil.languages.Python.YggInterface import YggRpcClient


def growth_rate(t, mass, LAI):
    # Initialize yggdrasil connection
    client = YggRpcClient("light_yield", global_scope=True)
    
    # Compute the light intercepted
    flag, light = client.call(t)
    if not flag:
        raise Exception("Error calling light model")

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
