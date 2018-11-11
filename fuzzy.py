import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import skfuzzy as fz
from skfuzzy import control as ctrl

# exec(open("filename.py").read())

# Custom scripts
import membership_funcs as mfs
import rule_gen as rg

# Run the computation
def get_washing_time(control, **kwargs):
	control_simulation = ctrl.ControlSystemSimulation(control)
	control_simulation.input['dirtiness'] = kwargs['dirtiness']
	control_simulation.input['dirt_type'] = kwargs['dirt_type']
	control_simulation.input['clothes_type'] = kwargs['clothes_type']
	control_simulation.compute()
	return control_simulation.output['washing_time']

# Plot a 3d surface 
def plot_surface(X, Y, Z, x_label, y_label, z_label='Wash Time'):
	# Plot dirtiness, dirt-type vs wash time
	fig = plt.figure()
	ax = plt.axes(projection='3d')
	ax.set_xlabel(x_label, fontsize=14)
	ax.set_ylabel(y_label, fontsize=14)
	ax.set_zlabel(z_label, fontsize=14)
	for label in (ax.get_xticklabels() + ax.get_yticklabels()):
		label.set_fontsize(16)
	ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap='viridis',edgecolor='none')
	

# Generate all input / output surface plots
def run_sim(control):
	num_points_per_input_val = 20
	clothes_type = np.linspace(0, 10, num_points_per_input_val)
	dirt_type = np.linspace(0, 10, num_points_per_input_val)
	dirtiness = np.linspace(0, 10, num_points_per_input_val)

	# Plot dirtiness and dirt-type
	X, Y = np.meshgrid(dirtiness, dirt_type)
	outputs = np.array([get_washing_time(control, dirtiness=x, dirt_type=y, clothes_type=5) for x, y in zip(np.ravel(X), np.ravel(Y))])
	Z = outputs.reshape(X.shape)
	plot_surface(X, Y, Z, 'Dirtyness', 'Dirt Type')

	# Plot dirtiness and clothes_type
	X, Y = np.meshgrid(dirtiness, clothes_type)
	outputs = np.array([get_washing_time(control, dirtiness=x, dirt_type=5, clothes_type=y) for x, y in zip(np.ravel(X), np.ravel(Y))])
	Z = outputs.reshape(X.shape)
	plot_surface(X, Y, Z, 'Dirtyness', 'Clothes Type')

	# Plot dirt_type and clothes_type
	X, Y = np.meshgrid(dirt_type, clothes_type)
	outputs = np.array([get_washing_time(control, dirtiness=5, dirt_type=x, clothes_type=y) for x, y in zip(np.ravel(X), np.ravel(Y))])
	Z = outputs.reshape(X.shape)
	plot_surface(X, Y, Z, 'Dirt Type', 'Clothes Type')

	plt.show()






# Input membership functions
membership_funcs = mfs.get_membership_functions(ctrl)
rules = rg.gen_rules(membership_funcs, ctrl)

# Create our controller
control = ctrl.ControlSystem(rules=rules)
print(get_washing_time(control, dirtiness=4, dirt_type=4, clothes_type=4))

run_sim(control)
