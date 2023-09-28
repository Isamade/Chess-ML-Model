import helper
from checker import Checker

def move_pawn(selected_piece, target_square, probe):
    if selected_piece['color'] != target_square['color']:
        if selected_piece['x_value'] == target_square['x_value'] and target_square['color'] != helper.change_color(selected_piece['color']):
            if target_square['y_value'] - selected_piece['y_value'] == 1 and selected_piece['color'] == 'white':
                if (target_square['y_value'] == 2 or target_square['y_value'] == 3 or target_square['y_value'] == 4 
                    or target_square['y_value'] == 5 or target_square['y_value'] == 6 or target_square['y_value'] == 7
                ):
                    probe['layout'] = helper.update_position(probe['layout'], selected_piece['position'], target_square['position'])
                    return True
                elif(target_square['y_value'] == 8):
                    probe['layout'] = helper.update_position_swap_piece(probe['layout'], selected_piece['position'], target_square['position'])
                    return True
            elif target_square['y_value'] - selected_piece['y_value'] == -1 and selected_piece['color'] == 'black':
                if (target_square['y_value'] == 2 or target_square['y_value'] == 3 or target_square['y_value'] == 4
                    or target_square['y_value'] == 5 or target_square['y_value'] == 6 or target_square['y_value'] == 7
                ):
                    probe['layout'] = helper.update_position(probe['layout'], selected_piece['position'], target_square['position'])
                    return True
                elif (target_square['y_value'] == 1):
                    probe['layout'] = helper.update_position_swap_piece(probe['layout'], selected_piece['position'], target_square['position'])
                    return True
            elif (target_square['y_value'] - selected_piece['y_value'] == 2 and selected_piece['y_value'] == 2 and selected_piece['color'] == 'white'
                and helper.linear_move(probe['layout'], selected_piece, target_square)
            ):
                probe['layout'] = helper.update_position(probe['layout'], selected_piece['position'], target_square['position'])
                return True
            elif (target_square['y_value'] - selected_piece['y_value'] == -2 and selected_piece['y_value'] == 7 and selected_piece['color'] == 'black'
                and helper.linear_move(probe['layout'], selected_piece, target_square)
            ):
                probe['layout'] = helper.update_position(probe['layout'], selected_piece['position'], target_square['position'])
                return True
        elif (abs(selected_piece['x_value'] - target_square['x_value']) == 1 and target_square['color'] ==  helper.change_color(selected_piece['color'])):
            if target_square['y_value'] - target_square['y_value'] == 1 and selected_piece['color'] == 'white':
                if (target_square['y_value'] == 3 or target_square['y_value'] == 4 or target_square['y_value'] == 5
                    or target_square['y_value'] == 6 or target_square['y_value'] == 7
                ):
                    probe['layout'] = helper.update_position(probe['layout'], selected_piece['position'], target_square['position'])
                    return True
                elif (target_square['y_value'] == 8):
                    probe['layout'] = helper.update_position_swap_piece(probe['layout'], selected_piece['position'], target_square['position'])
                    return True
            elif target_square['y_value'] - target_square['y_value'] == -1 and selected_piece['color'] == 'black':
                if (target_square['y_value'] == 2 or target_square['y_value'] == 3 or target_square['y_value'] == 4
                    or target_square['y_value'] == 5 or target_square['y_value'] == 6
                ):
                    probe['layout'] = helper.update_position(probe['layout'], selected_piece['position'], target_square['position'])
                    return True
                elif (target_square['y_value'] == 1):
                    probe['layout'] = helper.update_position_swap_piece(probe['layout'], selected_piece['position'], target_square['position'])
                    return True
    return False


def move_rook(selected_piece, target_square, probe):
    if selected_piece['color'] != target_square['color'] and helper.linear_move(probe['layout'], selected_piece, target_square):
        probe['can_castle_left'] = False if selected_piece['x_value'] == 1 else probe['can_castle_left']
        probe['can_castle_right'] = False if selected_piece['x_value'] == 8 else probe['can_castle_right']
        probe['layout'] = helper.update_position(probe['layout'], selected_piece['position'], target_square['position'])
        return True
    return False

