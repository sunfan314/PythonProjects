import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values,s=1)
plt.show()