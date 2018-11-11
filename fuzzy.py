import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import skfuzzy as fz
from skfuzzy import control as ctrl

# exec(open("filename.py").read())

# Custom scripts
import membership_funcs as mfs

def plotMfs():
	for x in mfs.get_membership_functions():
		x.view()
		input("Press enter to continue..")

# Get result of fuzzy logic model from inputs and model
def get_output_speed(fan_control, temp, del_temp):
	fan_control_simulation = ctrl.ControlSystemSimulation(fan_control)
	fan_control_simulation.input['cpu_temp'] = temp
	fan_control_simulation.input['del_cpu_temp'] = del_temp
	fan_control_simulation.compute()
	return fan_control_simulation.output['fan_speed']

# Run an entire simulation
def run_sim(fan_control):
	num_points_per_input_val = 50
	temps = np.linspace(1, 100, num_points_per_input_val)
	del_temps = np.linspace(-4, 4, num_points_per_input_val)

	X, Y = np.meshgrid(temps, del_temps)
	output_speeds = np.array([get_output_speed(fan_control, temp, del_temp) for temp, del_temp in zip(np.ravel(X), np.ravel(Y))])
	Z = output_speeds.reshape(X.shape)

	fig = plt.figure()
	ax = plt.axes(projection='3d')
	ax.set_xlabel('CPU Temp')
	ax.set_ylabel('Delta CPU Temp')
	ax.set_zlabel('Fan Speed')
	ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap='viridis',edgecolor='none')





	# x = np.linspace(-6, 6, 2)
	# y = np.linspace(-6, 6, 2)
	# X, Y = np.meshgrid(x, y)
	# Z = f(X, Y)
	# print(Z)

	# fig = plt.figure()
	# ax = plt.axes(projection='3d')
	# ax.contour3D(X, Y, Z, 50, cmap='binary')
	# ax.set_xlabel('x')
	# ax.set_ylabel('y')
	# ax.set_zlabel('z')

	plt.show()


# Input membership functions
(cpu_temp, del_cpu_temp, fan_speed) = mfs.get_membership_functions()

# If CPU temp is low --> fan speed is okay low no matter what
low = ctrl.Rule(cpu_temp['l'], fan_speed['l'])

# If CPU temp medium and not rising --> leave at medium
med_not_rising = ctrl.Rule(cpu_temp['m'] & (del_cpu_temp['no_change'] | del_cpu_temp['cooling']), fan_speed['m'])

# If CPU temp is medium but rising --> set fan to fast
med_rising = ctrl.Rule(cpu_temp['m'] & del_cpu_temp['warming'], fan_speed['h'])

# If CPU temp is high but cooling --> set fan to mediun,
high_cooling = ctrl.Rule(cpu_temp['h'] & del_cpu_temp['cooling'], fan_speed['m'])

# If CPU temp is high but not cooling --> set fan to fast
high_not_cooling = ctrl.Rule(cpu_temp['h'] & (del_cpu_temp['no_change'] | del_cpu_temp['warming']), fan_speed['h'])

# Create our fan control using supplied rules and membership functions
fan_control = ctrl.ControlSystem([low, med_not_rising, med_rising, high_cooling, high_not_cooling])

run_sim(fan_control)
