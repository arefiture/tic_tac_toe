class FieldIndexError(IndexError):
    """Исключение на ход вне поля"""
    def __str__(self) -> str:
        return 'Введено значение за границами игрового поля'


class CellOccupiedError(Exception):
    """Исключение на ход в занятое пространство"""
    def __str__(self) -> str:
        return 'Попытка изменить занятую ячейку'