def move_knight(selected_piece, target_square, probe):
    if abs(selected_piece['color'] != target_square['color']
            and selected_piece['x_value'] - target_square['x_value'] == 2 and abs(selected_piece['y_value'] - target_square['y_value']) == 1
    ):
        probe['layout'] = helper.update_position(probe['layout'], selected_piece['position'], target_square['position'])
        return True
    elif abs(selected_piece['color'] != target_square['color'] 
            and selected_piece['x_value'] - target_square['x_value'] == 1 and abs(selected_piece['y_value'] - target_square['y_value']) == 2
    ):
        probe['layout'] = helper.update_position(probe['layout'], selected_piece['position'], target_square['position'])
        return True
    return False

def move_bishop(selected_piece, target_square, probe):
    if selected_piece['color'] != target_square['color'] and helper.diagonal_move(probe['layout'], selected_piece, target_square):
        probe['layout'] = helper.update_position(probe['layout'], selected_piece['position'], target_square['position'])
        return True
    return False

def move_queen(selected_piece, target_square, probe):
    if (selected_piece['color'] != target_square['color'] 
        and (helper.diagonal_move(probe['layout'], selected_piece, target_square) or helper.linear_move(probe['layout'], selected_piece, target_square))
    ):
        probe['layout'] = helper.update_position(probe['layout'], selected_piece['position'], target_square['position'])
        return True
    return False

def move_king(selected_piece, target_square, probe):
    if (selected_piece['color'] != target_square['color']
        and abs(selected_piece['x_value'] - target_square['x_value']) <= 1
        and abs(selected_piece['y_value'] - target_square['y_value']) <= 1
        and (abs(selected_piece['x_value'] - target_square['x_value']) + abs(selected_piece['y_value'] - target_square['y_value']) != 0)
    ):
        probe['can_castle_left'] = False
        probe['can_castle_right'] = False
        probe['layout'] = helper.update_position(probe['layout'], selected_piece['position'], target_square['position'])
        return True
    elif (selected_piece['color'] != target_square['color']
        and selected_piece['name'] == 'KW' and target_square['y_value'] == 1
    ):
        if (probe['can_castle_left'] and target_square['x_value'] == 2
            and helper.linear_move(probe['layout'], selected_piece, {'position': 0, 'x_value': 1, 'y_value': 1})
            and not(Checker('white', probe['layout']).was_checked())
            and not(Checker('white', helper.update_position(probe['layout'], selected_piece['position'], 2)).was_checked())
        ):
            probe['layout'] = helper.update_position(probe['layout'], selected_piece['position'], target_square['position'])
            probe['layout'] = helper.update_position(probe['layout'], 0, 2)
            probe['can_castle_left'] = False
            probe['can_castle_right'] = False
            return True
        elif (probe['can_castle_right'] and target_square['x_value'] == 6
              and helper.linear_move(probe['layout'], selected_piece, {'position': 7, 'x_value': 8, 'y_value': 1})
              and not(Checker('white', probe['layout']).was_checked())
              and not(Checker('white', helper.update_position(probe['layout'], selected_piece['position'], 4)).was_checked())
        ):
            probe['layout'] = helper.update_position(probe['layout'], selected_piece['position'], target_square['position'])
            probe['layout'] = helper.update_position(probe['layout'], 7, 4)
            probe['can_castle_left'] = False
            probe['can_castle_right'] = False
            return True
    elif (selected_piece['color'] != target_square['color']
          and selected_piece['name'] == 'KB' and target_square['y_value'] == 8
    ):
        if (probe['can_castle_left'] and target_square['x_value'] == 2
            and helper.linear_move(probe['layout'], selected_piece, {'position': 56, 'x_value': 1, 'y_value': 8})
            and not(Checker('black', probe['layout']).was_checked())
            and not(Checker('black', helper.update_position(probe['layout'], selected_piece['position'], 58)).was_checked())
        ):
            probe['layout'] = helper.update_position(probe['layout'], selected_piece['position'], target_square['position'])
            probe['layout'] = helper.update_position(probe['layout'], 56, 58)
            probe['can_castle_left'] = False
            probe['can_castle_right'] = False
            return True
        elif (probe['can_castle_right'] and target_square['x_value'] == 6
              and helper.linear_move(probe['layout'], selected_piece, {'position': 63, 'x_value': 8, 'y_value': 8})
              and not(Checker('black', probe['layout']).was_checked())
              and not(Checker('black', helper.update_position(probe['layout'], selected_piece['position'], 60)).was_checked())
        ):
            probe['layout'] = helper.update_position(probe['layout'], selected_piece['position'], target_square['position'])
            probe['layout'] = helper.update_position(probe['layout'], 63, 60)
            probe['can_castle_left'] = False
            probe['can_castle_right'] = False
            return True
    return False

