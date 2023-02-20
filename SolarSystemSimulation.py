from matplotlib import animation
import matplotlib.image as mpimg
from PropagationModule import *
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Load the image
img = mpimg.imread(r'C:\Users\Christian\CosmoScope\space_bg2.png')


# Define a function to animate the plot
def animate_func(i):
    # --------------------------------------------------------------------------------------
    # PROCEDURE
    # Animating the plot for real time results.
    # --------------------------------------------------------------------------------------

    ax.set_facecolor('none')             # Sets the color of imaginary square to black

    ax.clear()
    ax.set_axis_off()

    width = 1000
    border = 1500
    ax.set_position([border / width, 0, (width - border * 2) / width, 1])


    if timescale[i] <= t_end:
        fig.suptitle('TIME ' + spice.spiceypy.et2utc(timescale[i], "C", 3), fontsize=16)

        # Plot the Sun
        ax.scatter(0, 0, 0, s=150, c="yellow")
        ax.text(0, 0, 0, "Sun", color="white")

        # Plot Mercury
        ax.plot(Lx_mercury[:i + 1], Ly_mercury[:i + 1], Lz_mercury[:i + 1], c="#ffffff", linewidth=1.2)
        ax.scatter(Lx_mercury[i], Ly_mercury[i], Lz_mercury[i], s=1.38, c='#808080', marker='o')
        ax.text(5 + Lx_mercury[i], 5 + Ly_mercury[i], 5 + Lz_mercury[i], "Mercury", color="white", size=5)

        # Plot Venus
        ax.plot(Lx_venus[:i + 1], Ly_venus[:i + 1], Lz_venus[:i + 1], c="#E9ECAA", linewidth=1.2)
        ax.scatter(Lx_venus[i], Ly_venus[i], Lz_venus[i], s=10, c='#E9CA09', marker='o')
        ax.text(5 + Lx_venus[i], 5 + Ly_venus[i], 5 + Lz_venus[i], "Venus", color="white", size=5)

        # Plot Earth
        ax.plot(Lx_earth[:i + 1], Ly_earth[:i + 1], Lz_earth[:i + 1], c="#00FFFF", linewidth=1.2)
        ax.scatter(Lx_earth[i], Ly_earth[i], Lz_earth[i], s=10.72, c='#0000ff', marker='o')
        ax.text(5 + Lx_earth[i], 5 + Ly_earth[i], 5 + Lz_earth[i], "Earth", color="white", size=5)

        # Plot Mars
        ax.plot(Lx_mars[:i + 1], Ly_mars[:i + 1], Lz_mars[:i + 1], c="#FFC0CB", linewidth=1.2)
        ax.scatter(Lx_mars[i], Ly_mars[i], Lz_mars[i], s=10.5, c='#ff0000', marker='o')
        ax.text(5 + Lx_mars[i], 5 + Ly_mars[i], 5 + Lz_mars[i], "Mars", color="white", size=5)

        # Plot Jupiter
        ax.plot(Lx_jupiter[:i + 1], Ly_jupiter[:i + 1], Lz_jupiter[:i + 1], c="#d8ca9d", linewidth=1.2)
        ax.scatter(Lx_jupiter[i], Ly_jupiter[i], Lz_jupiter[i], s=70, c='#c99039', marker='o')
        ax.text(5 + Lx_jupiter[i], 5 + Ly_jupiter[i], 5 + Lz_jupiter[i], "Jupiter", color="white", size=5)

        # Plot Saturn
        ax.plot(Lx_saturn[:i + 1], Ly_saturn[:i + 1], Lz_saturn[:i + 1], c="#C5AB6E", linewidth=1.2)
        ax.scatter(Lx_saturn[i], Ly_saturn[i], Lz_saturn[i], s=55.4, c='#A49B72', marker='o')
        ax.text(5 + Lx_saturn[i], 5 + Ly_saturn[i], 5 + Lz_saturn[i], "Saturn", color="white", size=5)

        # Plot Uranus
        ax.plot(Lx_uranus[:i + 1], Ly_uranus[:i + 1], Lz_uranus[:i + 1], c="#BBE1E4", linewidth=1.2)
        ax.scatter(Lx_uranus[i], Ly_uranus[i], Lz_uranus[i], s=30, c='#93B8BE', marker='o')
        ax.text(5 + Lx_uranus[i], 5 + Ly_uranus[i], 5 + Lz_uranus[i], "Uranus", color="white", size=5)

        # Plot Neptune
        ax.plot(Lx_neptune[:i + 1], Ly_neptune[:i + 1], Lz_neptune[:i + 1], c="#6081FF", linewidth=1.2)
        ax.scatter(Lx_neptune[i], Ly_neptune[i], Lz_neptune[i], s=30, c='#3E54E8', marker='o')
        ax.text(5 + Lx_neptune[i], 5 + Ly_neptune[i], 5 + Lz_neptune[i], "Neptune", color="white", size=5)

        # Plot Pluto
        ax.plot(Lx_pluto[:i + 1], Ly_pluto[:i + 1], Lz_pluto[:i + 1], c="#ddc4af", linewidth=1.2)
        ax.scatter(Lx_pluto[i], Ly_pluto[i], Lz_pluto[i], s=0.38, c='#968570', marker='o')
        ax.text(5 + Lx_pluto[i], 5 + Ly_pluto[i], 5 + Lz_pluto[i], "Pluto", color="white", size=5)

        # Adjustes the distance of planets to the sun

        x_data = Coordinates(reg_pos, 4)[0]
        y_data = Coordinates(reg_pos, 4)[1]
        z_data = Coordinates(reg_pos, 4)[2]

        xmin = numpy.min(x_data)
        xmax = numpy.max(x_data)

        ymin = numpy.min(y_data)
        ymax = numpy.max(y_data)

        zmin = numpy.min(z_data)
        zmax = numpy.max(z_data)

        ax.set_xlim3d(xmin, xmax)
        ax.set_ylim3d(ymin, ymax)
        ax.set_zlim3d(zmin, zmax)

    else:

        simulation.event_source.stop()
        print("Simulation ended successfully.")



