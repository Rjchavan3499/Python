#Desc -> A library for reading in 2D arrays of integers, doubles, or booleans from
#standard input and printing them out to standard
def arr(int1,int2):

	matrix = []
	print("Enter the entries rowwise:")

# For user input
	for i in range(int1):
		a =[]
	for j in range(int2):
		a.append(int(input()))
		matrix.append(a)

# For printing the matrix
	for i in range(int1):
		for j in range(int2):
			print(matrix[i][j], end = " ")

a = int(input("Enter the number of rows:"))
b = int(input("Enter the number of columns:"))
ans = arr(a,b)