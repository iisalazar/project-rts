from .basic import Basic
from math import sqrt

class Dependent:
	pass

class Independent:

	def __init__(self):
		self.group1 = []
		self.group2 = []
		self.__basic = Basic()

	def add_elements(self, group1, group2):
		self.group1 = group1
		self.group2 = group2
		

	def get_mean(self):
		self.mean1 = self.__basic.get_mean(self.group1)
		self.mean2 = self.__basic.get_mean(self.group2)
		return {'mean1': self.mean1, 'mean2': self.mean2}

	def get_df(self):
		self.df = (len(self.group1) + len(self.group2)) - 2
		return {"df": self.df}

	def get_SS(self):
		sum_of_group1 = 0
		sum_of_group2 = 0
		sum_of_squared1 = 0 # just a holder
		sum_of_squared2 = 0 # just another holder


		# get the summation of group 1
		for data in self.group1:
			sum_of_group1 += data

		# get the summation of group 2
		for data in self.group2:
			sum_of_group2 += data

		# get the summation of group 1 squared
		for data in self.group1:
			sum_of_squared1 += (data) ** 2

		# get the summation of group 2 squared	
		for data in self.group2:
			sum_of_squared2 += (data) ** 2
		
		self.SS1 = sum_of_squared1 - float( (sum_of_group1 ** 2) / len(self.group1) )
		self.SS2 = sum_of_squared2 - float ( (sum_of_group2 ** 2) / len(self.group2) )
		
		return {
			"SS1": self.SS1, 
			"SS2": self.SS2
			}
		
	def get_t(self):
		t_value = abs(self.mean1 - self.mean2) / sqrt( ( (self.SS1 + self.SS2) / self.df ) * (1.0/len(self.group1) + 1.0/len(self.group2)))
		return {"t-computed": t_value}