# Zoom function
def on_scroll(event):
    ax = event.inaxes
    if ax is not None:
        if event.button == 'up':
            # Zoom in
            ax.dist = max(ax.dist - 20, 0)
        elif event.button == 'down':
            # Zoom out
            ax.dist += 20

# ==================================================================
#                               MAIN
# ==================================================================

# Initial positions and velocities using ephemeris at t_start

# Sun
sun_id = 0
pos_sun = Ephemeris(t_start, 'SUN')[0]
vel_sun = Ephemeris(t_start, 'SUN')[1]
m_sun = 1.989e30

# Mercury
mercury_id = 1
pos_mercury = Ephemeris(t_start, 'MERCURY')[0]
vel_mercury = Ephemeris(t_start, 'MERCURY')[1]
m_mercury = 0.330e24

# Mars
mars_id = 2
pos_mars = Ephemeris(t_start, 'MARS BARYCENTER')[0]
vel_mars = Ephemeris(t_start, 'MARS BARYCENTER')[1]
m_mars = 0.642e24

# Earth
earth_id = 3
pos_earth = Ephemeris(t_start, 'EARTH')[0]
vel_earth = Ephemeris(t_start, 'EARTH')[1]
m_earth = 5.97e24

# Venus
venus_id = 4
pos_venus = Ephemeris(t_start, 'VENUS')[0]
vel_venus = Ephemeris(t_start, 'VENUS')[1]
m_venus = 4.87e24

# Jupiter
jupiter_id = 5
pos_jupiter = Ephemeris(t_start, 'JUPITER BARYCENTER')[0]
vel_jupiter = Ephemeris(t_start, 'JUPITER BARYCENTER')[1]
m_jupiter = 1898e24

# Saturn
saturn_id = 6
pos_saturn = Ephemeris(t_start, 'SATURN BARYCENTER')[0]
vel_saturn = Ephemeris(t_start, 'SATURN BARYCENTER')[1]
m_saturn = 568e24

# Uranus
uranus_id = 7
pos_uranus = Ephemeris(t_start, 'URANUS BARYCENTER')[0]
vel_uranus = Ephemeris(t_start, 'URANUS BARYCENTER')[1]
m_uranus = 86.8e24

