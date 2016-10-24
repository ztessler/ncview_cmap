from __future__ import print_function
import sys
import numpy as np
import matplotlib.cm as cm

if len(sys.argv) > 1:
    cmap_name = sys.argv[1]
else:
    cmap_name = 'viridis'

cmap = getattr(cm, cmap_name)

for n in np.linspace(0.0, 1.0, 256):
    print('{} {} {}'.format(*map(int, np.array(cmap(n)[:3])*255)))
