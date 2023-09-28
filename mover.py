import helper
import pieces
from checker import Checker

def move(selected_piece, target_square, probe):
    piece_name = selected_piece['name'][0]
    def validate_move():
        if piece_name == 'P':
            return pieces.move_pawn(selected_piece, target_square, probe)
        elif piece_name == 'R':
            return pieces.move_rook(selected_piece, target_square, probe)
        elif piece_name == 'N':
            return pieces.move_knight(selected_piece, target_square, probe)
        elif piece_name == 'B':
            return pieces.move_bishop(selected_piece, target_square, probe)
        elif piece_name == 'Q':
            return pieces.move_queen(selected_piece, target_square, probe)
        elif piece_name == 'K':
            return pieces.move_king(selected_piece, target_square, probe)

    can_make_move = validate_move()
    if (can_make_move == False):
        return False
    
    checked = Checker(selected_piece['color'], probe['layout']).was_checked()
    if (checked == True):
        return False
    
    probe['check_type'] = Checker(helper.change_color(selected_piece['color']), probe['layout']).find_check_type()
    
    return True

def find_possible_moves(layout, selected_piece, can_castle_left, can_castle_right):
    possible_moves = []
    for idx in range(64):
        if idx == selected_piece['position']:
            continue
        target_square = {
            'name': layout[idx],
            'color': helper.find_color(layout[idx]),
            'x_value': (idx % 8) + 1,
            'y_value': int(idx/8) + 1,
            'position': idx
        }
        probe = {
            'layout': list(layout),
            'can_castle_left': can_castle_left,
            'can_castle_right': can_castle_right
        }
        piece_name = selected_piece['name'][0]
        #print(piece_name)
        if (piece_name == 'P'
            and pieces.move_pawn(selected_piece, target_square, probe)
            and not(Checker(selected_piece['color'], probe['layout']).was_checked())
        ):
            possible_moves.append(idx)
        elif (piece_name == 'R'
            and pieces.move_rook(selected_piece, target_square, probe)
            and not(Checker(selected_piece['color'], probe['layout']).was_checked())
        ):
            possible_moves.append(idx)
        elif (piece_name == 'N'
            and pieces.move_knight(selected_piece, target_square, probe)
            and not(Checker(selected_piece['color'], probe['layout']).was_checked())
        ):
            possible_moves.append(idx)
        elif (piece_name == 'B'
            and pieces.move_bishop(selected_piece, target_square, probe)
            and not(Checker(selected_piece['color'], probe['layout']).was_checked())
        ):
            possible_moves.append(idx)
        elif (piece_name == 'Q'
            and pieces.move_queen(selected_piece, target_square, probe)
            and not(Checker(selected_piece['color'], probe['layout']).was_checked())
        ):
            possible_moves.append(idx)
        elif (piece_name == 'K'
            and pieces.move_king(selected_piece, target_square, probe)
            and not(Checker(selected_piece['color'], probe['layout']).was_checked())
        ):
            possible_moves.append(idx)

    return possible_moves

