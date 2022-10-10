import numpy as np

x = np.array([2,-1]);
h = np.array([-1,2,1]);

# Form the row and column vectors for the Toeplitz matrix
r = [h zeros(1, length(x) - 1)];
c = [h(1) zeros(1, length(x) - 1)];

# Toeplitz matrix
hConv = toeplitz(c,r)

#Compare the two types of convolutions
y1 = x*hConv
y2 = conv(x, h)