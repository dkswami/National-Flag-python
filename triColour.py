from textwrap import fill
from turtle import color
import numpy as npy
from matplotlib import pyplot as pplot
from matplotlib import patches as patch

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

#24 spokes inside AshokChakra
for i in range(0,24):
    a = 6 + radius/2 * npy.cos(npy.pi*i/12 + npy.pi/48)
    b = 6 + radius/2 * npy.cos(npy.pi*i/12 - npy.pi/48)
    c = 4 + radius/2 * npy.sin(npy.pi*i/12 + npy.pi/48)
    d = 4 + radius/2 * npy.sin(npy.pi*i/12 - npy.pi/48)
    e = 6 + radius * npy.cos(npy.pi*i/12)
    f = 4 + radius * npy.sin(npy.pi*i/12)
    n.add_patch(patch.Polygon([[6,4],[a,c],[e,f],[b,d]], fill=True, closed=True, color='#000089ff'))

pplot.axis('equal')
pplot.show()