from pieces import check, create_desk, display_desk, Pawn, Rook, Knight, Bishop, Queen, King, LETTERS

desk = create_desk('white')

# for i in range(8):
#     desk[1][i] = Pawn(colour='black', position=f'{LETTERS[i]}7', step=-1)
#     desk[6][i] = Pawn(colour='white', position=f'{LETTERS[i]}2', step=1)
#
#
# desk[0][0], desk[0][7] = Rook(colour='black', position='a8'), Rook(colour='black', position='h8')
# desk[7][0], desk[7][7] = Rook(colour='white', position='a1'), Rook(colour='white', position='h1')
#
# desk[0][1], desk[0][6] = Knight(colour='black', position='b8'), Knight(colour='black', position='g8')
# desk[7][1], desk[7][6] = Knight(colour='white', position='b1'), Knight(colour='white', position='g1')
#
# desk[0][2], desk[0][5] = Bishop(colour='black', position='c8'), Bishop(colour='black', position='f8')
# desk[7][2], desk[7][5] = Bishop(colour='white', position='c1'), Bishop(colour='white', position='f1')
#
# desk[7][3], desk[0][3] = Queen(colour='white', position='d1'), Queen(colour='black', position='d8')
# desk[7][4], desk[0][4] = King(colour='white', position='d1'), King(colour='black', position='d8')

# desk[7][4], desk[0][4] = King(colour='white', position='d1'), King(colour='black', position='d8')
# desk[6][4] = Rook(colour='white', position='e2')

print(check(desk, 'black'))