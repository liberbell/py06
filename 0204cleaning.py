import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as pp

billboard = pd.read_csv('billboard.csv', encoding='latin-1')
print(billboard.head())

print(billboard.columns)
pp.plot(billboard.loc[0, 'x1st.week':'x67th.week'])
pp.savefig('foo.png')

for index, row in billboard.iterrows():
    pp.plot(range(1,77), row['x1st.week': 'x76th.week'], color='C0', alpha=0.1)
    pp.savefig('foo2.png')
