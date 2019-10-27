#Pattern5
'''
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1

'''
def drawPattern(size):
	for i  in range(size):
		for j in range(size,-1,-1):
			print(i,end=" ")
		print()

#DriverCode
siZe=int(input())
drawPattern(siZe)
