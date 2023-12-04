import random


# Создаем игровое поле размером 10x10
def create_board():
    board = []
    for _ in range(10):
        row = ["O"] * 10
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
                print_row.append("O")
            else:
                print_row.append(cell)
        print(f"{i + 1} {' '.join(print_row)}")

        # Размещаем корабли на поле
        def place_ships(board):
            def place_ships(board):
                ships = {
                    "Aircraft Carrier": 4,
                    "Battleship": 3,
                    "Submarine": 2,
                    "Destroyer": 2,
                    "Patrol Boat": 1,
                }
                for ship, size in ships.items():
                    place_ship(board, ship, size)

        # Размещаем один корабль на поле
        def place_ship(board, ship, size):
            while True:
                orientation = random.choice(["horizontal", "vertical"])
                if orientation == "horizontal":
                    row = random.randint(0, 9)
                    col = random.randint(0, 10 - size)
                else:
                    row = random.randint(0, 10 - size)
                    col = random.randint(0, 9)
                if is_valid_placement(board, row, col, orientation, size):
                    if orientation == "horizontal":
                        for i in range(size):
                            board[row][col + i] = "S"  # "S" обозначает корабль
                    else:
                        for i in range(size):
                            board[row + i][col] = "S"  # "S" обозначает корабль
                    break

        # Проверяем, можно ли разместить корабль в данной позиции
        def is_valid_placement(board, row, col, orientation, size):
            def is_neighboring(row, col):
                # Проверяет, есть ли соседние клетки (верх, вниз, влево, вправо, диагональ)
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                    r, c = row + dr, col + dc
                    if 0 <= r < 10 and 0 <= c < 10 and board[r][c] != "O":
                        return True
                return False

            if orientation == "horizontal":
                for i in range(size):
                    if board[row][col + i] != "O" or is_neighboring(row, col + i):
                        return False
            else:
                for i in range(size):
                    if board[row + i][col] != "O" or is_neighboring(row + i, col):
                        return False
            return True

