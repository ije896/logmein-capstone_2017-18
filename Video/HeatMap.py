#!/usr/bin/env python

'''
Heat Map
====================
The Heat Map module plots a graph indicating user's movement
throughout a pre analyzed video. Some dummy data has been placed
in main() for demonstration
Usage
-----
HeatMap.py
----
ESC - exit
'''

import matplotlib.pyplot as plt
import seaborn as sns #potential library to plot heatmap
from matplotlib.colors import LogNorm
import numpy as np
import io
import os
import sys


class HeatMap:
    def __init__(self, coord_list):
        self.coords_and_time = coord_list #a tuple of x, y coord, sec
        self.x_coords = None
        self.y_coords = None
        self.x_times = None
        self.time_stamps = None
        self.x_range = 0
        self.y_range = 0

    def set_x_coords(self):
        self.x_coords = []
        for (x,y,time) in self.coords_and_time:
            self.x_coords.append(x)

    def set_y_coords(self):
        self.y_coords = []
        for (x,y,time) in self.coords_and_time:
            self.y_coords.append(y)

    def set_xrange(self, range):
        self.x_range = range

    def set_yrange(self, range):
        self.y_range = range

    def set_xtimes(self):
        self.x_times = []
        for (x,y,time) in self.coords_and_time:
            self.x_times.append([time,x])

    def plot(self):
        x_times = self.x_times
        plt.scatter(*zip(*x_times))
        plt.xlabel("Time (s)")
        plt.ylabel("x-coords")
        plt.show()


def main():
    test = [[573, 215, 0.03], [576, 238, 1.0], [572, 262, 2.01],
    [542, 317, 3.01], [610, 358, 4.02], [489, 369, 5.02], [415, 372, 6.02],
    [205, 301, 8.0], [205, 300, 8.03], [300, 292, 9.0], [401.5, 282.0, 10.01],
    [541, 249, 11.01], [733, 213, 12.02], [858, 179, 13.02], [899, 94, 14.02],
    [927.5, 83.5, 15.03], [801, 177, 16.0], [819, 271, 17.0], [766, 335, 18.01],
    [814, 348, 19.01], [839, 346, 20.01], [833, 346, 21.02], [799, 348, 22.02],
    [503, 325, 24.0], [367, 315, 25.0], [273, 315, 26.0], [258, 313, 27.01],
    [270, 299, 28.01], [298, 284, 29.02], [266, 312, 30.02], [310, 337, 31.02],
    [355, 303, 32.0], [522, 213, 33.0], [569.5, 103.5, 34.0], [635.5, 271.5, 35.01]]
    print(__doc__)
    app = HeatMap(test)
    app.set_x_coords()
    app.set_y_coords()
    app.set_xrange(900)
    app.set_yrange(500)
    app.set_xtimes()
    app.plot()

if __name__ == '__main__':
    main()
