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