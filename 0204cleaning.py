import numpy as np
import pandas as pd

import matplotlib
import matplotlib.pyplot as pp

billboard = pd.read_csv('billboard.csv', encoding='latin-1')
print(billboard.head())

print(billboard.columns)
pp.plot(billboard.loc[0, 'x1st.week':'x67th.week'])
pp.savefig('foo.png')

# for index, row in billboard.iterrows():
#     pp.plot(range(1,77), row['x1st.week': 'x76th.week'], color='C0', alpha=0.1)
#     pp.savefig('foo2.png')

bshort = billboard[['artist.inverted', 'track', 'time', 'date.entered', 'x1st.week', 'x2nd.week', 'x3rd.week']]
print(bshort.head())

bshort.columns = ['artist', 'track', 'time', 'date', 'x1st', 'x2nd', 'x3rd']
print(bshort.head())

bmelt = bshort.melt(['artist', 'track', 'time', 'date'],['wk1', 'wk2', 'wk3'],'week', 'rank')
print(bmelt.head())
