import numpy as np
import skfuzzy as fz
from skfuzzy import control as ctrl

def get_membership_functions():
	# return cpu_temp_mf(), cpu_usage_mf(), del_cpu_temp_mf(), fan_speed_mf()
	return cpu_temp_mf(), del_cpu_temp_mf(), fan_speed_mf()

def cpu_temp_mf():
	cpu_temp = ctrl.Antecedent(np.arange(0, 101, 1), 'cpu_temp')
	cpu_temp['l'] = fz.trapmf(cpu_temp.universe, [0, 0, 20, 40])
	cpu_temp['m'] = fz.trimf(cpu_temp.universe, [30, 55, 65])
	cpu_temp['h'] = fz.trapmf(cpu_temp.universe, [60, 80, 100, 100])
	return cpu_temp

# def cpu_usage_mf():
# 	cpu_usage = ctrl.Antecedent(np.arange(0, 101, 1), 'cpu_usage')
# 	cpu_usage['l'] = fz.trapmf(cpu_usage.universe, [0, 0, 25, 50])
# 	cpu_usage['m'] = fz.trimf(cpu_usage.universe, [40, 50, 65])
# 	cpu_usage['h'] = fz.trapmf(cpu_usage.universe, [60, 80, 100, 100])
# 	return cpu_usage

def del_cpu_temp_mf():
	del_cpu_temp = ctrl.Antecedent(np.arange(-4, 5, 1), 'del_cpu_temp')
	del_cpu_temp['cooling'] = fz.trapmf(del_cpu_temp.universe, [-4, -4, -2, 0])
	del_cpu_temp['no_change'] = fz.trimf(del_cpu_temp.universe, [-1, 0, 1])
	del_cpu_temp['warming'] = fz.trapmf(del_cpu_temp.universe, [0, 2, 4, 4])
	return del_cpu_temp

def fan_speed_mf():
	fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')
	fan_speed['l'] = fz.trapmf(fan_speed.universe, [0, 0, 20,40])
	fan_speed['m'] = fz.trimf(fan_speed.universe, [30, 50, 70])
	fan_speed['h'] = fz.trapmf(fan_speed.universe, [60, 80, 100, 100])
	return fan_speed