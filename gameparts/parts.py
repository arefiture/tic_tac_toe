# Объявить класс.
class Board:
    """Класс, который описывает игровое поле"""
    field_size = 3
    __save_file = 'results.txt'

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    # Метод, который обрабатывает ходы игроков.
    def make_move(self, row, col, player):
        self.board[row][col] = player

    # Метод, который отрисовывает игровое поле.
    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def __str__(self) -> str:
        return (
            'Объект игрового поля размером '
            f'{self.field_size}x{self.field_size}'
        )

    def is_board_full(self):
        for row in range(self.field_size):
            for column in range(self.field_size):
                if self.board[row][column] == ' ':
                    return False
        return True

    def check_win(self, player, row, col):
        # Проверка строки и колонки относительно прошлого хода
        if (
            all([self.board[row][col] == player
                 for col in range(self.field_size)])
        ) or (
            all([self.board[row][col] == player
                 for row in range(self.field_size)])
        ):
            return True
        # Ну и диагональ, если элемент лежит на ...
        # Главной диагонали
        if row == col and all(
            [self.board[line][line] == player
             for line in range(self.field_size)]
        ):
            return True
        # Побочной диагонали
        if row + col == self.field_size - 1 and all(
            [self.board[line][self.field_size - 1 - line] == player
             for line in range(self.field_size)]
        ):
            return True
        return False

    def save_result(self, data: str) -> None:
        with open(self.__save_file, 'a', encoding='utf-8') as file:
            file.write(data + '\n')
