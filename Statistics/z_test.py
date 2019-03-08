from .basic import Basic
from math import sqrt
import pprint

class one_sample:
	pass
# two-sample z -test ojbect
class two_sample(Basic):
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
		self.mean1 = self.getMean(self.group1)
		self.mean2 = self.getMean(self.group2)
		return {"mean1": self.mean1, "mean2": self.mean2}
		#return ("Mean for group1: {}\nMean for group2: {}".format(self.mean1, self.mean2))

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
		try:
			self.z_computed = (self.mean1 - self.mean2) / sqrt((self.variance1 / len(self.group1) + (self.variance2 / len(self.group2))))
		except AttributeError:
			self.get_mean()
			self.get_variance()
			self.z_computed = (self.mean1 - self.mean2) / sqrt( float((float(self.variance1) / len(self.group1) ) + float(float(self.variance2) / len(self.group2)) ))
		return (self.z_computed)

	# a future method to gracefully print all the values computed
	def print_all(self):
		values = {
				'z-value': self.z_computed, 
				'variance for set 1' : self.variance1,
				'variance for set 2' : self.variance2,
				'mean for set 1' : self.mean1,
				'mean for set 2' : self.mean2,
				'Number of elements for set 1': len(self.group1),
				'Number of elements for set 2': len(self.group2),
		}
		pprint.pprint(values)

	def get_all_data(self):
		self.get_mean()
		self.get_variance()
		self.get_z_value()
		data = {
			'Group 1' : self.group1,
			'Group 2' : self.group2,
			'mean1' : self.mean1,
			'mean2' : self.mean2,
			'variance1' : self.variance1,
			'variance2' : self.variance2,
			'z_critical' : self.z_computed
		}
		return data