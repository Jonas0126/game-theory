import numpy as np

def create_utility(): 
    #utility[player1 act][player2 act][player utility] 
    utility = np.zeros((2, 2, 2))
    for i in range(2):
        for j in range(2):
            for k in range(2):
                utility[i][j][k] = input(f'player{k} utility at ({i},{j}) : ')
    return utility

def calculate_payoff(prob, utility):
    #payoff[player][act payoff]
    payoff = np.zeros((2, 2))
    for i in range(2):
        payoff[0][i] = prob[1][0] * utility[i][0][0] + prob[1][1] * utility[i][1][0]
    for i in range(2):
        payoff[1][i] = prob[0][0] * utility[0][i][1] + prob[0][1] * utility[1][i][1]
    return payoff

def belief():
    #prob[player][action]
    prob = np.zeros((2, 2))
    for i in range(2):
        for j in range(2):
            prob[i][j] = input(f'how many time did player{i} perform action{j} : ')
    return prob


#update player belief
def update(belief_matrix, payoff):
    act = np.zeros(2)
    if payoff[0][0] > payoff[0][1]:
        belief_matrix[0][0] += 1
        act[0] = 0
    elif payoff[0][0] < payoff[0][1]:
        belief_matrix[0][1] += 1
        act[0] = 1
    else:
        randnum = np.random.rand(1)
        print(randnum[0])
        if randnum[0] >= 0.5:
            belief_matrix[0][1] += 1
            act[0] = 1
        else:
            belief_matrix[0][0] += 1
            act[0] = 0 

    if payoff[1][0] > payoff[1][1]:
        belief_matrix[1][0] += 1
        act[1] = 0
    elif payoff[1][0] < payoff[1][1]:
        belief_matrix[1][1] += 1
        act[1] = 1
    else:
        randnum = np.random.rand(1)
        if randnum[0] >= 0.5:
            belief_matrix[1][1] += 1
            act[1] = 1
        else:
            belief_matrix[1][0] += 1
            act[1] = 0
    return act
def play(round):
    utility_matrix = create_utility()
    print(f'utility_matrix = {utility_matrix}')
    belief_matrix = belief()
    print(f'round 0, 1\'s act : -, 2\'s act : -', end='')
    for i in range(round):
        
        print(f'1\'s belief : {belief_matrix[1]}, 2\'s belief : {belief_matrix[0]}, ', end="")
        payoff = calculate_payoff(belief_matrix, utility_matrix)
        print(f'1\'s payoff : {payoff[0]}, 2\'s payoff : {payoff[1]}')
        act = update(belief_matrix, payoff)
        
        print(f'round {i}, 1\'s act : {act[0]}, 2\'s act : {act[1]}, ', end='')
    print(f'1\'s belief : {belief_matrix[1]}, 2\'s belief : {belief_matrix[0]}, ', end="")
    payoff = calculate_payoff(belief_matrix, utility_matrix)
    print(f'1\'s payoff : {payoff[0]}, 2\'s payoff : {payoff[1]}')
    act = update(belief_matrix, payoff)
    print('')
    player1_act0_prob = belief_matrix[0][0] / belief_matrix[0].sum()
    player1_act1_prob = belief_matrix[0][1] / belief_matrix[0].sum()
    player2_act0_prob = belief_matrix[1][0] / belief_matrix[1].sum()
    player2_act1_prob = belief_matrix[1][1] / belief_matrix[1].sum()
    print(f'player 1\'s act prob : ({player1_act0_prob}, {player1_act1_prob}), player 2\'s act prob : ({player2_act0_prob}, {player2_act1_prob})')
play(1000)


