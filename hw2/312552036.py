import sys
import random
from k_domination import *
from symmetric_mds import *
from matching import *
num_node = int(sys.argv[1])


def process_arg(num_node):
    node_matrix = [[0] * num_node for _ in range(num_node)]
    for i in range(num_node):
        for j in range(num_node):
            if sys.argv[i+2][j] == '1':
                node_matrix[i][j] = 1
    return node_matrix



def create_ws_model(num_node, edge):
    node_matrix = [[0] * num_node for _ in range(num_node)]
    for i in range(num_node):
        chosen = [i]
        while (len(chosen) < edge+1):
            #randomly select neighbor
            neighbor = random.randint(0, num_node-1)
            if neighbor not in chosen:
                chosen.append(neighbor)
                node_matrix[i][neighbor] = 1
                node_matrix[neighbor][i] = 1

    return node_matrix
node_matrix = process_arg(num_node)
#node_matrix = create_ws_model(6, 2)
#num_node = 6
print(f'number of node : {num_node}')
print(f'node matrix : ')
for i in range(len(node_matrix)):
    print(f'{node_matrix[i]}')

min = 10000
best_solution = ''
for _ in range(10):
    cardinality = k_domination(node_matrix, num_node)
    
    if sum(cardinality) <= min:
        min = sum(cardinality)
        best_solution = cardinality

print(f'Requirement 1-1:')
print(f'the cardinality of 2-dominaiton game is {min}')
print(f'solution = {best_solution}')
print(f'---------------------------------')

min = 100000
best_solution = ''

for _ in range(10):
    cardinality = symmetric_mds(node_matrix, num_node)
    if sum(cardinality) <= min:
        min = sum(cardinality)
        best_solution = cardinality


print(f'Requirement 1-2:')
print(f'the cardinality of Symmetric MDS-based IDS game is {min}')
print(f'solution = {best_solution}')
print(f'---------------------------------')


max = 0
best_solution = ''

for _ in range(5):
    count = 0
    cardinality = matching(node_matrix, num_node)
    temp = cardinality.copy()
    for i in range(num_node):
        if temp[i] != 'null':
            if temp[temp[i]] == i:
                count += 1
                temp[temp[i]] = 'null'
                temp[i] = 'null'

    if count >= max:
        max = count
        best_solution = cardinality

print(f'Requirement 2:')
print(f'the cardinality of Matching game is {max}')
print(f'solution = {best_solution}')
print(f'---------------------------------')
