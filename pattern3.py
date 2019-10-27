#Pattern 3
'''
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

'''
def drawPattern(size):
	for i  in range(size):
		for j in range(1,size+1,1):
			print(j,end=" ")
		print()

#DriverCode
siZe=int(input())
drawPattern(siZe)
	