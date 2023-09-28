import csv
import helper
import time
from board import Board

initialLayout = ["RW","NW","BW","KW","QW","BW","NW","RW","PW","PW","PW","PW","PW","PW","PW","PW","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","PB","PB","PB","PB","PB","PB","PB","PB","RB","NB","BB","KB","QB","BB","NB","RB"]

class Game:
    over = False
    player_one = {
        'color': 'white',
        'history': [],
        'can_castle_left': True,
        'can_castle_right': True,
        'winner': False
    }
    player_two = {
        'color': 'black',
        'history': [],
        'can_castle_left': True,
        'can_castle_right': True,
        'winner': False
    }
    def __init__(self, layout):
        self.board = Board(self, layout)

file_name = str(int(time.time())) + '.csv'
print(file_name)
for num in range(50):
    game = Game(initialLayout)
    while not(game.over):
        game.board.move_piece()
    training_data = helper.get_training_data(game.player_one, game.player_two)
    with open(file_name, 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(training_data)