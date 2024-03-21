LETTERS = 'abcdefgh'
DESK_SIZE = 8


def get_index(position):  # get 'a2', return (6, 0), like index in python list
    i = DESK_SIZE - int(position[1])
    j = LETTERS.index(position[0])
    return i, j


def get_chess_cords(i, j):  # get (6, 0), return 'a2'
    return LETTERS[j] + str(DESK_SIZE - i)


class Piece:
    def __init__(self, colour, position):
        self.colour = colour
        self.position = position


class Pawn(Piece):
    def __init__(self, colour, position, step):  # step костиль
        super().__init__(colour, position)
        self.step = step
        self.start_position = position

    def __str__(self):
        return "bp" if self.colour == 'black' else "wp"

    def available_moves(self, desk):
        moves = []
        i, j = get_index(self.position)

        # move
        if desk[i - self.step][j] == '':
            moves.append(get_chess_cords(i - self.step, j))
        if desk[i - 2 * self.step][j] == '' and (i, j) == get_index(self.start_position):
            moves.append(get_chess_cords(i - 2 * self.step, j))

        # attack
        if j < (DESK_SIZE - 1) and desk[i - self.step][j + 1] != '' and desk[i - self.step][
            j + 1].colour != self.colour:
            moves.append(get_chess_cords(i - self.step, j + 1))
        if j > 0 and desk[i - self.step][j - 1] != '' and desk[i - self.step][j - 1].colour != self.colour:
            moves.append(get_chess_cords(i - self.step, j - 1))

        return moves


class Rook(Piece):

    def __str__(self):
        return "br" if self.colour == 'black' else "wr"

    def available_moves(self, desk):  # f5
        moves = []
        i, j = get_index(self.position)

        for c in range(1, DESK_SIZE - j):
            if desk[i][j + c] != '':
                if desk[i][j + c].colour != self.colour:
                    moves.append(get_chess_cords(i, j + c))
                break
            moves.append(get_chess_cords(i, j + c))

        for c in range(1, j + 1):
            if desk[i][j - c] != '':
                if desk[i][j - c].colour != self.colour:
                    moves.append(get_chess_cords(i, j - c))
                break
            moves.append(get_chess_cords(i, j - c))

        for c in range(1, DESK_SIZE - i):
            if desk[i + c][j] != '':
                if desk[i + c][j].colour != self.colour:
                    moves.append(get_chess_cords(i + c, j))
                break
            moves.append(get_chess_cords(i + c, j))

        for c in range(1, i + 1):
            if desk[i - c][j] != '':
                if desk[i - c][j].colour != self.colour:
                    moves.append(get_chess_cords(i - c, j))
                break
            moves.append(get_chess_cords(i - c, j))

        return moves


class Knight(Piece):

    def __str__(self):
        return 'bkn' if self.colour == 'black' else 'wkn'

    def available_moves(self, desk):
        moves = []
        i, j = get_index(self.position)
        if i - 2 >= 0:
            if j + 1 < DESK_SIZE:
                if desk[i - 2][j + 1] == '' or desk[i - 2][j + 1].colour != self.colour:
                    moves.append(get_chess_cords(i - 2, j + 1))
            if j - 1 >= 0:
                if desk[i - 2][j - 1] == '' or desk[i - 2][j - 1].colour != self.colour:
                    moves.append(get_chess_cords(i - 2, j - 1))
        if i - 1 >= 0:
            if j + 2 < DESK_SIZE:
                if desk[i - 1][j + 2] == '' or desk[i - 1][j + 2].colour != self.colour:
                    moves.append(get_chess_cords(i - 1, j + 2))
            if j - 2 >= 0:
                if desk[i - 1][j - 2] == '' or desk[i - 1][j - 2].colour != self.colour:
                    moves.append(get_chess_cords(i - 1, j - 2))
        if i + 2 < DESK_SIZE:
            if j + 1 < DESK_SIZE:
                print(desk[i + 2][j + 1])
                if desk[i + 2][j + 1] == '' or desk[i + 2][j + 1].colour != self.colour:
                    moves.append(get_chess_cords(i + 2, j + 1))
            if j - 1 >= 0:
                if desk[i + 2][j - 1] == '' or desk[i + 2][j - 1].colour != self.colour:
                    moves.append(get_chess_cords(i + 2, j - 1))
        if i + 1 < DESK_SIZE:
            if j + 2 < DESK_SIZE:
                if desk[i + 1][j + 2] == '' or desk[i + 1][j + 2].colour != self.colour:
                    moves.append(get_chess_cords(i + 1, j + 2))
            if j - 2 >= 0:
                if desk[i + 1][j - 2] == '' or desk[i + 1][j - 2].colour != self.colour:
                    moves.append(get_chess_cords(i + 1, j - 2))

        return moves


