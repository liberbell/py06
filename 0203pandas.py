import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as pp

# %matplotlib inline

planets = pd.read_csv('Planets2.csv')

print(planets)
planets = pd.read_csv('Planets2.csv', usecols=[0, 1, 2, 3])
print(planets)
print(planets['Mass'])

print(planets.Mass)
print(planets.index)
