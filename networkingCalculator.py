import numpy as np
import random as rn
import csv
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

def output(file: str):
	i = rn.randint(100, 999)
	out = os.path.join(current_directory, (file + str(i) + ".csv"))

	return out

def matrix(x: int):
	i = j = 0
	d = np.zeros((x,x))
	out = output("matrix")

	while (i<len(d)):
		while (j<len(d)):
			d[i][j] = float(input(f"[{i}, {j}]: Enter a value: \n"))
			j+=1
				
		i+=1
		if (j==len(d)):
			j = 0

	with open(out, 'w') as f:
		write = csv.writer(f)
		write.writerows(d)
	
	return d

def community_matrix():
	i = 0
	out = output("community_matrix")
	
	size = int(input("Input the total number of nodes: \n"))

	community = np.zeros((size,size), dtype = bool)
	
	while (i<size):
		j = 0 
		while (j<size):
			prompt = str(input(f"Does node {i} connect to node {j}? (y/n): \n"))
			match prompt.lower():
				case 'y':
					community[i][j] = True
					j+=1
				case 'n':
					j+=1
				case _:
					print("Try again\n")
		i+=1

	with open(out, 'w') as f:
		write = csv.writer(f)
		write.writerows(community)

	return community

def random_walk(i: int):
	j = np.zeros((i,i)) + (1 / i)
	return j

def modularity():
	i = j = sum = 0
	modularity = []
	nodes = []
	degrees = []
	
	edges = int(input("Input total number of edges: \n"))
	groups = int(input("Input number of colors: \n"))
	
	while (i<groups):
		print(f"Community {i + 1}")
		input_node = int(input("Input the total number of nodes in this community: \n"))
		nodes.append(input_node)

		input_degree = int(input("Input the total degrees of all the edges within this community: \n"))
		degrees.append(input_degree)

		modularity.append( (nodes[i] / edges) - (degrees[i]/ (2 * edges))**2 )

		print(f"Nodes: {nodes[i]}, degrees: {degrees[i]}, modularity: {modularity[i]}.\n")

		sum = sum + modularity[i]
		i+=1

	while (j<groups):
		print(f"Modularity of group {j}: {modularity[j]}")
		j+=1

	print(f"Total Modularity: {sum}")

def modularity_(array :np.ndarray):
	modularity = 0.0

	edges = np.sum(array) / 2
	nodes = array.shape[0]

	degrees = np.sum(array, axis = 1)

	for i in range(nodes):
		e = 0
		for j in range(nodes):
			if array[i][j]:
				e+=1
				
		modularity = ( (nodes / edges) - (degrees[i]/ (2 * edges))**2 )

	return modularity

def stat_vector(arr: np.ndarray):
	a = arr[0][0]
	b = arr[0][1]
	c = arr[0][2]

	##todo

	##print(stationary_vector)
	##return stationary_vector
	return 0

def page_rank(i: int, x: int):
	matrix_a = matrix(x)
	print(matrix_a)
	a = float(input("Enter the jump probability"))
	matrix_b = random_walk(len(matrix_a))
	print(matrix_b)

	while True:
		matrix_c = (a * matrix_b) + ((1 - a) * matrix_a)
		if (i==1):
			print(matrix_c)
			##stat_vector(matrix_c)
			return matrix_c

			break
		else:
			i-=1
			matrix_a = matrix_c

def greedy_algorithm(c_m: numpy.ndarray, x: int):#TODO
	a = c_m.shape[0]

	permuted_indices = np.random.permutation(a)

	split_point = a // 2
	first_i = permuted_indices[:split_point]
	second_i = permuted_indices[split_point:]

	array_1 = c_m[:, first_i]
	array_2 = c_m[:, second_i]

	modularity_1 = modularity_(array_1)
	modularity_2 = modularity_(array_2)

	while (x > 0):

		i = 0

		while (i>len(array_1)):
			z = 0
			i+=1

def main():
	print(" What do you want to do today?: \n 'm' for modularity calulator\n 'x' for matrix\n 'p' for page rank\n 'r' for random walk")
	foo = input(str()).lower()
	match foo:
		case "m":
			modularity()
		case "x":
			x = int(input("Enter the size of the matrix: "))
			print(matrix(x))
		case "p":
			x = int(input("Enter the size of the matrix: "))
			i = int(input(" How many adjustments do you want to make?: \n"))
			print(page_rank(i, x))
		case "r":
			i = int(input(" Enter size of matrix: \n"))
			print(random_walk(i))
		case "s":##TODO
			k = np.zeros((3,3))
			k[0][1] = k[0][2] = k[2][0] = k[2][1] = 0.5
			k = page_rank(k, 2)
			stat_vector(k)

main()

#################

def _modularity():#Old
	i = 0
	j = []
	foo = int(input(" Enter total number of colors: "))
	m = int(input(" Enter the total number of edges: "))
	while (i<foo):
		print(i)
		e = float(input(" Enter the fraction of edges: "))

		k = int(input(" Enter the total degrees in this community: "))
		j.append(e - ( (k / (2*m) )**2 ) )
		i+=1
	print(j)
	return j