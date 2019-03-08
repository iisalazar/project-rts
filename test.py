from Statistics.z_test import two_sample

z = two_sample()
z.add_data(group1=[1,2,3,4,5], group2=[6,7,8,9,10])
z.get_z_value()

from Statistics.t_test import Independent
t = Independent()
t.add_elements(group1=[1,2,3,4,5], group2=[6,7,8,9,10])
print(t.get_t())