import random
from config import *
from initial import *


def calculate_priority_mat(node_matrix, num_node):
    priority = [0] * num_node

    for i in range(num_node):
        priority[i] = 1/sum(node_matrix[i])

    return priority

def calculate_g_mat(player_i, player_strategy):
    ci = player_strategy[player_i]
    cj = player_strategy[ci]

    if cj != player_i:
        return beta
    
    elif cj == player_i:
        return alpha
    
def calculate_w_mat(player_i, player_strategy, player_priority, node_matrix, num_node):
    ci = player_strategy[player_i]

    #Check if there exists a node whose priority is higher or equal to Pi, and the strategy is the same as Pi.
    for i in range(num_node):
        if node_matrix[ci][i] == 1 and i != player_i:
            if player_priority[player_i] <= player_priority[i] and player_strategy[i] == ci:
                return gamma
            
    return 0

def calculate_u_mat(player_i, player_strategy, player_priority, node_matrix, num_node):
    if player_strategy[player_i] == 'null':
        return 0
    
    g = calculate_g_mat(player_i, player_strategy)
    w = calculate_w_mat(player_i, player_strategy, player_priority, node_matrix, num_node)

    return g-w


def matching(node_matrix, num_node):

    #initial game
    player_strategy, utility = initial_matchgame(node_matrix, num_node)
    player_priority = calculate_priority_mat(node_matrix, num_node)

    for i in range(num_node):
        utility[i] = calculate_u_mat(i, player_strategy, player_priority, node_matrix, num_node)

    #print(f'player priority = {player_priority}')
    #print(f'initial player strategy = {player_strategy}')
    #print(f'initial utility = {utility}')

    move_count = 0
    player_i = random.randint(0, num_node-1)

    already_check = []

    #game start
    while 1:
        #print(f'player {player_i} was chosen')
        pre_strategy = player_strategy[player_i]
        max = 0
        best_strategy = None
        for i in range(num_node):
            if node_matrix[player_i][i] == 1:
                player_strategy[player_i] = i
                u = calculate_u_mat(player_i, player_strategy, player_priority, node_matrix, num_node)
                if u > max:
                    max = u
                    best_strategy = i
        
        if max == 0:
            player_strategy[player_i] = 'null'
            utility[player_i] = 0
        else:
            player_strategy[player_i] = best_strategy
            utility[player_i] = max

        if pre_strategy == player_strategy[player_i]:
            already_check.append(player_i)
        else:
            already_check.clear()

        move_count += 1

        #print(f'player strategy after {move_count} update : {player_strategy}')
        #print(f'----------------------------------------------------------')

        if len(already_check) == num_node:
            break

        while(1):
            player_i = random.randint(0, num_node-1)
            if player_i not in already_check:
                break
    return player_strategy
