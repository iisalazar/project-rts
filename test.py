from pprint import pprint
'''
from Statistics.z_test import two_sample

z = two_sample()
z.add_data(group1=[1,2,3,4,5], group2=[6,7,8,9,10])
z.get_z_value()

from Statistics.t_test import Independent
t = Independent()
t.add_elements(group1=[1,2,3,4,5], group2=[6,7,8,9,10])
print(t.get_t())
'''
from Statistics.t_test import Dependent

t = Dependent()
t.add_elements(group1=[1,2,3,4,5], group2=[6,7,8,9,10])
#print(t.get_t())

from Statistics.anova import ANOVA

anova = ANOVA()
data = [
	{ 'label' : "soft",
		"data" : [14, 17, 25, 16]
	},
	{ 'label' : "ballad",
		"data" : [12, 22, 17, 18]
	},
	{ 'label' : "classical",
		"data" : [15, 20, 27, 16]
	},
	{ 'label' : "none",
		"data" : [16, 26, 15, 14]
	}
]
anova.set_data(data=data)
pprint(anova.get_all_data())