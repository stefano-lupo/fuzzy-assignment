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

def run_sample(membership_funcs):
	uni = np.arange(0, 121, 1)
	wt_med = fz.trimf(uni, [50, 60, 70])
	wt_long = fz.trimf(uni, [60, 80, 100])

	med_alpha = 0.25
	long_alpha = 0.5
	wt_med_alpha = [min(y, med_alpha) for y in wt_med]
	wt_long_alpha = [min(y, long_alpha) for y in wt_long]

	plt.plot(uni, wt_med, label='no cut')
	plt.plot(uni, wt_med_alpha, label='α = 0.25')
	plt.title('wash_time = medium, alpha cut, α = 0.25')
	plt.xlabel('Wash Time (mins)')
	plt.ylabel('Membership')
	plt.legend()
	plt.show()

	plt.plot(uni, wt_long, label='no cut')
	plt.plot(uni, wt_long_alpha, label='α = 0.5')
	plt.title('wash_time = long, alpha cut, α = 0.5')
	plt.xlabel('Wash Time (mins)')
	plt.ylabel('Membership')
	plt.legend()
	plt.show()

	combined = [max(x, y) for (x,y) in zip (wt_med_alpha, wt_long_alpha)]
	plt.plot(uni, combined, label='wash_time')
	plt.title('Composed Wash Time MF')
	plt.xlabel('Wash Time (mins)')
	plt.ylabel('Membership')
	plt.legend(loc='upper left')
	plt.show()





# Input membership functions
membership_funcs = mfs.get_membership_functions()

run_sample(membership_funcs)

# # # Read and build rules from rulese
# rules = rg.gen_rules(membership_funcs, ctrl)

# # # Create our controller
# control = ctrl.ControlSystem(rules=rules)

# # Do a sample calculation
# print(get_washing_time(control, dirtiness=4, dirt_type=4, clothes_type=4))

# # Generate surface plots
# run_sim(control)


