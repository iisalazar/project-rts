class Basic:

	def getMean(self, data):
		# to check if all elements in list 'data' is an integer
		if self.__is_valid(data):
			value = 0
			for d in data:
				value += int(d)
			return (value / len(data))
		else:
			return ("Error! one element in list is not an integer")

	def getMedian(self, data):
		data.sort()
		
		if len(data)%2:
			# if the length of d is an odd number
			# returns the Nth element in d
			# N = (len(d) - 1) / 2 + 1
			# meaning it returns the middle element
			return data[(len(data)-1)/2]
		else:
			# if the length of d is an even number
			# returns mean between the (len(d)-1 / 2)th and ((len(d)-1 / 2)+1)th item in the list
			return (float(data[(len(data)-1) / 2 ] + data[(len(data)-1) / 2 + 1]) / 2)

	def getSum(self, data):
		summation = 0.0
		for d in data:
			summation += float(d)
		return float(summation)

	# a private method that checks if all items in a list is an integer
	def __is_valid(self, data):
		for d in data:
			if type(d) == int:
				pass
			else:
				return False
		return True