class Bishop(Piece):

    def __str__(self):
        return 'bb' if self.colour == 'black' else 'wb'

    def available_moves(self, desk):
        moves = []
        i, j = get_index(self.position)

        limit = None
        if DESK_SIZE - j <= DESK_SIZE - i:
            limit = DESK_SIZE - j
        else:
            limit = DESK_SIZE - i
        for c in range(1, limit):
            if desk[i + c][j + c] != '':
                if desk[i + c][j + c].colour != self.colour:
                    moves.append(get_chess_cords(i + c, j + c))
                break
            moves.append(get_chess_cords(i + c, j + c))

        if j + 1 <= DESK_SIZE - i:
            limit = j + 1
        else:
            limit = DESK_SIZE - i
        for c in range(1, limit):
            if desk[i + c][j - c] != '':
                if desk[i + c][j - c].colour != self.colour:
                    moves.append(get_chess_cords(i + c, j - c))
                break
            moves.append(get_chess_cords(i + c, j - c))

        if DESK_SIZE - j <= i + 1:
            limit = DESK_SIZE - j
        else:
            limit = i + 1
        for c in range(1, limit):
            if desk[i - c][j + c] != '':
                if desk[i - c][j + c].colour != self.colour:
                    moves.append(get_chess_cords(i - c, j + c))
                break
            moves.append(get_chess_cords(i - c, j + c))

        if j + 1 <= i + 1:
            limit = j + 1
        else:
            limit = i + 1
        for c in range(1, limit):
            if desk[i - c][j - c] != '':
                if desk[i - c][j - c].colour != self.colour:
                    moves.append(get_chess_cords(i - c, j - c))
                break
            moves.append(get_chess_cords(i - c, j - c))

        return moves


class Queen(Piece):
    def __str__(self):
        return 'bq' if self.colour == 'black' else 'wq'

    def available_moves(self, desk):
        moves = []
        rook = Rook(self.colour, self.position)
        bishop = Bishop(self.colour, self.position)
        moves += rook.available_moves(desk)
        moves += bishop.available_moves(desk)
        return moves


class King(Piece):
    def __str__(self):
        return 'bk' if self.colour == 'black' else 'wk'

    def available_moves(self, desk):
        moves = []
        i, j = get_index(self.position)
        for step_y in range(-1, 2):
            for step_x in range(-1, 2):
                if DESK_SIZE >= j - step_x >= 0 and desk[i - step_y][j - step_x] == '':
                    moves.append(get_chess_cords(i - step_y, j - step_x))
                elif desk[i - step_y][j - step_x] != '' and desk[i - step_y][j - step_x].colour != self.colour:
                    moves.append(get_chess_cords(i - step_y, j - step_x))
        moves.remove(self.position)
        return moves


def check(desk, colour_op):
    colour_your = 'white' if colour_op == 'black' else 'black'
    all_available_moves = []
    for i in desk:
        for piece in i:
            if piece != '':
                if piece.colour == colour_op:
                    for piece.position in piece.available_moves(desk):
                        if not (piece.position in all_available_moves):
                            all_available_moves.append(piece.position)

    king_position = None
    for i in desk:
        for piece in i:
            if type(piece) == King and piece.colour == colour_your:
                king_position = piece.position
    if king_position in all_available_moves:
        return True
    return False


def move(desk, piece, move):
    if move in piece.available_moves(desk):
        i, j = get_index(piece.position)
        i1, j1 = get_index(move)
        desk[i][j] = ''
        desk[i1][1] = 'piece'


def create_desk(your_colour):
    colour_op = 'black' if your_colour == 'white' else 'white'
    desk = [[' '] * DESK_SIZE for i in range(DESK_SIZE)]

    for i in range(8):
        desk[1][i] = Pawn(colour=colour_op, position=f'{LETTERS[i]}7', step=-1)
        desk[6][i] = Pawn(colour=your_colour, position=f'{LETTERS[i]}2', step=1)

    desk[0][0], desk[0][7] = Rook(colour=colour_op, position='a8'), Rook(colour=colour_op, position='h8')
    desk[7][0], desk[7][7] = Rook(colour=your_colour, position='a1'), Rook(colour=your_colour, position='h1')

    desk[0][1], desk[0][6] = Knight(colour=colour_op, position='b8'), Knight(colour=colour_op, position='g8')
    desk[7][1], desk[7][6] = Knight(colour=your_colour, position='b1'), Knight(colour=your_colour, position='g1')

    desk[0][2], desk[0][5] = Bishop(colour=colour_op, position='c8'), Bishop(colour=colour_op, position='f8')
    desk[7][2], desk[7][5] = Bishop(colour=your_colour, position='c1'), Bishop(colour=your_colour, position='f1')

    desk[7][3], desk[0][3] = Queen(colour=your_colour, position='d1'), Queen(colour=colour_op, position='d8')
    desk[7][4], desk[0][4] = King(colour=your_colour, position='d1'), King(colour=colour_op, position='d8')

    return desk


def display_desk(desk):
    displayed_desk = [[''] * 8 for i in range(DESK_SIZE)]
    for j in range(DESK_SIZE):
        max_len = 0
        for i in range(DESK_SIZE):
            if len(str(desk[i][j])) > max_len:
                max_len = len(str(desk[i][j]))
        for i in range(DESK_SIZE):
            if len(str(desk[i][j])) < max_len:
                displayed_desk[i][j] = str(desk[i][j]) + ' ' * (max_len - len(str(desk[i][j])))
            else:
                displayed_desk[i][j] = str(desk[i][j])
    for i in displayed_desk:
        print(i)


