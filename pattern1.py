#Pattern 1
'''
* * * *
* * * *
* * * *
* * * *

'''
def drawPattern(size):
	for row in range(size):
		for col in range(size):
			print(" * ",end="")
		print("")

siZe=int(input())
drawPattern(siZe)
