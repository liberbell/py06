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

print(planets.loc[0])
print(planets.set_index('Planet', inplace=True))

print(planets.info())
print(len(planets))

print(planets.loc['MERCURY':'EARTH'])
print(planets.columns)
