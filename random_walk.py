from matplotlib import pyplot
from random import choice

def steps(step_count=10000):
	steps_x = [0]
	steps_y = [0]
	size = int(40000 // step_count) 
	
	while len(steps_x) < step_count:
		x_direction = choice([-1, 1])
		x_distance = choice([0,1,2,3,4])
		x_step = x_distance * x_direction
		
		y_direction = choice([-1, 1])
		y_distance = choice([0,1,2,3,4])
		y_step = y_distance * y_direction
		
		if x_step == 0 and y_step == 0:
			continue
		x_step += steps_x[-1]
		y_step += steps_y[-1]
		steps_x.append(x_step)
		steps_y.append(y_step)
		
	return [steps_x, steps_y, size]

horizontal_steps, vertical_steps,size = steps()

pyplot.scatter(horizontal_steps, vertical_steps, c="black", edgecolor="none", s=size)
pyplot.axes().get_xaxis().set_visible(False)
pyplot.axes().get_yaxis().set_visible(False)
pyplot.figure(figsize=(10, 6))
pyplot.show()