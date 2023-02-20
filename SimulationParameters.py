import numpy as np
import spiceypy as spice


spice.tkvrsn('TOOLKIT')
spice.furnsh('de440.bsp')
spice.furnsh('p10-a.bsp')
spice.furnsh('naif0012.tls')
 

#=======================================================================================================
#                                           Simulation parameters
#=======================================================================================================

t_start = spice.spiceypy.str2et('2007 Jan 02 00:00:00.0000')        # start time of the simulation

t_end = spice.spiceypy.str2et('2023 Jan 02 00:00:00.0000')          # end time of simulation

dt = 3*24*3600                                                        # timestep

G = 6.67430e-11                                                     # Newton's Gravitational Constant m3.kg-1.s-2

num_ts = int(np.ceil(t_end/dt))                                     # number of timesteps

#=======================================================================================================