# Neptune
neptune_id = 8
pos_neptune = Ephemeris(t_start, 'NEPTUNE BARYCENTER')[0]
vel_neptune = Ephemeris(t_start, 'NEPTUNE BARYCENTER')[1]
m_neptune = 102e24

# Pluto
pluto_id = 9
pos_pluto = Ephemeris(t_start, 'PlUTO BARYCENTER')[0]
vel_pluto = Ephemeris(t_start, 'PLUTO BARYCENTER')[1]
m_pluto = 0.322e24



# Initial conditions mass, positions and velocities with ephemeris

mass = np.array([m_sun, m_mercury, m_mars, m_earth, m_venus, m_jupiter, m_saturn, m_uranus, m_neptune, m_pluto])

pos_init = np.concatenate(
    (pos_sun, pos_mercury, pos_mars, pos_earth, pos_venus, pos_jupiter, pos_saturn, pos_uranus, pos_neptune, pos_pluto), axis=0)

vel_init = np.concatenate(
    (vel_sun, vel_mercury, vel_mars, vel_earth, vel_venus, vel_jupiter, vel_saturn, vel_uranus, vel_neptune, vel_pluto), axis=0)

# Integration using the leapfrog integration (Störmer-Verlet method)

reg_pos, reg_vel = leapfrog(pos_init, vel_init, mass)

# Generating lists containing x,y,z position values of each bodies

Lx_mercury = Coordinates(reg_pos, 1)[0]
Ly_mercury = Coordinates(reg_pos, 1)[1]
Lz_mercury = Coordinates(reg_pos, 1)[2]

Lx_mars = Coordinates(reg_pos, 2)[0]
Ly_mars = Coordinates(reg_pos, 2)[1]
Lz_mars = Coordinates(reg_pos, 2)[2]

Lx_earth = Coordinates(reg_pos, 3)[0]
Ly_earth = Coordinates(reg_pos, 3)[1]
Lz_earth = Coordinates(reg_pos, 3)[2]

Lx_venus = Coordinates(reg_pos, 4)[0]
Ly_venus = Coordinates(reg_pos, 4)[1]
Lz_venus = Coordinates(reg_pos, 4)[2]

Lx_jupiter = Coordinates(reg_pos, 5)[0]
Ly_jupiter = Coordinates(reg_pos, 5)[1]
Lz_jupiter = Coordinates(reg_pos, 5)[2]

Lx_saturn = Coordinates(reg_pos, 6)[0]
Ly_saturn = Coordinates(reg_pos, 6)[1]
Lz_saturn = Coordinates(reg_pos, 6)[2]

Lx_uranus = Coordinates(reg_pos, 7)[0]
Ly_uranus = Coordinates(reg_pos, 7)[1]
Lz_uranus = Coordinates(reg_pos, 7)[2]

Lx_neptune = Coordinates(reg_pos, 8)[0]
Ly_neptune = Coordinates(reg_pos, 8)[1]
Lz_neptune = Coordinates(reg_pos, 8)[2]

Lx_pluto = Coordinates(reg_pos, 9)[0]
Ly_pluto = Coordinates(reg_pos, 9)[1]
Lz_pluto = Coordinates(reg_pos, 9)[2]


# Animation show the evolution of bodies in the Solar System

# 3D solar system figure


# Adds a bg image
fig = plt.figure("Solar System simulation", dpi=150)
ax = fig.add_subplot(111, projection='3d')  # 3D plot
fig.figimage(img, alpha=0.3, resize='auto')

ax.set_facecolor('none')
ax.set_axis_off()

figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()

plt.rcParams['axes.facecolor'] = 'black'  # axes in black
plt.rcParams['text.color'] = 'white'  # texts in white
fig.set_facecolor('black')  # black background

ax.view_init(elev=-80, azim=-50)  # initial orientation of simulation
fig.canvas.mpl_connect('scroll_event', on_scroll)

timescale = np.arange(t_start, t_end + 2 * dt, dt)  # generating time scale

simulation = animation.FuncAnimation(fig, animate_func, interval=50, frames=abs(int(t_end)), blit=False)

plt.tight_layout()

plt.show()