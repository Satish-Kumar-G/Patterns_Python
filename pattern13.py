#Pattern13
'''
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
'''
def drawPAttern(size):
	i=0
	while(i<size):
		for j in range(size-i):
			print(i+1,end=" ")
		print()
		i+=1
#Driver Code
if __name__ == '__main__':
	siZe=int(input())
	drawPAttern(siZe)