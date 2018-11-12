from statistics import mean
from math import sqrt

class one_sample:
	pass

class two_sample:
	def __init__(self):
		self.group1 = []
		self.group2 = []

	def add_data(self, group1, group2):
		if len(group1) == len(group2):
			self.group1 = group1
			self.group2 = group2
		else:
			return "Error, group 1 and group 2 has unequal number of elements"

	def get_mean(self):
		self.mean1 = mean(self.group1)
		self.mean2 = mean(self.group2)
		return ("Mean for group1: {}\nMean for group2: {}".format(self.mean1, self.mean2))

	def get_variance(self):
		holder1 = 0
		holder2 = 0
		for data in self.group1:
			holder1 += (data - self.mean1) **2
			
		for data in self.group2:
			holder2 += (data - self.mean2) **2
			
		self.variance1 = holder1 / len(self.group1)
		self.variance2 = holder2 / len(self.group2)

		return(self.variance1, self.variance2)

	def get_z_value(self, tabular=0):
		z_computed = (self.mean1 - self.mean2) / sqrt((self.variance1 / len(self.group1) + (self.variance2 / len(self.group2))))
		return (z_computed)

	def print_all(self):
		pass		
