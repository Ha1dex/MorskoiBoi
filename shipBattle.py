import random


# Создаем игровое поле размером 10x10
def create_board():
    board = []
    for _ in range(10):
        row = ["O"] * 10  # "O" обозначает пустое место
        board.append(row)
    return board


# Выводим игровое поле
def print_board(board, hide_computer_ships=False):
    header = "  A B C D E F G H I J"
    print(header)
    for i, row in enumerate(board):
        print_row = []
        for cell in row:
            if hide_computer_ships and cell == "S":
                print_row.append("O")  # Если корабль компьютера должен быть скрыт, заменяем "S" на "O"
            else:
                print_row.append(cell)
        print(f"{i + 1} {' '.join(print_row)}")


