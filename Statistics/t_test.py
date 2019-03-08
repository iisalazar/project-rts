from .basic import Basic
from math import sqrt
import pprint
class Dependent(Basic):
	def __init__(self):
		self.group1 = []
		self.group2 = []

	def add_elements(self, group1, group2):
		self.group1 = group1
		self.group2 = group2

	def get_difference(self):
		self.diff = 0.0
		self.diff_list = []
		self.diff_squared = 0.0
		self.diff_squared_list = []
		if len(self.group1) != len(self.group2):
			return {"error": "Length of both groups are not equal"}
		for i in range(len(self.group1)):
			buffer = self.group1[i] - self.group2[i]
			self.diff += float(buffer)
			self.diff_list.append(float(buffer))
			self.diff_squared += float(buffer ** 2)
			self.diff_squared_list.append(float(buffer))

	def get_t(self):
		try:
			self.get_difference()
			self.t = float( self.diff / len(self.group1) ) / sqrt ( float( float(self.diff_squared - float( (self.diff) ** 2 / len(self.group1) ) ) / ( (len(self.group1) - 1) * len(self.group1) ) ) )
			return self.t
		except ZeroDivisionError:
			self.t = "Infinity"
			return self.t

	def get_all_data(self):
		self.get_difference()
		self.get_t()
		data = {
			'Group 1' : self.group1,
			'Group 2' : self.group2,
			'N' : len(self.group1),
			'Difference (D)' : self.diff,
			'Difference Squared' : self.diff_squared,
			't_critical': self.t
		}
		return data


class Independent(Basic):

	def __init__(self):
		self.group1 = []
		self.group2 = []
		

	def add_elements(self, group1, group2):
		self.group1 = group1
		self.group2 = group2
		

	def get_mean(self):
		self.mean1 = self.getMean(self.group1)
		self.mean2 = self.getMean(self.group2)
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
		self.get_mean()
		self.get_df()
		self.get_SS()
		#  
		self.t_value = abs(self.mean1 - self.mean2) / sqrt( float( (self.SS1 + self.SS2) / self.df ) * float(1.0/len(self.group1)) + float(1.0/len(self.group2))  ) 
		return self.t_value

	def get_all_data(self):
		self.get_mean()
		self.get_df()
		self.get_SS()
		self.get_t()
		data = {
			'Group 1' : self.group1,
			'Group 2' : self.group2,
			'mean1' : self.mean1,
			'mean2' : self.mean2,
			'df' : self.df,
			'Sum of Squares 1' : self.SS1,
			'Sum of Squares 2' : self.SS2,
			't_critical' : self.t_value
		}
		return data