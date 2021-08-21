import numpy as np

class Agent:

	def __init__(self):
		self.value_function = {}
		with open('initial_value_states.txt', 'r') as f:
			for line in f:
				self.value_function[line[3:44:5]] = float(line[-5:-2])
