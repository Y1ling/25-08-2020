import matplotlib.pyplot as plt
from numpy import *

# create the lists of height and weight
height = [162, 170, 182, 173, 201, 185]
weight = [50, 55, 90, 63, 114, 84]

# draw the plot
plt.bar(height,weight, alpha=1)

# set x axis title
plt.xlabel('height(cm)')

# set axis title of y axis
plt.ylabel('weight(kg)')

# add the title for the plot
plt.title('height/weight plot')

# display the plot
plt.show()