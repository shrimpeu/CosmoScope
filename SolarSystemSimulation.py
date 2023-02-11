from matplotlib import animation

from SimulationParameters import *
from PropagationModule import *



def animate_func(i):

    #--------------------------------------------------------------------------------------
    # PROCEDURE
    # Animating the plot for real time results.
    #--------------------------------------------------------------------------------------
    ax.set_facecolor('black')            # Sets the color of imaginary square to black

    ax.clear()
    ax.set_axis_off()

    ax.scatter(0,0,0, s=150, c="yellow")
    ax.text(0,0,0,"Sun",color="white")

    ax.set_xlim3d([-Lx_neptune[-1], Lx_neptune[-1]])
    ax.set_ylim3d([-Ly_neptune[-1], Ly_neptune[-1]])
    ax.set_zlim3d([-Lz_neptune[-1], Lz_neptune[-1]])

    if timescale[i] <= t_end:

        ax.plot(Lx_mercury[:i+1],Ly_mercury[:i+1],Lz_mercury[:i+1],c="#ffffff",linewidth=1.2)
        ax.scatter(Lx_mercury[i],Ly_mercury[i],Lz_mercury[i], s=0.38,c='#808080', marker='o')
        ax.text(5+Lx_mercury[i],5+Ly_mercury[i],5+Lz_mercury[i],"Mercury",color="white")

        ax.plot(Lx_venus[:i+1],Ly_venus[:i+1],Lz_venus[:i+1],c="#E9ECAA",linewidth=1.2)
        ax.scatter(Lx_venus[i],Ly_venus[i],Lz_venus[i], s=10,c='#E9CA09', marker='o')
        ax.text(5+Lx_venus[i],5+Ly_venus[i],5+Lz_venus[i],"Venus",color="white")

        ax.plot(Lx_earth[:i + 1], Ly_earth[:i + 1], Lz_earth[:i + 1], c="#E9ECAA", linewidth=1.2)
        ax.scatter(Lx_earth[i], Ly_earth[i], Lz_earth[i], s=10.72, c='#0000ff', marker='o')
        ax.text(5 + Lx_earth[i], 5 + Ly_earth[i], 5 + Lz_earth[i], "Earth", color="white")

        ax.plot(Lx_mars[:i + 1], Ly_mars[:i + 1], Lz_mars[:i + 1], c="#E9ECAA", linewidth=1.2)
        ax.scatter(Lx_mars[i], Ly_mars[i], Lz_mars[i], s=10.72, c='#ff0000', marker='o')
        ax.text(5 + Lx_mars[i], 5 + Ly_mars[i], 5 + Lz_mars[i], "Mars", color="white")

        ax.plot(Lx_jupiter[:i+1],Ly_jupiter[:i+1],Lz_jupiter[:i+1], c="#EBC0B7",linewidth=1.2)
        ax.scatter(Lx_jupiter[i],Ly_jupiter[i],Lz_jupiter[i],s=70, c='#B3280A', marker='o')
        ax.text(5+Lx_jupiter[i],5+Ly_jupiter[i],5+Lz_jupiter[i],"Jupiter",color="white")

        ax.plot(Lx_saturn[:i+1],Ly_saturn[:i+1],Lz_saturn[:i+1],c="#BDB9AD",linewidth=1.2)
        ax.scatter(Lx_saturn[i],Ly_saturn[i],Lz_saturn[i],s=55.4, c='#7C5029', marker='o')
        ax.text(5+Lx_saturn[i],5+Ly_saturn[i],5+Lz_saturn[i],"Saturn",color="white")

        ax.plot(Lx_uranus[:i+1],Ly_uranus[:i+1],Lz_uranus[:i+1], c="#A2D2DC",linewidth=1.2)
        ax.scatter(Lx_uranus[i],Ly_uranus[i],Lz_uranus[i],s=30, c='#088F8F', marker='o')
        ax.text(5+Lx_uranus[i],5+Ly_uranus[i],5+Lz_uranus[i],"Uranus",color="white")

        ax.plot(Lx_neptune[:i+1],Ly_neptune[:i+1],Lz_neptune[:i+1], c="#BCE9BA",linewidth=1.2)
        ax.scatter(Lx_neptune[i],Ly_neptune[i],Lz_neptune[i],s=30, c='#118A0B', marker='o')
        ax.text(5+Lx_neptune[i],5+Ly_neptune[i],5+Lz_neptune[i],"Neptune",color="white")

        ax.set_title('TIME ' + spice.spiceypy.et2utc(timescale[i],"C", 3))

    else:

        simulation.event_source.stop()
        print("Simulation ended successfully.")

def anim_energ(i):

    ax2.clear()
    ax2.plot(timescale[:i+1],Ltot[:i+1])
    ax2.set_title('TIME ' + spice.spiceypy.et2utc(timescale[i],"C", 3))


#==================================================================
#                               MAIN
#==================================================================

# Initial positions and velocities using ephemeris at t_start

# Sun
sun_id = 0
pos_sun = Ephemeris(t_start,'SUN')[0]
vel_sun = Ephemeris(t_start,'SUN')[1]
m_sun = 1.989e30


