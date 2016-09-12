import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

verts = [
    (9, 11), # left, bottom
    (7, 9), # left, top
    (7, 15), # right, top
    (6, 14), # right, bottom
    (5, 15), # ignored
    (3, 13),
    (5, 12),
    (4, 8),
    (2, 10),
    (1, 5),
    (3, 3),
    (5, 4),
    (7, 1),
    (7, 7),
    (8, 6),
    (9, 11),
    ]

codes = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]

path = Path(verts, codes)

fig = plt.figure()
ax = fig.add_subplot(111)
patch = patches.PathPatch(path, facecolor='orange', lw=2)
ax.add_patch(patch)
ax.set_xlim(-2,20)
ax.set_ylim(-2,20)
plt.show()