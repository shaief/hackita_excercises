import numpy as np

print "enter a number: "
n = raw_input()
nn = int(n)
multi = np.zeros((nn,nn), dtype=np.int)
for i in range(nn):
	for j in range(nn):
		multi[i,j] = (i+1)*(j+1)
print multi