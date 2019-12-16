#Pattern8
'''
*
* *
* * *
* * * *
* * * * *
'''
def drawPAttern(size):
	i=0
	while(i<size):
		for j in range(i+1):
			print(end="* ")
		print()
		i+=1
#Driver Code
if __name__ == '__main__':
	siZe=int(input())
	drawPAttern(siZe)
