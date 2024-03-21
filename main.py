from pieces import check, create_desk, display_desk

new_game = True
while new_game:
    game = input('Start new game?(y/n)')
    if game == 'n':
        new_game = False
    else:
        game = True

    your_colour = input('Choose your colour: ')
    desk = create_desk(your_colour)
    display_desk(desk)

