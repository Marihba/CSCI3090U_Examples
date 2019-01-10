# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 16:34:56 2018

@author: Randy J. Fortier

This code produces a plot of the Cardinal (Catmull-Rom) blending functions.
"""

import numpy as np
import matplotlib.pyplot as plt

def b0(t):
    return -0.5 * t + t**2 - 0.5 * t**3

def b1(t):
    return 1 - 2.5 * t**2 + 1.5 * t**3

def b2(t):
    return 0.5 * t + 2 * t**2 - 1.5 * t**3

def b3(t):
    return -0.5 * t**2 + 0.5 * t**3

ts = np.linspace(0.0, 1.0, 100)

b0vals = np.array([b0(t) for t in ts])
b1vals = np.array([b1(t) for t in ts])
b2vals = np.array([b2(t) for t in ts])
b3vals = np.array([b3(t) for t in ts])

p0 = plt.plot(ts, b0vals, 'r-')
p1 = plt.plot(ts, b1vals, 'g-')
p2 = plt.plot(ts, b2vals, 'b-')
p3 = plt.plot(ts, b3vals, 'k-')

plt.grid(True)
plt.legend([p0[0], p1[0], p2[0], p3[0]], ['-0.5 * t + t**2 - 0.5 * t**3', '1 - 2.5 * t**2 + 1.5 * t**3', '0.5 * t + 2 * t**2 - 1.5 * t**3', '-0.5 * t**2 + 0.5 * t**3'], loc=9)
plt.show()
