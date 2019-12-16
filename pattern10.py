#Pattern10
'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
def drawPAttern(size):
	i=0
	while(i<size):
		for j in range(i+1):
			print(i+1,end=" ")
		print()
		i+=1
#Driver Code
if __name__ == '__main__':
	siZe=int(input())
	drawPAttern(siZe)