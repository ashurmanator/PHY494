# Heaviside step function
import matplotlib.pyplot as plt

def heaviside(x):
    """Heaviside step function"""

    if x < 0:
        theta = 0.
    elif x == 0:
        theta = 0.5
    else:
        theta = 1.

    return theta

x = 3
theta = theta = []

print("Theta(" + str(x) +") = " + str(theta))
xvalues = []
h = 0.5
xmin, xmax = -4, 4
x = xmin
while x <= xmax:
    xvalues.append(x)
    x += h
for i in xvalues:
    theta.append(heaviside(i))

plt.plot(xvalues, theta, '-o', color="red", linewidth=2)
plt.show()
