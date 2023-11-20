import random
from config import *
from initial import *



def calculate_v_kdomination(player_i, player_state, node_matrix, num_node):
    count = 0
    for i in range(num_node):
        if i != player_i and node_matrix[player_i][i] == 1 and player_state[i] == 1:
                count += 1
    return count

def calculate_g_kdomination(player_i ,player_state, node_matrix, num_node):
    if player_state[player_i] == 1:
        return 0
    
    v = calculate_v_kdomination(player_i, player_state, node_matrix, num_node)
    if v <= k:
        return alpha
    else:
        return 0
    
    
def calculate_u_kdominaiton(player_i, player_state, node_matrix, num_node):
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
                
                sum += calculate_g_kdomination(i, player_state, node_matrix, num_node)
        sum -= beta
        return sum
               
def k_domination(node_matrix, num_node): 
    #random initial game state
    player_state, utility = initial_game(num_node)
    
    for i in range(num_node):
        utility[i] = calculate_u_kdominaiton(i, player_state, node_matrix, num_node)

    move_count = 0
    #random peak one player
    player_i = random.randint(0, num_node-1)
    already_check = []
    while(1):
        #print(f'player {player_i} was chosen')
        pre_state = player_state[player_i]
        player_state[player_i] = 1

        #player_i utility(ci = 1)
        ui_1 = calculate_u_kdominaiton(player_i, player_state, node_matrix, num_node)
        utility[player_i] = ui_1

        if ui_1 < 0:
            player_state[player_i] = 0
            utility[player_i] = 0

        if pre_state == player_state[player_i]:
            already_check.append(player_i)
        else:
            already_check.clear()

        move_count += 1
        if len(already_check) == num_node:
            break
        while(1):
            player_i = random.randint(0, num_node-1)
            if player_i not in already_check:
                break
    return player_state