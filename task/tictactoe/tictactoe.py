user_stage = '_________'  # input('Enter cells: > ')
step_turn1 = 'X'
step_turn2 = 'O'


def populate_field(ustage):
    print('---------')
    print('|', *ustage[0:3], '|', sep=' ')
    print('|', *ustage[3:6], '|', sep=' ')
    print('|', *ustage[6:9], '|', sep=' ')
    print('---------')


def status(ustage):
    my_list = [ustage[2] + ustage[4] + ustage[6],
               ustage[0] + ustage[4] + ustage[8],
               ustage[0:3],
               ustage[3:6],
               ustage[6:9],
               ustage[0] + ustage[3] + ustage[6],
               ustage[1] + ustage[4] + ustage[7],
               ustage[2] + ustage[5] + ustage[8]]
    # print(my_list)
    x3_count = my_list.count('XXX')
    o3_count = my_list.count('OOO')
    if abs(ustage.count('O') - ustage.count('X')) > 1 or x3_count + o3_count > 1:
        print('Impossible')
        return 'stop'
    elif x3_count == 0 and o3_count == 0:
        if '_' not in ustage:
            print('Draw')
            return 'stop'
        else:
            # print('Game not finished')
            return 'go'
    elif x3_count == 1:
        print('X wins')
        return 'stop'
    elif o3_count == 1:
        print('O wins')
        return 'stop'
    else:
        print('Impossible')
        return 'stop'


def next_step(ustage, ucolumn, urow):
    global user_stage, step_turn1, step_turn2
    if urow == 3:
        new_index = ucolumn - 1
    elif urow == 2:
        new_index = ucolumn + 2
    else:
        new_index = ucolumn + 5

    ulist = list(ustage)
    if ulist[new_index] == '_':
        ulist[new_index] = step_turn1
        (step_turn1, step_turn2) = (step_turn2, step_turn1)
        user_stage = ''.join(ulist)
        populate_field(user_stage)
        return status(user_stage)
    else:
        print('This cell is occupied! Choose another one!')
        return 'go'


def step():
    col_row_list = list(input('Enter the coordinates: > ').strip().split())
    if ''.join(col_row_list).isdigit():
        if int(col_row_list[0]) < 4 and int(col_row_list[1]) < 4:
            return next_step(user_stage, int(col_row_list[0]), int(col_row_list[1]))
        else:
            print('Coordinates should be from 1 to 3!')
            return 'go'
    else:
        print('You should enter numbers!')
        return 'go'


populate_field(user_stage)
# status(user_stage)

state = 'go'
while state != 'stop':
    state = step()
