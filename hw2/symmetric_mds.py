from config import *
from initial import *
import random

def calculate_v_mds(player_i, player_state, node_matrix, num_node):
    count = 0
    for i in range(num_node):
        if node_matrix[player_i][i] == 1 and player_state[i] == 1:
            count += 1
    if player_state[player_i] == 1:
        count += 1
        
    return count

def calculate_g_mds(player_i, player_state, node_matrix, num_node):
    v = calculate_v_mds(player_i, player_state, node_matrix, num_node)
    if v == 1:
        return alpha
    else:
        return 0
    
def calculate_w_mds(player_i, player_state, node_matrix, num_node):
    ci = player_state[player_i]
    if ci == 0:
        return 0
    
    count = 0
    for i in range(num_node):
        if node_matrix[player_i][i] == 1 and player_state[i] == 1:
            count += gamma

    return count

def calculate_u_mds(player_i, player_state, node_matrix, num_node):

    if player_state[player_i] == 0:
        return 0
        
    sum = 0
    for i in range(num_node):
        if node_matrix[player_i][i] == 1:
            sum += calculate_g_mds(i, player_state, node_matrix, num_node)
    
    sum += calculate_g_mds(player_i, player_state, node_matrix, num_node) - beta

    w = calculate_w_mds(player_i, player_state, node_matrix, num_node)
    
    sum -= w
    
    return sum
    
def symmetric_mds(node_matrix, num_node):
    #random initial game state
    player_state, utility = initial_game(num_node)
    
    for i in range(num_node):
        utility[i] = calculate_u_mds(i, player_state, node_matrix, num_node)
        
    
    #print(f'initial player state = {player_state}')
    #print(f'initial utility = {utility}')
    
    move_count = 0
    
    #random peak one player
    player_i = random.randint(0, num_node-1)
    
    already_check = []
    
    #game start
    while(1):
        pre_state = player_state[player_i]
        player_state[player_i] = 1
        
        #player_i utility(ci=1)
        ui_1 = calculate_u_mds(player_i, player_state, node_matrix, num_node)
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