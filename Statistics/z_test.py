from statistics import mean
from math import sqrt

class one_sample:
	pass
# two-sample z -test ojbect
class two_sample:
	# whenever a two_sample object is instantiate, 
	# 2 new sets of groups are created

	def __init__(self):
		self.group1 = []
		self.group2 = []

	# input should be in a form of list
	def add_data(self, group1, group2):
		self.group1 = group1
		self.group2 = group2
		return(self.group1, self.group2)

	# get mean for two_sample
	def get_mean(self):
		self.mean1 = mean(self.group1)
		self.mean2 = mean(self.group2)
		return ("Mean for group1: {}\nMean for group2: {}".format(self.mean1, self.mean2))

	# get the variance
	def get_variance(self):

		holder1 = 0 # just a holder variable
		holder2 = 0 # another holder variable

		for data in self.group1:

			holder1 += (data - self.mean1) **2 # loops through the group and gets the summation of (x - mean) squared
			
		for data in self.group2:
			holder2 += (data - self.mean2) **2 # loops through the group and gets the summation of (x - mean) squared
			
		self.variance1 = holder1 / len(self.group1) # creates the global variance for group 1
		self.variance2 = holder2 / len(self.group2) # creates the global variance for group 2

		return(self.variance1, self.variance2)


	# getting the z value from the global variables
	# mean1, mean2, variance1, variance2,n1 and n2
	def get_z_value(self, tabular=0):
		z_computed = (self.mean1 - self.mean2) / sqrt((self.variance1 / len(self.group1) + (self.variance2 / len(self.group2))))
		return (z_computed)

	# a future method to gracefully print all the values computed
	def print_all(self):
		pass		
