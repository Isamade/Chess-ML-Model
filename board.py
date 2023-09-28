import random
import helper
import mover

class Board:
    players_turn = 'white'
    selected_piece = {
        'name': '',
        'color': '',
        'position': None,
        'x_value': None,
        'y_value': None
    }
    target_square = {
        'name': '',
        'color': '',
        'position': None,
        'x_value': None,
        'y_value': None
    }
    probe = {
        'check_type': '',
        'can_castle_left': True,
        'can_castle_right': True,
        'layout': []
    }
    possible_moves = []

    def __init__(self, game, layout):
        self.game = game
        self.layout = layout

    def select_piece(self):
        self.selected_piece['position'] = random.randrange(0, 64)
        self.selected_piece['name'] = self.layout[self.selected_piece['position']]
        self.selected_piece['color'] = helper.find_color(self.selected_piece['name'])        
        while self.selected_piece['name'] == '' or self.selected_piece['color'] != self.players_turn:
            self.selected_piece['position'] = random.randrange(0, 64)
            self.selected_piece['name'] = self.layout[self.selected_piece['position']]
            self.selected_piece['color'] = helper.find_color(self.selected_piece['name'])
        self.selected_piece['x_value'] = (self.selected_piece['position'] % 8) + 1
        self.selected_piece['y_value'] = int(self.selected_piece['position'] / 8) + 1
        #print(self.selected_piece)

    def select_target(self, possible_moves):
        selected_move = random.choice(possible_moves)
        self.target_square['position'] = selected_move
        self.target_square['name'] = self.layout[selected_move]
        self.target_square['color'] = helper.find_color(self.target_square['name'])
        self.target_square['x_value'] = (self.target_square['position'] % 8) + 1
        self.target_square['y_value'] = int(self.target_square['position'] / 8) + 1

    def move_piece(self):
        possible_moves = []
        self.probe['can_castle_left'] = self.game.player_one['can_castle_left'] if self.selected_piece['color'] == 'white' else self.game.player_two['can_castle_left']
        self.probe['can_castle_right'] = self.game.player_one['can_castle_right'] if self.selected_piece['color'] == 'white' else self.game.player_two['can_castle_right']
        self.probe['layout'] = list(self.layout)

        while len(possible_moves) == 0:
            self.select_piece()
            possible_moves = mover.find_possible_moves(self.layout, self.selected_piece, self.probe['can_castle_left'], self.probe['can_castle_right'])
            #print(possible_moves)
        self.select_target(possible_moves)

        moved = mover.move(self.selected_piece, self.target_square, self.probe)
        if moved == False:
            return
        
        if self.players_turn == 'white':
            self.game.player_one['history'].append(self.layout + self.probe['layout'])
            self.game.player_one['can_castle_left'] = self.probe['can_castle_left']
            self.game.player_one['can_castle_right'] = self.probe['can_castle_right']
        elif self.players_turn == 'black':
            self.game.player_two['history'].append(self.layout + self.probe['layout'])
            self.game.player_two['can_castle_left'] = self.probe['can_castle_left']
            self.game.player_two['can_castle_right'] = self.probe['can_castle_right']

        if self.probe['check_type'] == 'checkmate' or self.probe['check_type'] == 'stalemate' or helper.check_stalemate(self.probe['layout']):
            print(self.probe)
            self.game.over = True
        if self.probe['check_type'] == 'checkmate':
            self.game.player_one['winner'] = True if self.players_turn == 'white' else False
            self.game.player_two['winner'] = True if self.players_turn == 'black' else False

        self.players_turn = helper.change_color(self.players_turn)
        self.layout = list(self.probe['layout'])
        