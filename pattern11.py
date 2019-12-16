#Pattern11
'''
* * * * *
* * * *
* * *
* * 
*
'''
def drawPAttern(size):
	i=size
	while(i>0):
		for j in range(i):
			print(end="* ")
		print()
		i-=1
#Driver Code
if __name__ == '__main__':
	siZe=int(input())
	drawPAttern(siZe)