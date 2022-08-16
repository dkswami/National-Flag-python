from textwrap import fill
import numpy as np
from matplotlib import pyplot as pplot
import matplotlib.patches as patch

#Plotting the tri colours in national flag
greenstrip = patch.Rectangle((0,1), width=12, height=2, facecolor='green', edgecolor='grey')
whitestrip = patch.Rectangle((0,3), width=12, height=2, facecolor='white', edgecolor='grey')
saffronstrip = patch.Rectangle((0,5), width=12, height=2, facecolor='#FF6103', edgecolor='grey')

m,n = pplot.subplots()
n.add_patch(greenstrip)
n.add_patch(whitestrip)
n.add_patch(saffronstrip)

#AshokChakra Circle in the middle strip
radius=0.8
pplot.plot(6,4, marker = 'o', markerfacecolor="#000089ff", markersize=9.5)
ashokchakra = pplot.Circle((6,4), radius, color='#000089ff', fill=False, linewidth=7)
n.add_artist(ashokchakra)

pplot.axis('equal')
pplot.show()