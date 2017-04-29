import sys
import math

def right_close(matrix,x,y):
	for index in xrange(y+1, width, 1):
		if matrix[x][index] == '0':
			return [x,index]
	return [-1,-1]

def bottom_close(matrix,x,y):
	for index in xrange(x+1, height, 1):
		if matrix[index][y] == '0':
			return [index,y]
	return [-1,-1]
# Don't let the machines win. You are humanity's last hope...

width = int(raw_input())  # the number of cells on the X axis
height = int(raw_input())  # the number of cells on the Y axis
matrix = [['.' for i in range(width+1)] for j in range(height+1)]

#print width,height

for i in xrange(height):
    line = list(raw_input())  # width characters, each either 0 or .
    for j in xrange(width):
        matrix[i][j] = line[j]

for i in xrange(height):
	for j in xrange(width):
	    if matrix[i][j] == '0':
		    print j,i,
		    print right_close(matrix,i,j)[1],right_close(matrix,i,j)[0],
		    print bottom_close(matrix,i,j)[1],bottom_close(matrix,i,j)[0]
