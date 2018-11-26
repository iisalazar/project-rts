from Statistics import z_test, basic, t_test
import sys
from pprint import pprint
'''
two_sample = z_test.two_sample()

two_sample.add_data(group1 = [1,2,3,4,5], group2 = [2,4,6,8,10])
print(two_sample.get_mean())
print(two_sample.get_variance())
print(two_sample.get_z_value())
'''
'''
def main():
	print("Project RTS - A minimal statistic calculator".center(10))
	while True:
		choice = int(input("Parametric statistical treatment to be used\n1. One-sample z-test\n2. Two-sample z-test\n3. T-test independent\n4. T-test dependent\n5. One-way ANOVA (WARNING: bloody path)\n6. Two-way ANOVA (WARNING!! bloody as hell)\n Choice: "))
		if choice == 1:
			pass
		elif choice == 2:
			two_sample = z_test.two_sample()
			two_sample.add_data(group1 = [1,2,3,4,5], group2 = [2,4,6,8,10])
			print(two_sample.get_mean())
			print(two_sample.get_variance())
			print(two_sample.get_z_value())
		elif choice == 3:
			pass
		elif choice == 4:
			pass
		elif choice == 5:
			pass
		elif choice == 6:
			pass
		else:
			print("Invalid input")
'''
if __name__ == '__main__':
	#basic = basic.Basic()
	#print(basic.get_median([1,2,3,4,5,6]))
	t_test_ind = t_test.Independent()

	t_test_ind.add_elements(group1=[1,2,3,4,5], group2=[6,7,8,9,10])
	mean = t_test_ind.get_mean()
	df = t_test_ind.get_df()
	SS = t_test_ind.get_SS()
	t_value = t_test_ind.get_t()
	print("Mean1 \t\t\t {}\nMean2 \t\t\t {}".format(mean['mean1'], mean['mean2']))
	print("Degrees of freedom \t {}".format(df['df']))
	print("Sum of squares 1 \t {}\nSum of squares 2 \t {}".format(SS['SS1'], SS['SS2']))
	print("computed t-value \t {}".format(t_value['t-computed']))
	



