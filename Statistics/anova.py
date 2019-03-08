from .basic import Basic

class ANOVA(Basic):
	def __init__(self):
		# a list of data
		# contains objects
		self.data = []


	'''
		Data should be in list format
		E.g.
		[
			{ "label": "Group label", "data" : () },
			{ "label": "Group label", "data" : () },
			{ "label": "Group label", "data" : () },
			{ "label": "Group label", "data" : () },
			{ "label": "Group label", "data" : () },
		]
	'''
	def set_data(self, data):
		self.N = 0.0
		self.data = data
		for group in self.data:
			label = group.get('label')
			data_set = group.get('data')
			self.N += len(data_set)
			group['summation'] = self.getSum(data_set)
		return self.data, self.N

	def get_squares(self):
		squared_list = []
		for group in self.data:
			label = group.get('label')
			new_group = {
				"label" : label,
				"data" : []
			}
			for each_data in group.get('data'):
				new_group['data'].append(each_data ** 2)
			new_group['summation'] = self.getSum(data=new_group.get('data'))
			squared_list.append(new_group)

		self.squared_list = tuple(squared_list)
		return self.squared_list


	def getSST(self):
		# TODO: Change the variable names...
		
		self.sum_square_list = 0.0
		for data in self.squared_list:
			self.sum_square_list += data.get('summation')
		self.sum_list = 0.0
		for data in self.data:
			self.sum_list += data.get('summation')
		self.sum_list = (self.sum_list ** 2) / self.N
		self.SST = self.sum_square_list - self.sum_list
		return self.SST

	def getSSB(self):
		step1 = 0.0
		buffer = []
		for data in self.data:
			step1 += ( data.get('summation') ** 2 ) / len(data.get('data'))
			buffer.append(data.get('summation'))

		step2 = ( self.getSum(buffer) ** 2 ) / self.N
		self.SSB = step1 - step2
		return self.SSB

	
	def getSSW(self):
		self.SSW = self.SST - self.SSB
		return self.SSW

	def getDF(self):
		self.dfT = self.N - 1
		self.dfB = len(self.data) - 1
		self.dfW = self.dfT - self.dfB
		return (self.dfT, self.dfB, self.dfW)

	def getMS(self):
		self.MSB = float( self.SSB / self.dfB )
		self.MSW = float( self.SSW / self.dfW )
		return (self.MSB, self.MSW)

	def get_F(self):
		self.F = float( self.MSB / self.MSW )
		return self.F

	def get_all_data(self):
		try:
			data = {
				'data' : self.data,
				'squared data' : self.squared_list,
				'N' : self.N,
				'k / groups' : len(self.data),
				'SST' : self.SST,
				'SSB' : self.SSB,
				'SSW' : self.SSW,
				'df total' : self.dfT,
				'df between' : self.dfB,
				'df within' : self.dfW,
				'Mean Square Between' : self.MSB,
				'Mean Square Within' : self.MSW,
				'F critical' : self.F
			}
		except AttributeError:
			print("Error! calling all functions first")
			self.get_squares()
			self.getSST()
			self.getSSB()
			self.getSSW()
			self.getDF()
			self.getMS()
			self.get_F()
			data = {
				'data' : self.data,
				'squared data' : self.squared_list,
				'N' : self.N,
				'k / groups' : len(self.data),
				'SST' : self.SST,
				'SSB' : self.SSB,
				'SSW' : self.SSW,
				'df total' : self.dfT,
				'df between' : self.dfB,
				'df within' : self.dfW,
				'Mean Square Between' : self.MSB,
				'Mean Square Within' : self.MSW,
				'F critical' : self.F
			}
		return data