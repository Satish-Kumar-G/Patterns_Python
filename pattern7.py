#Pattern7
'''
1
1 1
1 1 1
1 1 1 1
1 1 1 1 1
'''
def drawPattern(size):
	for i in range(1,size+1,1):
		for j in range(1,i+1,1):
			print('1',end=" ")
		print()

#DriverCode
siZe=int(input())
drawPattern(siZe)