# Mercury
mercury_id = 1
pos_mercury = Ephemeris(t_start,'MERCURY')[0]
vel_mercury = Ephemeris(t_start,'MERCURY')[1]
m_mercury = 0.330e24


# Mars
mars_id = 2
pos_mars = Ephemeris(t_start,'MARS BARYCENTER')[0]
vel_mars = Ephemeris(t_start,'MARS BARYCENTER')[1]
m_mars = 0.642e24


# Earth
earth_id = 3
pos_earth = Ephemeris(t_start,'EARTH')[0]
vel_earth = Ephemeris(t_start,'EARTH')[1]
m_earth = 5.97e24

# Venus
venus_id = 4
pos_venus = Ephemeris(t_start,'VENUS')[0]
vel_venus = Ephemeris(t_start,'VENUS')[1]
m_venus = 4.87e24


# Jupiter
jupiter_id = 5
pos_jupiter = Ephemeris(t_start,'JUPITER BARYCENTER')[0]
vel_jupiter = Ephemeris(t_start,'JUPITER BARYCENTER')[1]
m_jupiter = 1898e24

# Saturn
saturn_id = 6
pos_saturn = Ephemeris(t_start,'SATURN BARYCENTER')[0]
vel_saturn = Ephemeris(t_start,'SATURN BARYCENTER')[1]
m_saturn = 568e24

# Uranus
uranus_id = 7
pos_uranus = Ephemeris(t_start,'URANUS BARYCENTER')[0]
vel_uranus = Ephemeris(t_start,'URANUS BARYCENTER')[1]
m_uranus = 86.8e24

# Neptune
neptune_id = 8
pos_neptune = Ephemeris(t_start,'NEPTUNE BARYCENTER')[0]
vel_neptune = Ephemeris(t_start,'NEPTUNE BARYCENTER')[1]
m_neptune = 102e24



# Initial conditions mass, positions and velocities with ephemeris

mass = np.array([m_sun,m_mercury,m_mars,m_earth,m_venus,m_jupiter,m_saturn,m_uranus,m_neptune])

pos_init = np.concatenate((pos_sun,pos_mercury,pos_mars,pos_earth,pos_venus,pos_jupiter,pos_saturn,pos_uranus,pos_neptune),axis=0)

vel_init = np.concatenate((vel_sun,vel_mercury,vel_mars,vel_earth,vel_venus,vel_jupiter,vel_saturn,vel_uranus,vel_neptune),axis=0)



# Integration using the leapfrog integration (Störmer-Verlet method)

reg_pos, reg_vel = leapfrog(pos_init,vel_init,mass)


# Generating lists containing x,y,z position values of each bodies

Lx_mercury = Coordinates(reg_pos,1)[0]
Ly_mercury = Coordinates(reg_pos,1)[1]
Lz_mercury = Coordinates(reg_pos,1)[2]

Lx_mars = Coordinates(reg_pos,2)[0]
Ly_mars = Coordinates(reg_pos,2)[1]
Lz_mars = Coordinates(reg_pos,2)[2]

Lx_earth = Coordinates(reg_pos,3)[0]
Ly_earth = Coordinates(reg_pos,3)[1]
Lz_earth = Coordinates(reg_pos,3)[2]

Lx_venus = Coordinates(reg_pos,4)[0]
Ly_venus = Coordinates(reg_pos,4)[1]
Lz_venus = Coordinates(reg_pos,4)[2]

Lx_jupiter = Coordinates(reg_pos,5)[0]
Ly_jupiter = Coordinates(reg_pos,5)[1]
Lz_jupiter = Coordinates(reg_pos,5)[2]

Lx_saturn = Coordinates(reg_pos,6)[0]
Ly_saturn = Coordinates(reg_pos,6)[1]
Lz_saturn = Coordinates(reg_pos,6)[2]

Lx_uranus = Coordinates(reg_pos,7)[0]
Ly_uranus = Coordinates(reg_pos,7)[1]
Lz_uranus = Coordinates(reg_pos,7)[2]

Lx_neptune = Coordinates(reg_pos,8)[0]
Ly_neptune = Coordinates(reg_pos,8)[1]
Lz_neptune = Coordinates(reg_pos,8)[2]


# Animation show the evolution of bodies in the Solar System

#----------------------- 3D solar system figure

fig = plt.figure()

figManager = plt.get_current_fig_manager()
figManager.window.state('zoomed')          # maximize window automatically

ax = plt.axes(projection='3d')              # 3D plot


plt.rcParams['axes.facecolor'] = 'black'    # axes in black
plt.rcParams['text.color'] = 'black'        # texts in white
fig.set_facecolor('black')                  # black background

ax.view_init(elev=-89, azim=24)             # initial orientation of simulation

timescale = np.arange(t_start, t_end+2*dt, dt) # generating time scale

simulation = animation.FuncAnimation(fig, animate_func, interval=100, frames=abs(int(t_end)))

simu_energy = animation.FuncAnimation(fig, anim_energ, frames=abs(int(t_end)), interval=100)

plt.show()




