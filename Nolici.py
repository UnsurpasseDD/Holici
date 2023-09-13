pole = [[' ' for _ in range(3)] for _ in range(3)]



def print_board():
    for row in pole:
        print('|'.join(row))
        print('-----')



def check_win(board):
    for row in pole:
        if all([cell == board for cell in row]):
            return True
    for col in range(3):
        if all([pole[row][col] == board for row in range(3)]):
            return True
    if pole[0][0] == pole[1][1] == pole[2][2] == board:
        return True
    if pole[0][2] == pole[1][1] == pole[2][0] == board:
        return True
    return False



def check_not_win():
    return all([cell != ' ' for row in pole for cell in row])



hod = 0
end_game = False

while not end_game:
    print_board()
    if hod % 2 == 0:
        user = 'X'
    else:
        user = 'O'

    print(f"Ход игрока {user}")
    row = int(input("Введите номер строки (0, 1, 2): "))
    col = int(input("Введите номер столбца (0, 1, 2): "))

    if pole[row][col] == ' ':
        pole[row][col] = user
        hod += 1
    else:
        print("Эта клетка уже занята. Попробуйте снова.")

    if check_win(user):
        print_board()
        print(f"Игрок {user} выиграл!")
        конец_игры = True
    elif check_not_win():
        print_board()
        print("Ничья!")
        end_game = True