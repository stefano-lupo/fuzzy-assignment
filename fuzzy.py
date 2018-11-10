import numpy as np
import skfuzzy as fz
from skfuzzy import control as ctrl

# Custom scripts
import membership_funcs as mfs

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

fan_control_simulation = ctrl.ControlSystemSimulation(fan_control)
fan_control_simulation.input['cpu_temp'] = 70
fan_control_simulation.input['del_cpu_temp'] = -1
fan_control_simulation.compute()
print (fan_control_simulation.output['fan_speed'])
fan_speed.view(sim=fan_control_simulation)


def plotMfs():
	for x in mfs.get_membership_functions():
		x.view()
		# input("Press enter to continue..")