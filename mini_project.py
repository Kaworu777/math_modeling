import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation 

def moon_coord(R, v, t):
    alpha = v * np.pi / 180 * t 
    x = R * np.cos(alpha)
    y = R * np.sin(alpha) * 0.8
    return x, y

def animate(i):
    moon.set_data(moon_coord(8, 1, t=i))

if __name__ == "main":
    fig, ax = plt.subplots()
    plt.grid()
    plt.plot([0], [0], "o", ms=29, color="green")
    moon, = plt.plot([], [], "o", ms=7, color="grey")
    edge = 10 

    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig,
                        animate,
                        frames=360,
                        interval=20
                        )
    ani.save("Moon.gif")