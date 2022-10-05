import numpy as np
import matplotlib.pyplot as plt

# Create plots from point data
# Point data provided as an arbitrary number of C arguments
def polar_plot(*cVar):
    # Convert input string into a numpy array of floats
    points = np.array([float[x] for x in list(cVar[0][:-1].split(","))])
    x = []
    y = []
    pth = "../../plots/"

    # Parse point data and store in appropriate array
    for i in range(0, points.size):
        if i % 2:
            y.append(points[i])
        else:
            x.append(points[i])
    # Convert to numpy array for easier plotting
    y = np.array(y)
    x = np.array(x)

    # Set up the rectangular plot
    fig, ax = plt.subplots()
    ax.plot(x,y)
    ax.set_yticks(np.arange(0, 21, 1))
    ax.grid(True)
    ax.set_xlabel("Orientation")
    ax.set_ylabel("Elevation Angle")
    plt.title("Blockage Plot")
    plt.savefig(pth + "rec.png")

    # Set up the polar plot
    x = np.deg2rad(x) # convert to radians
    fig,ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(x,y)
    ymax = np.amax(y)
    ax.set_rticks(np.arange(-(ymax*.25), ymax, ymax*.25))
    ax.set_rlabel_position(-22.5)
    ax.grid(True)
    plt.title("Polar Blockage Plot")
    plt.savefig(pth + "pol.png")

    return 0