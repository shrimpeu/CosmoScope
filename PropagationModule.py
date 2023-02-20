import matplotlib.pyplot as plt
from matplotlib import *
from SimulationParameters import * 


"""
function that returns the position and velocity of a celestial body
at a given time (ref_time) from NASA SPICE files. The position and
velocity are returned as arrays of length 3.
"""
def Ephemeris(ref_time,body):
    
    #-------------------------------------------------------------------------
    # INPUT
    # body : name of the body (type string)
    # ref_time : time from when the ephemeris is taken
    #-------------------------------------------------------------------------
    # OUPUT
    # (pos,vel) : a tuple where index 0 is x,y,z of position (np array) and 
    #             index 1 is x,y,z of velocity (np array) of the body obtained 
    #             at time ref_time from NASA SPICE files
    #-------------------------------------------------------------------------


    '''
    obtain the position and velocity of the body from the SPICE files
    spkezr() returns a tuple whose 0-th element is a state vector.
    slice the state vector to obtain the position and velocity vectors.
    '''
    pos_list = spice.spiceypy.spkezr(body,ref_time,'J2000','NONE','SUN')[0][0:3]
    pos_matrix = np.array([ [pos_list[0], pos_list[1],pos_list[2]] ])
    
    vel_list = spice.spiceypy.spkezr(body,ref_time,'J2000','NONE','SUN')[0][3:6]
    vel_matrix = np.array([ [vel_list[0], vel_list[1],vel_list[2]] ])
    
    return (pos_matrix,vel_matrix)


'''
function that returns the acceleration of each celestial body in the
system. The acceleration is returned as an array of length 3.
'''
def NbodyProblem(pos, mass):
    
    #-----------------------------------------------------------------
    # INPUT
    # pos  : positions matrix size (N,3) 
    #        where each row i corresponds to the x,y,z coordinate of 
    #        one celestial body of the Solar System.
    # mass : masses matrix  (1,N)
    #        each row is the mass (kg) of one celestial body of the
    #        Solar System.
    # G    : Newton's Gravitational constant
    #-----------------------------------------------------------------
    # OUTPUT
    # acc  : accelerations matrix (N,3)
    #        where each row i corresponds to the ax,ay,az  
    #        accelerations of one celestial body of the Solar System.
    #-----------------------------------------------------------------
    
    global G

    # extract x,y,z coordinates from position matrix
    x = [row[0] for row in pos] # x element of position matrix
    y = [row[1] for row in pos] # y element of position matrix
    z = [row[2] for row in pos] # x element of position matrix
    acc = np.empty((0,3))   # initialize empty array to hold accelerations

    # iterate over each celestial body
    for j in range (0,len(x)):
        ax=0
        ay=0
        az=0
        # iterate over each other celestial body
        for i in range (0,len(x)):
            if (i!=j):
                # calculate distance between the two celestial bodies
                dx = x[i]-x[j]
                dy = y[i]-y[j]
                dz = z[i]-z[j]
                norm = np.sqrt(dx**2+dy**2+dz**2)

                # calculate acceleration due to gravity
                ax += (G*mass[i]*1e-9*dx)/norm**3
                ay += (G*mass[i]*1e-9*dy)/norm**3
                az += (G*mass[i]*1e-9*dz)/norm**3
                
        a = np.array([ax,ay,az])
        acc = np.append(acc,[a],axis=0)
        
    return acc



def Energy(pos, vel, mass):
    
    #----------------------------------------------------------------------
    # INPUT
    # pos : positions matrix size (N,3). 
    # vel : velocities matrix size (N,3).
    # mass : masses matrix (1,N).
    #----------------------------------------------------------------------
    # OUTPUT
    # (E_kinetic,E_potential) : returns a tuple containing the kinetic
    #                           and potential energies of the given system.
    #----------------------------------------------------------------------
    
    global G

    # Extract the x, y, and z elements from the velocity and position matrices
    vx = [row[0] for row in vel] # x element of velocity matrix
    vy = [row[1] for row in vel] # y element of velocity matrix
    vz = [row[2] for row in vel] # z element of velocity matrix 
    x = [row2[0] for row2 in pos] # x element of position matrix
    y = [row2[1] for row2 in pos] # y element of position matrix
    z = [row2[2] for row2 in pos] # z element of position matrix

    # Initialize the kinetic and potential energy variables
    E_kinetic = 0
    E_potential = 0

    # Loop over each particle in the system
    for j in range (0,len(vx)):
              
        norm = np.sqrt(vx[j]**2+vy[j]**2+vz[j]**2)  # Calculate the speed (magnitude of velocity) of the particle
        E_kinetic += (1/2) * mass[j] * norm**2  # Calculate the kinetic energy of the particle and add it to the total

        # Loop over all other particles in the system
        for i in range (0,len(x)):
            if (i!=j):
                # Calculate the distance between particle i and particle j
                dx = x[i]-x[j]
                dy = y[i]-y[j]
                dz = z[i]-z[j]
                norm2 = np.sqrt(dx**2+dy**2+dz**2)

                # Calculate the potential energy between particle i and particle j and add it to the total
                E_potential += (G*mass[i]*mass[j]*1e-9)/norm2

    # Return a tuple containing the kinetic and potential energies of the system
    return (E_kinetic,E_potential)



