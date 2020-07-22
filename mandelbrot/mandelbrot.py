from __future__ import division
 
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
 
m = 1200
n = 800

if False:
  x_span = (-2, 1)
  y_span = (-1, 1)
else:
  x_span = (-1.3, -1.2)
  y_span = (-0.1, 0)

 
x = np.linspace(x_span[0], x_span[1], num=m).reshape((1, m))
y = np.linspace(y_span[0], y_span[1], num=n).reshape((n, 1))
C = np.tile(x, (n, 1)) + 1j * np.tile(y, (1, m))

 
Z = np.zeros((n, m), dtype=complex)
M = np.full((n, m), True, dtype=bool)
N = np.zeros((n, m))
for i in range(256):
    print "Computing ", i
    Z[M] = Z[M] * Z[M] + C[M]
    M[np.abs(Z) > 2] = False
    N[M] = i
 
# Turn the center black
N[N==255] = 0
N /= 50.0
 
# Save with Matplotlib using a colormap.
fig = plt.figure()
fig.set_size_inches(m / 100, n / 100)
ax = fig.add_axes([0, 0, 1, 1], frameon=False, aspect=1)
ax.set_xticks([])
ax.set_yticks([])
plt.imshow(np.flipud(N), cmap='nipy_spectral')
plt.show()
