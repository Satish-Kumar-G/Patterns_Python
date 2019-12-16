#Pattern9
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
def drawPAttern(size):
	i=0
	while(i<size):
		for j in range(i+1):
			print(j+1,end=" ")
		print()
		i+=1
#Driver Code
if __name__ == '__main__':
	siZe=int(input())
	drawPAttern(siZe)