import numpy as np
import spiceypy as spice


spice.tkvrsn('TOOLKIT')         # Print spiceypy toolkit version
'''
kernel files that contains information about the positions and velocities of 
astronomical bodies, as well as time conversion information.
'''
# Load the de440.bsp ephemeris file
spice.furnsh('de440.bsp')   # contains data on the positions and velocities of celestial bodies in the solar system

# Load the p10-a.bsp ephemeris file
spice.furnsh('p10-a.bsp')   # contains information on the orientation of the Earth

# Load the naif0012.tls leap seconds kernel file
spice.furnsh('naif0012.tls')    # This data adjusts UTC  in order to keep it synchronized with the rotation of the Earth
 

#=======================================================================================================
#                                           Simulation parameters
#=======================================================================================================

t_start = spice.spiceypy.str2et('2007 Jan 02 00:00:00.0000')        # start time of the simulation

t_end = spice.spiceypy.str2et('2023 Jan 02 00:00:00.0000')          # end time of simulation

dt = 3*24*3600                                                        # timestep

G = 6.67430e-11                                                     # Newton's Gravitational Constant m3.kg-1.s-2

num_ts = int(np.ceil(t_end/dt))                                     # number of timesteps

#=======================================================================================================

