map = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

pobeda = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


# Вывод карты на экран
def print_maps():
    print(map[0], end=" ")
    print(map[1], end=" ")
    print(map[2])

    print(map[3], end=" ")
    print(map[4], end=" ")
    print(map[5])

    print(map[6], end=" ")
    print(map[7], end=" ")
    print(map[8])


# Сделать ход в ячейку
def step_maps(step, symbol):
    ind = map.index(step)
    map[ind] = symbol


# Получить текущий результат игры
def get_result():
    win = ""

    for i in pobeda:
        if map[i[0]] == "X" and map[i[1]] == "X" and map[i[2]] == "X":
            win = "X"
        if map[i[0]] == "O" and map[i[1]] == "O" and map[i[2]] == "O":
            win = "O"

    return win


# Основная программа
game_over = False
player1 = True
j = 0

while game_over == False:

    print_maps()

    if player1 == True:
        symbol = "X"
        step = int(input("Игрок X, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Игрок O, ваш ход: "))
    j = j + 1
    step_maps(step, symbol)
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False
        if j == 9 or j > 9:
            game_over = True
    player1 = not (player1)


print_maps()
if j == 9 or j > 9:
    print("Ничья")
else:
    print("Победил", win)