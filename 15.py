import sys

def Triangle(num_rows):
	num_rows+=1
	grid = [1]*num_rows
	for i in range(1,num_rows):
		for j in range(1,num_rows):
			grid[j] += grid[j-1]
		print grid

if __name__ == "__main__":
	if len(sys.argv)>=2:
		Triangle(int(sys.argv[1]))
	else:
		print("Needs a grid size")
