import numpy as np
import matplotlib.bezier as bezier
import matplotlib.pyplot as plt

# function to plot bezier curve
def plot_bezier_curve(curve, nTimes=1000):
    # curve: a bezier curve object
    # nTimes: number of points to plot
    x, y = np.array(curve.point_at_t(np.linspace(0,1,1000))).T
    plt.plot(x,y)