from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

xdata1 = []
ydata1 = []
D = 0.33
C = 0.3
x0 = 0.01
y0 = 0.01
xdata1.append(x0)
ydata1.append(y0)


def ggwp(i):
    xdata1.append(xdata1[i-1]**2 - ydata1[i-1]**2 + C)
    ydata1.append(2 * xdata1[i-1] * ydata1[i-1] + D) 
    kill.set_data(xdata1, ydata1)

if __name__ == "__main__":
    plt.axis("equal")
    fig, ax = plt.subplots()
    kill, = plt.plot([], [], "o", color="r", label="Ball")
    edge = 1 
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig,
                            ggwp,
                            frames=range(1, 50),
                            interval=200)
    ani.save("animation_4.gif")


