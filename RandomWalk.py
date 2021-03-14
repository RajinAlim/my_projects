#Required Third Party Modules is matplotlib

import random
from itertools import permutations
from matplotlib import pyplot as plt


class Walker:
    
    def __init__(self, axis=(500, 500), speed=1):
        self.current_pos = [axis[0] // 2, axis[1] // 2]
        self.axis = axis
        self.speed = speed
        self.force_positive = [0, 0]
        self.force_negative = [0, 0]
    
    def walk(self):
        if self.force_positive[0]:
            x_direction = self.speed
            self.force_positive[0] -= 1
        elif self.force_negative[0]:
            x_direction = -self.speed
            self.force_negative[0] -= 1
        else:
            x_direction = random.choice([self.speed, -self.speed])
        
        if self.force_positive[1]:
            y_direction = self.speed
            self.force_positive[1] -= 1
        elif self.force_negative[1]:
            y_direction = -self.speed
            self.force_negative[1] -= 1
        else:
            y_direction = random.choice([self.speed, -self.speed])
            
        if self.current_pos[0] < 0:
            x_direction = self.speed
            self.current_pos[0] = 0
            self.force_positive[0] = self.axis[0] // 10
        elif self.current_pos[0] > self.axis[0]:
            x_direction = -self.speed
            self.current_pos[0] = self.axis[0]
            self.force_negative[0] = self.axis[0] // 10
        
        if self.current_pos[1] < 0:
            self.force_positive[1] = self.axis[1] // 10
            y_direction = self.speed
            self.current_pos[1] = 0
        elif self.current_pos[1] > self.axis[1]:
            y_direction = -self.speed
            self.current_pos[1] = self.axis[1]
            self.force_negative[1] = self.axis[1] // 10
        
        self.current_pos[0] += x_direction
        self.current_pos[1] += y_direction

cmaps = "tab20", "Paired", "tab10", "Set1", "jet","brg", "nipy_spectral", "prism", "hsv", "winter", "plasma", 'YlOrRd', "inferno", "spring", "cool", "rainbow"
walker = Walker((250, 250))

plt.axis([0, 250, 0, 250])
plt.tick_params(labelsize=0, width=0, length=0)

count = 62500
x, y = [], []
for _ in range(count):
    walker.walk()
    x.append(walker.current_pos[0])
    y.append(walker.current_pos[1])

plt.scatter(x, y, s=1, c=range(count), cmap=random.choice(cmaps))
plt.show()

"""Project: Random Walk
Author: Rajin Alim
Completed On Sunday, 14 March 2020, 10:12 PM"""