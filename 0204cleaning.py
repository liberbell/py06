import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as pp

billboard = pd.read_csv('billboard.csv', encoding='latin-1')
print(billboard.head())

print(billboard.columns)
pp.plot(range(1,77),billboard.loc[0, 'x1st.week':'x67th.week'])
pp.savefig('foo.png')
