import sys
import random
alpha = 10
beta = 5
#num_node = int(sys.argv[1])
k = 2

def process_arg():
    node_matrix = [[0] * num_node for _ in range(num_node)]
    for i in range(num_node):
        for j in range(num_node):
            if sys.argv[i+2][j] == '1':
                node_matrix[i][j] = 1
    return node_matrix

def calculate_v(player_i, player_state, node_matrix):
    count = 0
    for i in range(num_node):
        if i != player_i and node_matrix[player_i][i] == 1 and player_state[i] == 1:
                count += 1
    return count

def calculate_g(player_i ,player_state, node_matrix):
    if player_state[player_i] == 1:
        return 0
    
    v = calculate_v(player_i, player_state, node_matrix)
    if v <= k:
        return alpha
    else:
        return 0
def calculate_u(player_i, player_state, node_matrix):
    degree_i = 0
    #calculate degree of player_i 
    for i in node_matrix[player_i]:
        if i == 1:
            degree_i += 1
    
    if player_state[player_i] == 0:
        return 0

    if degree_i < k:
        return alpha
    elif degree_i >= k:
        sum = 0
        for i in range(num_node):
            if node_matrix[player_i][i] == 1 and i != player_i:
                
                sum += calculate_g(i, player_state, node_matrix)
        sum -= beta
        return sum
               
def k_domination(node_matrix):
    
    #random initial game state
    player_state = [0] * num_node
    for i in range(num_node):
        rand_num = random.randint(0,1)
        if rand_num == 1:
            player_state[i] = 1
        else:
            player_state[i] = 0
    utility = [0] * num_node
    for i in range(num_node):
        utility[i] = calculate_u(i, player_state, node_matrix)
    
    print(f'initial player state = {player_state}')
    print(f'initial utility = {utility}')


    move_count = 0
    #random peak one player
    player_i = random.randint(0, num_node-1)
    already_cheack = []
    while(1):
        print(f'player {player_i} was chosen')
        pre_state = player_state[player_i]
        player_state[player_i] = 1

        #player_i utility(ci = 1)
        ui_1 = calculate_u(player_i, player_state, node_matrix)
        utility[player_i] = ui_1

        if ui_1 < 0:
            player_state[player_i] = 0
            utility[player_i] = 0


        if pre_state == player_state[player_i]:
            already_cheack.append(player_i)
        else:
            already_cheack.clear()

        move_count += 1
        print(f'player state after {move_count} update : {player_state}')
        print(f'------------------------------------------------------------')
        if len(already_cheack) == num_node:
            break
        while(1):
            player_i = random.randint(0, num_node-1)
            if player_i not in already_cheack:
                break
        


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
node_matrix = create_ws_model(8, 2)
num_node = 8
print(f'number of node : {num_node}')
print(f'node matrix : ')
for i in range(len(node_matrix)):
    print(f'{node_matrix[i]}')
print(f'---------------------------------')
print(f'k-dominaiton game ')
print(f'---------------------------------')
k_domination(node_matrix)