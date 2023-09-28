import helper
import pieces

class Checker:
    def __init__(self, color, layout):
        self.color = color
        self.layout = layout
        self.probe = {
            'layout': list(layout),
            'can_castle_left': False,
            'can_castle_right': False
        }

    def was_checked(self):
        pos = helper.find_kings(self.probe['layout'])[self.color]
        target_square = {
            'name': self.probe['layout'][pos],
            'color': self.color,
            'x_value': (pos % 8) + 1,
            'y_value': int(pos/8) + 1,
            'position': pos
        }
        check_probe = {
            'layout': [],
            'can_castle_left': False,
            'can_castle_right': False
        }
        for idx in range(64):
            if self.probe['layout'][idx] != '' and self.color != helper.find_color(self.probe['layout'][idx]):
                check_probe['layout'] = list(self.probe['layout'])
                selected_piece = {
                    'name': self.probe['layout'][idx],
                    'color': helper.find_color(self.probe['layout'][idx]),
                    'x_value': (idx % 8) + 1,
                    'y_value': int(idx/8) + 1,
                    'position': idx
                }

                piece_name = self.probe['layout'][idx][0]
                if piece_name == 'P':
                    checked = pieces.move_pawn(selected_piece, target_square, check_probe)
                    if checked:
                        #print(idx)
                        return True
                if piece_name == 'R':
                    checked = pieces.move_rook(selected_piece, target_square, check_probe)
                    if checked:
                        #print(idx, selected_piece, target_square, check_probe, self.probe['layout'])
                        return True
                if piece_name == 'N':
                    checked = pieces.move_knight(selected_piece, target_square, check_probe)
                    if checked:
                        #print(idx)
                        return True
                if piece_name == 'B':
                    checked = pieces.move_bishop(selected_piece, target_square, check_probe)
                    if checked:
                        #print(idx)
                        return True
                if piece_name == 'Q':
                    checked = pieces.move_queen(selected_piece, target_square, check_probe)
                    if checked:
                        return True
                if piece_name == 'K':
                    checked = pieces.move_king(selected_piece, target_square, check_probe)
                    if checked:
                        #print(idx, selected_piece, target_square, check_probe, self.probe['layout'])
                        return True
        return False

    def cant_move(self):
        for idx in range(64):
            if self.layout[idx] != '' and self.color == helper.find_color(self.layout[idx]):
                selected_piece = {
                    'name': self.layout[idx],
                    'color': helper.find_color(self.layout[idx]),
                    'x_value': (idx % 8) + 1,
                    'y_value': int(idx/8) + 1,
                    'position': idx
                }
                for idx in range(64):
                    target_square = {
                        'name': self.layout[idx],
                        'color': helper.find_color(self.layout[idx]),
                        'x_value': (idx % 8) + 1,
                        'y_value': int(idx/8) + 1,
                        'position': idx
                    }
                    piece_name = selected_piece['name'][0]
                    if piece_name == 'P':
                        moved = pieces.move_pawn(selected_piece, target_square, self.probe)
                        if moved and not(self.was_checked()):
                            return False
                    elif piece_name == 'R':
                        moved = pieces.move_rook(selected_piece, target_square, self.probe)
                        if moved and not(self.was_checked()):
                            return False
                    elif piece_name == 'N':
                        moved = pieces.move_knight(selected_piece, target_square, self.probe)
                        if moved and not(self.was_checked()):
                            return False
                    elif piece_name == 'B':
                        moved = pieces.move_bishop(selected_piece, target_square, self.probe)
                        if moved and not(self.was_checked()):
                            return False
                    elif piece_name == 'Q':
                        moved = pieces.move_queen(selected_piece, target_square, self.probe)
                        if moved and not(self.was_checked()):
                            return False
                    elif piece_name == 'K':
                        moved = pieces.move_king(selected_piece, target_square, self.probe)
                        if moved and not(self.was_checked()):
                            return False
                    self.probe['layout'] = list(self.layout)
        return True

    def find_check_type(self):
        if self.was_checked():
            return 'checkmate' if self.cant_move() else 'check'
        else:
            return 'stalemate' if self.cant_move() else ''
