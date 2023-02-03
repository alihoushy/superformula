#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 16:01:34 2023

@author: ali.houshy
"""

import math
import matplotlib.pyplot as plt
import random

def superformula(a, b, m1, m2, n1, n2, n3, phi):
    r = ((math.cos(m1 * phi / 4) / a)**n2 + (math.sin(m2 * phi / 4) / b)**n3)**(-1 / n1)
    x = r * math.cos(phi)
    y = r * math.sin(phi)
    return x, y

def generate_shape(a, b, m1, m2, n1, n2, n3, filename):
    num_points = 1000
    phi = [2 * math.pi * i / num_points for i in range(num_points)]
    x, y = zip(*[superformula(a, b, m1, m2, n1, n2, n3, p) for p in phi])

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_aspect('equal')
    plt.savefig(filename)
    plt.close(fig)

def generate_filename(a, b, m1, m2, n1, n2, n3):
    return 'sp_' + str(a) + '_' + str(b) + '_' + str(m1) + '_' + str(m2) + '_' + str(n1) + '_' + str(n2) + '_' + str(n3) + '.png'

for i in range(1000):
    try:
        a = random.randint(-100, 100)
        b = random.randint(-100, 100)
        m1 = random.randint(-100, 100)
        m2 = random.randint(-100, 100)
        n1 = random.randint(-100, 100)
        n2 = random.randint(-100, 100)
        n3 = random.randint(-100, 100)
        generate_shape(a, b, m1, m2, n1, n2, n3, generate_filename(a, b, m1, m2, n1, n2, n3))
    except ZeroDivisionError:
        pass
    except OverflowError as e:
        pass
