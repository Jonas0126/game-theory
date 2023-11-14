import sys
import random
from k_domination import *
from symmetric_mds import *
#num_node = int(sys.argv[1])


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
#node_matrix = process_arg()
node_matrix = create_ws_model(6, 2)
num_node = 6
print(f'number of node : {num_node}')
print(f'node matrix : ')
for i in range(len(node_matrix)):
    print(f'{node_matrix[i]}')
print(f'---------------------------------')
print(f'k-dominaiton game ')
print(f'---------------------------------')
k_domination(node_matrix, num_node)

print(f'---------------------------------')
print(f'symmetric MDS-based IDS Game ')
print(f'---------------------------------')
symmetric_mds(node_matrix, num_node)