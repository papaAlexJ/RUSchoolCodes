import numpy as np
import random as rn
import csv
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

def output(file: str):
	i = rn.randint(000, 999)
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
	print("Community Matrix:")
	i = 0
	out = output("community_matrix")
	
	size = int(input("Input the total number of nodes: \n"))

	community = np.zeros((size,size), dtype = int)
	
	while (i<size):
		j = 0 
		while (j<size):
			prompt = str(input(f"Does node {i} connect to node {j}? (y/n): \n"))
			if prompt == 'y':
				prompt2 = str(input(f"Is this relationship positive? (y/n): \n"))
				match prompt2.lower():
					case 'y':community[i][j] =  1
					case 'n':community[i][j] = -1
					case '' :community[i][j] =  1
					case _:print("Try again\n")		
			elif prompt in ('n', ''):pass
			j+=1
		i+=1

	with open(out, 'w', newline='') as f:
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
	edges = np.sum(np.abs(array)) / 2
	nodes = array.shape[0]
	degrees = np.sum(np.abs(array), axis = 1)

	for i in range(nodes):
		for j in range(nodes):
			if array[i][j]:
				modularity += ( (nodes / edges) - (degrees[i]/ (2 * edges))**2 )
				print(f"array at {i}, {j}: {array[i][j]} || Modularity at: {modularity}")

	modularity = modularity / (2 * edges)

	print(f"Total Edges: {edges} || Total Nodes: {nodes} || Total degrees: {degrees}")

	return modularity

def stat_vector(arr: np.ndarray):#TODO
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

def greedy_algorithm(c_m: np.ndarray, x: int):#TODO
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

def clustering_coefficient(array :np.ndarray, x: int) -> float:#TODO
	c = 0.0
	neighbors = np.where(array[x])[0]
	k_i = len(neighbors)
	#if k_i < 2: return c

	e_i = np.sum(array[np.ix_(neighbors, neighbors)]) / 2 #Wrong?

	c = (2 * e_i) / (k_i * (k_i  - 1))
	print(f"Neighbors: {neighbors} || k_i: {k_i} || e_i: {e_i}")
	return c

def degree_distribution(arr: np.ndarray) -> np.ndarray:
	dd = []
	degree = []

	for i in range(len(arr)): 
		degree.append(sum(arr[i]))

	total_degree = sum(degree)
	
	for d in degree:
		distro = d / total_degree
		dd.append(distro)

	return np.ndarray(dd)

def sas(p :float, q: float, r: float, c: int):
	tr = p * c
	sas = tr / (q + r)
	return sas

def input_csv(file_name: csv) -> np.ndarray:
	with open(file_name, 'r') as file:
		reader = csv.reader(file)
		data = []
		for idx, row in enumerate(reader):
			if not any(row):#Skip empty rows
				continue
			processed_row = []
			for value in row:
				if value.lstrip('-').isdigit():
					processed_row.append(int(value))
				elif value == '':
					processed_row.append(0)
				else:
					processed_row.append(None)
			data.append(processed_row)

	int_data = np.array(data)
	return int_data

def main():
	print(" What do you want to do today?: \n 'm' or 'mo' for modularity calulator\n 'x' for matrix\n 'p' for page rank\n 'r' for random walk\n 'c' for community matrix")
	print(" 'cc' for clustering coefficiant\n 'dd' for degree distribution\n")
	foo = input(str()).lower()
	match foo:
		case "m":
			modularity()
		case "mo":
			com_graph = input_csv(str(input("Enter the name of the community graph csv file:\n")))
			mod = modularity_(com_graph)
			print(mod)
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
		case "c":
			community_matrix()
		case "cc":
			input_ = input_csv(str(input("Enter the name of the community graph csv file:\n")))
			node = int(input("Enter the number of the node to calculte:\n"))
			print(clustering_coefficient(input_, node))
		case "dd":
			input_ = input_csv(str(input("Enter the name of the community graph csv file:\n")))
			print(degree_distribution(input_))
        case "sas":
            p = float(input("Enter the per-day probability of disease transmission: \n"))
            q = float(input("Enter the per-day probability of recovery: \n"))
            r = float(input("Enter the per-day probability the node has died:\n"))
            c = int(input("Enter the number of contacts each node has per day:\n"))
            print(sas(p,q,r,c))
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
