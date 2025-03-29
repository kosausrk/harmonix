import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

def harmonograph_3d(a1, a2, a3, f1, f2, f3, d1, d2, d3, p1, p2, p3, t_max=40, dt=0.005):
    """Generates a 3D harmonograph with more points for a dense pattern."""
    t = np.arange(0, t_max, dt)
    x = a1 * np.sin(f1 * t + p1) * np.exp(-d1 * t)
    y = a2 * np.sin(f2 * t + p2) * np.exp(-d2 * t)
    z = a3 * np.sin(f3 * t + p3) * np.exp(-d3 * t)
    return x, y, z

def plot_static_harmonograph_3d(x, y, z, title="Woven Harmonograph"):
    """Plots a static 3D harmonograph with desired aesthetics."""
    fig = plt.figure(figsize=(10, 10), facecolor='black') # Black background
    ax = fig.add_subplot(111, projection='3d', facecolor='black') # Black background
    ax.set_title(title, color='white')
    ax.set_xlabel("X", color='white')
    ax.set_ylabel("Y", color='white')
    ax.set_zlabel("Z", color='white')
    ax.grid(False)
    ax.plot(x, y, z, lw=0.8, color='white') # White lines, thinner linewidth
    ax.set_facecolor('black') # Set axes background to black
    ax.xaxis.set_pane_color((0.0, 0.0, 0.0, 0.0)) # Remove grid planes
    ax.yaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.zaxis.set_pane_color((0.0, 0.0, 0.0, 0.0))
    ax.tick_params(axis='x', colors='white') # Set tick colors to white
    ax.tick_params(axis='y', colors='white')
    ax.tick_params(axis='z', colors='white')
    plt.show()

if __name__ == "__main__":
    # Parameters to create a dense, woven pattern
    a1 = 15
    a2 = 12
    a3 = 10
    f1 = 2.03
    f2 = 3.05
    f3 = 4.07
    d1 = 0.02
    d2 = 0.03
    d3 = 0.04
    p1 = 0
    p2 = math.pi / 2
    p3 = math.pi / 4

    x, y, z = harmonograph_3d(a1, a2, a3, f1, f2, f3, d1, d2, d3, p1, p2, p3)
    plot_static_harmonograph_3d(x, y, z, "Woven Harmonograph")