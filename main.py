from Statistics import z_test
import sys


#two_sample.add_data(group1 = [1,2,3,4,5], group2 = [2,4,6,8,10])
#print(two_sample.get_mean())
#print(two_sample.get_variance())
#print(two_sample.get_z_value())


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

if __name__ == '__main__':
	main()