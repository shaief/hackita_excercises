print "enter a number: "
n = raw_input()
nn = int(n)

print "Here is your multiplication board :) :"

multi_list = [[((i+1)*(j+1)) for i in range(nn)] for j in range(nn)]
for i in range(nn):
	print multi_list[i][:]

import numpy as np

multi = np.zeros((nn,nn), dtype=np.int)
for i in range(nn):
	for j in range(nn):
		multi[i,j] = (i+1)*(j+1)
print multi