def leapfrog(pos0, vel0, mass):
    
    #-------------------------------------------------------------------
    # INPUT
    # pos0 : initial positions matrix size (N,3). 
    # vel0 : initial velocities matrix size (N,3).
    # mass : masses matrix (1,N).
    # dt   : timestep.
    #-------------------------------------------------------------------
    # OUTPUT
    # pos_register : dictionnary of all positions matrix size (N,3)
    #                found by leapfrog or Stormer-Verlet integration 
    #                method at each time of the simulation.
    # vel_register : dictionnary of all velocities matrix size (N,3)
    #                found by leapfrog or Stormer-Verlet integration 
    #                method at each time of the simulation.
    #-------------------------------------------------------------------
    
    global G, t_start, t_end, dt
 
    pos_register = {}
    vel_register = {}
    
    pos = pos0  # initial position
    vel = vel0  # initial velocity
    acc = NbodyProblem(pos,mass)    # calculate initial acceleration

    # kick-drift-kick version
    for t in np.arange(t_start, t_end, dt): # iterate over time range with given timestep

        vel = vel + acc * dt * 0.5       # kick
        pos = pos + vel * dt             # drift
        
        acc = NbodyProblem(pos,mass)     # update acceleration
        vel = vel + acc * dt * 0.5       # kick
        
        pos_register[t] = pos            # save in the positions register
        vel_register[t] = vel            # save in the velocities register
        
    return (pos_register,vel_register)



def EnergyOverTime(pos_register,vel_register,mass):
    
    #-------------------------------------------------------------------
    # INPUT
    # pos_register : dictionnary of all positions matrix size (N,3)
    #                at each time of the simulation.
    # vel_register : dictionnary of all velocities matrix size (N,3)
    #                at each time of the simulation.
    #-------------------------------------------------------------------
    # OUTPUT
    # _time : list containing the time ranging from t_start to t_end, 
    #         with step equal to dt.
    # _KE   : list containing the kinetic energies of the system at each 
    #         time t in Lt.
    # _PE   : list containing the potential energies of the system at each 
    #         time t in Lt.
    # _TOT  : list containing the total energies of the system at each 
    #         time t in Lt.
    #-------------------------------------------------------------------
    
    global G, t_start, t_end, dt
    
    _time = []
    _KE = []
    _PE = []
    _TOT = []
    
    for t in np.arange(t_start, t_end, dt): 
        
        pos = pos_register[t]
        vel = vel_register[t]
        
        E_kinetic, E_potential = Energy(pos,vel,mass)
        E_total = E_kinetic - E_potential
        
        _time.append(t)
        _KE.append(E_kinetic)
        _PE.append(E_potential)
        _TOT.append(E_total)
        
    return (_time, _KE, _PE, _TOT)       



def Coordinates(register, body_id):
    
    #----------------------------------------------------------------
    # INPUT
    # register : Dictionary containing all the positions matrix 
    #            at all time t of the simulation.
    # body_id : identification number of the body, which corresponds 
    #           to the row number in the positions matrix. 
    #----------------------------------------------------------------
    # OUTPUT
    # (Lx,Ly,Lz) : 3 lists containig respectively all x, y and z
    #              values of the desired body (id_body).
    #----------------------------------------------------------------
    
    global t_start, t_end, dt
    
    Lx = []
    Ly = []
    Lz = []
    
    for t in np.arange(t_start, t_end, dt):
        matrix = register[t]
        Lx.append(matrix[body_id,0])
        Ly.append(matrix[body_id,1])
        Lz.append(matrix[body_id,2])
        
    return (Lx,Ly,Lz)



