#Pattern6
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
def drawPattern(size):
	for i in range(1,size+1,1):
		for j in range(1,i+1,1):
			print(j,end=" ")
		print()

#DriverCode
siZe=int(input())
drawPattern(siZe)
