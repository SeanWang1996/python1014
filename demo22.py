import copy

player1 = [['A', 'K'], ['Q', 'J']]
player2 = player1
player3 = copy.copy(player1)
player4 = copy.deepcopy(player1)
print(player1, player2, player3, player4)
player1.append('JOKER')
print(player1, player2, player3, player4)
player1[0][1] = 10
print(player1, player2, player3, player4)