#Pattern14
'''
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''
def drawPAttern(size):
	i=size
	while(i>0):
		for j in range(i):
			print(i,end=" ")
		print()
		i-=1
#Driver Code
if __name__ == '__main__':
	siZe=int(input())
	drawPAttern(siZe)
	