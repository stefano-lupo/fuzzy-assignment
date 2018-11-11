import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import skfuzzy as fz
from skfuzzy import control as ctrl

# exec(open("filename.py").read())

# Custom scripts
import membership_funcs as mfs
import rule_gen as rg

def plotMfs():
	for x in mfs.get_membership_functions():
		x.view()
		input("Press enter to continue..")

# Get result of fuzzy logic model from inputs and model
def get_output_speed(control, input_values):
	zipped = list(zip(mfs.inputs, input_values))
	control_simulation = ctrl.ControlSystemSimulation(control)

	for pair in zipped:
		control_simulation.input[pair[0]] = pair[1]

	control_simulation.compute()
	return control_simulation.output[mfs.output]

# Run an entire simulation
def run_sim(control):
	num_points_per_input_val = 50
	clothes_type = np.linspace(1, 100, num_points_per_input_val)
	dirt_type = np.linspace(-4, 4, num_points_per_input_val)
	dirtiness = np.linspace(-4, 4, num_points_per_input_val)

	X, Y = np.meshgrid(temps, del_temps)
	output_speeds = np.array([get_output_speed(control, temp, del_temp) for temp, del_temp in zip(np.ravel(X), np.ravel(Y))])
	Z = output_speeds.reshape(X.shape)

	fig = plt.figure()
	ax = plt.axes(projection='3d')
	ax.set_xlabel('CPU Temp (°C)')
	ax.set_ylabel('Delta CPU Temp (°C)')
	ax.set_zlabel('Fan Speed (RPM)')
	ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap='viridis',edgecolor='none')

	plt.show()


# Input membership functions
membership_funcs = mfs.get_membership_functions(ctrl)
rules = rg.gen_rules(membership_funcs, ctrl)

# Create our controller
control = ctrl.ControlSystem(rules=rules)
print(get_output_speed(control, [4, 4, 4]))

#run_sim(control)
