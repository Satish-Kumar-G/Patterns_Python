#Pattern4
'''
5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1


'''
def drawPattern(size):
	for i  in range(size,-1,-1):
		for j in range(size):
			print(i,end=" ")
		print()

#DriverCode
siZe=int(input())
drawPattern(siZe)