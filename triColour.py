import numpy as np
from matplotlib import pyplot as py
import matplotlib.patches as patch

#Plotting the tri colours in national flag
a = patch.Rectangle((0,1), width=12, height=2, facecolor='green', edgecolor='grey')
b = patch.Rectangle((0,3), width=12, height=2, facecolor='white', edgecolor='grey')
c = patch.Rectangle((0,5), width=12, height=2, facecolor='#FF6103', edgecolor='grey')

m,n = py.subplots()
n.add_patch(a)
n.add_patch(b)
n.add_patch(c)

py.axis('equal')
py.show()