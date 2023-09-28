import random

def find_color(piece):
    if piece == '':
        return ''
    return 'white' if piece[1] == 'W' else ('black' if piece[1] == 'B' else '')

def change_color(color):
    return 'white' if color == 'black' else ('black' if color == 'white' else '')

def find_kings(layout):
    kings_positions = {
        'white': None,
        'black': None
    }
    for index, value in enumerate(layout):
        if value == 'KW':
            kings_positions['white'] = index
        if value == 'KB':
            kings_positions['black'] = index
    return kings_positions

def update_position(probe_layout, current_position, target_position):
    new_layout = list(probe_layout)
    new_layout[target_position] = new_layout[current_position]
    new_layout[current_position] = ''
    return new_layout

def update_position_swap_piece(probe_layout, current_position, target_position):
    new_layout = list(probe_layout)
    if probe_layout[current_position][1] == 'W':
        new_layout[target_position] = random.choice(['RW', 'NW', 'BW', 'QW'])
    elif probe_layout[current_position][1] == 'B':
        new_layout[target_position] = random.choice(['RB', 'NB', 'BB', 'QB'])
    new_layout[current_position] = ''
    return new_layout

def linear_move(probe_layout, current_square, target_square):
    if current_square['x_value'] == target_square['x_value'] or current_square['y_value'] == target_square['y_value']:
        if target_square['x_value'] == current_square['x_value'] and target_square['y_value'] < current_square['y_value']:
            for pos in range(current_square['position'] - 8, target_square['position'], -8):
                possible = False if probe_layout[pos] != '' else True
                if not(possible):
                    return False
        elif target_square['x_value'] < current_square['x_value'] and target_square['y_value'] == current_square['x_value']:
            for pos in range(current_square['position'] - 1, target_square['position'], -1):
                possible = False if probe_layout[pos] != '' else True
                if not(possible):
                    return False
        elif target_square['x_value'] > current_square['x_value'] and target_square['y_value'] == current_square['y_value']:
            for pos in range(current_square['position'] + 1, target_square['position'], 1):
                possible = False if probe_layout[pos] != '' else True
                if not(possible):
                    return False
        elif target_square['x_value'] == current_square['x_value'] and target_square['y_value'] > current_square['y_value']:
            for pos in range(current_square['position'] + 8, target_square['position'], 8):
                possible = False if probe_layout[pos] != '' else True
                if not(possible):
                    return False
        return True
    else:
        return False

def diagonal_move(probe_layout, current_square, target_square):
    if abs(current_square['x_value'] - target_square['x_value']) == abs(current_square['y_value'] - target_square['y_value']):
        if target_square['x_value'] < current_square['x_value'] and target_square['y_value'] < current_square['y_value']:
            for pos in range(current_square['position'] - 9, target_square['position'], -9):
                possible = False if probe_layout[pos] != '' else True
                if not(possible):
                    return False
        elif target_square['x_value'] > current_square['x_value'] and target_square['y_value'] < current_square['y_value']:
            for pos in range(current_square['position'] - 7, target_square['position'], -7):
                possible = False if probe_layout[pos] != '' else True
                if not(possible):
                    return False
        elif target_square['x_value'] < current_square['x_value'] and target_square['y_value'] > current_square['y_value']:
            for pos in range(current_square['position'] + 7, target_square['position'], 7):
                possible = False if probe_layout[pos] != '' else True
                if not(possible):
                    return False
        elif target_square['x_value'] > current_square['x_value'] and target_square['y_value'] > current_square['y_value']:
            for pos in range(current_square['position'] + 9, target_square['position'], 9):
                possible = False if probe_layout[pos] != '' else True
                if not(possible):
                    return False
        return True
    else:
        return False

def check_stalemate(layout):
    for pos in range(64):
        if layout[pos] != 'KW' and layout[pos] != 'KB' and layout[pos] != '':
            return False
    return True

def get_training_data(player_one, player_two):
    training_data = []
    def transform_entry(piece):
        if piece == 'PW':
            return 1
        elif piece == 'PB':
            return -1
        elif piece == 'BW':
            return 2
        elif piece == 'BB':
            return -2
        elif piece == 'NW':
            return 3
        elif piece == 'NB':
            return -3
        elif piece == 'RW':
            return 4
        elif piece == 'RB':
            return -4
        elif piece == 'QW':
            return 5
        elif piece == 'QB':
            return -5
        elif piece == 'KW':
            return 6
        elif piece == 'KB':
            return -6
        elif piece == '':
            return 0
    for move in player_one['history']:
        player_one_move = map(transform_entry, move)
        if player_one['winner'] == True:
            training_data.append(list(player_one_move) + [1])
        elif player_one['winner'] == False:
            training_data.append(list(player_one_move) + [0])
    for move in player_two['history']:
        player_two_move = map(transform_entry, move)
        if player_two['winner'] == True:
            training_data.append(list(player_two_move) + [1])
        elif player_two['winner'] == False:
            training_data.append(list(player_two_move) + [0])
    return training_data