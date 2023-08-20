import numpy as np
import matplotlib.pyplot as plt
from numpy.random import default_rng
from scipy.stats import binom
import statistics

# Define a random number generator
rng = default_rng()

# 1
# Function simulating a fair match
def fair_match():
    match = rng.integers(0, 2, size=20)
    player_a = 0
    player_b = 0
    count = 0
    for i in match:
        if player_a == 10 or player_b == 10:
            break
        elif i == 1:
            player_a += 1
        else:
            player_b += 1
        count += 1
    return match[:count]

# 2
# Statistic: Difference between goals
# 3 Function calculating test statistics for a single match
def matchstat(match):
    return 20 - len(match)

# 4 Simulating matches
# For a thousand matches
simulation1 = []
for _ in range(1000):
    simulation1.append(matchstat(fair_match()))

# For ten thousand matches
simulation2 = []
for _ in range(10000):
    simulation2.append(matchstat(fair_match()))

# Modified functions for point 7
def fair_match2(goals=10):
    match = rng.integers(0, 2, size=2 * goals)
    player_a = 0
    player_b = 0
    count = 0
    for i in match:
        if player_a == goals or player_b == goals:
            break
        elif i == 1:
            player_a += 1
        else:
            player_b += 1
        count += 1
    return match[:count]

def matchstat2(match, goals):
    return 2 * goals - len(match)

# Simulation for point 7
simulation3 = []
for k in range(1, 101):
    sym = []
    for _ in range(10000):
        sym.append(matchstat2(fair_match2(k), k))
    simulation3.append(statistics.quantiles(sym, n=20, method='inclusive')[18])
