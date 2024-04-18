game_zone = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]


def show_zone():  #функция отображения поля на текущий момент
    print(f'  │ 0 │ 1 │ 2 │')
    print('--│------------')
    print(f'0 │ {game_zone[0][0]} │ {game_zone[0][1]} │ {game_zone[0][2]} │')
    print('  -------------')
    print(f'1 │ {game_zone[1][0]} │ {game_zone[1][1]} │ {game_zone[1][2]} │')
    print('  -------------')
    print(f'2 │ {game_zone[2][0]} │ {game_zone[2][1]} │ {game_zone[2][2]} │')
    print('  -------------')


def step_player1(): #ход первого игрока с проверкой занятности и диапазона
    while True:
        x, y = input('Введите две координаты через пробел, а затем повтороно введите в следующем окне: ').split()
        x, y = int(x), int(y)
        if 0 <= x <= 2 and 0 <= y <= 2:
            if game_zone[x][y] == ' ' and game_zone[x][y] != 0:
                return x, y
            else:
                print('Клетка занята! ')
        else:
            print('Координаты вне диапазона ')


def step_player2(): #ход второго игрока с проверкой занятности и диапазона
    while True:
        x1, y1 = input('Введите две координаты через пробел, а затем повтороно введите в следующем окне: ').split()
        x1, y1 = int(x1), int(y1)
        if 0 <= x1 <= 2 and 0 <= y1 <= 2:
            if game_zone[x1][y1] == ' ' and game_zone[x1][y1] != 'x':
                return x1, y1
            else:
                print('Клетка занята! ')
        else:
            print('Координаты вне диапазона ')




def printing_stepPlayer1(): # функция печати хода первого игрока
    x, y = step_player1()
    if x == 0 and y == 0:
        game_zone[0][0] = 'x'
    elif x == 0 and y == 1:
        game_zone[0][1] = 'x'
    elif x == 0 and y == 2:
        game_zone[0][2] = 'x'
    elif x == 1 and y == 0:
        game_zone[1][0] = 'x'
    elif x == 1 and y == 1:
        game_zone[1][1] = 'x'
    elif x == 1 and y == 2:
        game_zone[1][2] = 'x'
    elif x == 2 and y == 0:
        game_zone[2][0] = 'x'
    elif x == 2 and y == 1:
        game_zone[2][1] = 'x'
    elif x == 2 and y == 2:
        game_zone[2][2] = 'x'


def printing_stepPlayer2():
    x1, y1 = step_player2()
    if x1 == 0 and y1 == 0:
        game_zone[0][0] = 0
    elif x1 == 0 and y1 == 1:
        game_zone[0][1] = 0
    elif x1 == 0 and y1 == 2:
        game_zone[0][2] = 0
    elif x1 == 1 and y1 == 0:
        game_zone[1][0] = 0
    elif x1 == 1 and y1 == 1:
        game_zone[1][1] = 0
    elif x1 == 1 and y1 == 2:
        game_zone[1][2] = 0
    elif x1 == 2 and y1 == 0:
        game_zone[2][0] = 0
    elif x1 == 2 and y1 == 1:
        game_zone[2][1] = 0
    elif x1 == 2 and y1 == 2:
        game_zone[2][2] = 0



def chek_winning(): # проверка выйгрышной комбинации
    while True:
        if game_zone[0][0]=='x' and game_zone[0][1]=='x' and game_zone[0][2]=='x':
            print('Игра окончена!')
            return False
        elif game_zone[0][0]== 0 and game_zone[0][1]== 0  and game_zone[0][2]==  0:
            print('Игра окончена!')
            return False
        elif game_zone[1][0]=='x' and game_zone[1][1]=='x' and game_zone[1][2]=='x':
            print('Игра окончена!')
            return False
        elif game_zone[1][0]== 0 and game_zone[1][1]== 0  and game_zone[1][2]==  0:
            print('Игра окончена!')
            return False
        elif game_zone[2][0]=='x' and game_zone[2][1]=='x' and game_zone[2][2]=='x':
            print('Игра окончена!')
            return False
        elif game_zone[2][0] == 0 and game_zone[2][1] == 0 and game_zone[2][2] == 0:
            print('Игра окончена!')
            return False
        elif game_zone[0][0] == 'x' and game_zone[1][1] == 'x' and game_zone[2][2] == 'x':
            print('Игра окончена!')
            return False
        elif game_zone[0][0] == 0 and game_zone[1][1] == 0 and game_zone[2][2] == 0:
            print('Игра окончена!')
            return False

while True:
    show_zone()
    step_player1()
    printing_stepPlayer1()
    show_zone()
    step_player2()
    printing_stepPlayer2()
    show_zone()
    show_zone()
    step_player1()
    printing_stepPlayer1()
    show_zone()
    step_player2()
    printing_stepPlayer2()
    show_zone()
    show_zone()
    step_player1()
    printing_stepPlayer1()
    show_zone()
    chek_winning()
    if chek_winning() == False:
        break
    break

    step_player2()
    printing_stepPlayer2()
    show_zone()
    chek_winning()
    if chek_winning() == False:
        break
    break
    step_player1()
    printing_stepPlayer1()
    show_zone()
    chek_winning()
    if chek_winning() == False:
        break
    break
    step_player2()
    printing_stepPlayer2()
    show_zone()
    chek_winning()
    if chek_winning() == False:
        break
    break