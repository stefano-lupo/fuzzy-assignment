import numpy as np
import skfuzzy as fz
from skfuzzy import control as ctrl

zero_ten_universe = np.arange(0, 11, 1)

inputs = ['clothes_type', 'dirt_type', 'dirtiness']
output = 'washing_time'

def get_membership_functions():
	return clothes_type_mf(), dirt_type_mf(), dirtiness_mf(), washing_time_mf()

def clothes_type_mf():
	clothes_type = ctrl.Antecedent(np.arange(0, 11, 1), 'clothes_type')
	clothes_type['silk'] = fz.trapmf(clothes_type.universe, [0, 0, 3, 5])
	clothes_type['woolen'] = fz.trimf(clothes_type.universe, [3, 5, 7])
	clothes_type['cotton'] = fz.trapmf(clothes_type.universe, [5, 8, 10, 10])
	return clothes_type

def dirt_type_mf():
	dirt_type = ctrl.Antecedent(np.arange(0, 11, 1), 'dirt_type')
	dirt_type['not_greasy'] = fz.trapmf(dirt_type.universe, [0, 0, 3, 5])
	dirt_type['medium'] = fz.trimf(dirt_type.universe, [3, 5, 7])
	dirt_type['greasy'] = fz.trapmf(dirt_type.universe, [5, 8, 10, 10])
	return dirt_type

def dirtiness_mf():
	dirtiness = ctrl.Antecedent(np.arange(0, 11, 1), 'dirtiness')
	dirtiness['low'] = fz.trapmf(dirtiness.universe, [0, 0, 3, 5])
	dirtiness['medium'] = fz.trimf(dirtiness.universe, [4, 5, 6])
	dirtiness['high'] = fz.trapmf(dirtiness.universe, [5, 8, 10, 10])
	return dirtiness

def washing_time_mf():
	washing_time = ctrl.Consequent(np.arange(0, 121, 1), 'washing_time')
	washing_time['very_short'] = fz.trapmf(washing_time.universe, [0, 0, 20, 40])
	washing_time['short'] = fz.trimf(washing_time.universe, [20, 40, 60])
	washing_time['medium'] = fz.trimf(washing_time.universe, [50, 60, 70])
	washing_time['long'] = fz.trimf(washing_time.universe, [60, 80, 100])
	washing_time['very_long'] = fz.trapmf(washing_time.universe, [80, 100, 120, 120])
	return washing_time

# clothes_type_mf().view()
# dirt_type_mf().view()
# dirtiness_mf().view()
# washing_time_mf().view()
# input("Enter.")