#Pattern 2
'''
1 1 1 1
2 2 2 2
3 3 3 3
4 4 4 4

'''
def drawPattern(size):
	i=1
	while(i<=size):
		for j in range(size):
			print(i,end=" ")
		print("")
		i+=1

siZe=int(input())
drawPattern(siZe)
