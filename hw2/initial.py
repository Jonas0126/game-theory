import random

def initial_game(num_node):
    player_state = [0] * num_node
    for i in range(num_node):
        rand_num = random.randint(0,1)
        if rand_num == 1:
            player_state[i] = 1
        else:
            player_state[i] = 0
    utility = [0] * num_node
    
    return player_state, utility


def initial_matchgame(node_matrix, num_node):
    player_strategy = [0] * num_node
    for i in range(num_node):
        N = sum(node_matrix[i])
        rand_num = random.randint(0,N)
        if rand_num == N:
            player_strategy[i] = 'null'
        else:
            count = 0
            j = 0
            while 1:
                if node_matrix[i][j] == 1:
                    if count == rand_num:
                        player_strategy[i] = j
                        break
                    count += 1
                j += 1
    utility = [0] * num_node
    return player_strategy, utility   
    