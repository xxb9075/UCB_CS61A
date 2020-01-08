def create_row(size):
    """Returns a single, empty row with the given size. Each empty spot is
    represented by the string '-'.

    >>> create_row(5)
    ['-', '-', '-', '-', '-']
    """
    def create_dash(size, row=None):
        if row is None:
            row = []
        if size == 0:
            return row
        if size == 1:
            row.append('-')
            return row
        else:
            row.append('-')
            return create_dash(size-1, row)
    return create_dash(size)



def create_board(rows, columns):
    """Returns a board with the given dimensions.

    >>> create_board(3, 5)
    [['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-']]
    """
    board = []
    def create_columns(rows):
        if rows == 1:
            board.append(create_row(columns))
            return board
        else:
            board.append(create_row(columns))
            return create_columns(rows-1)
    return create_columns(rows)



def replace_elem(lst, index, elem):
    """Create and return a new list whose elements are the same as those in
    LST except at index INDEX, which should contain element ELEM instead.

    >>> old = [1, 2, 3, 4, 5, 6, 7]
    >>> new = replace_elem(old, 2, 8)
    >>> new
    [1, 2, 8, 4, 5, 6, 7]
    >>> new is old   # check that replace_elem outputs a new list
    False
    """
    assert index >= 0 and index < len(lst), 'Index is out of bounds'
    lst_new = lst[:]
    lst_new[index] = elem
    return lst_new


def get_piece(board, row, column):
    """Returns the piece at location (row, column) in the board.

    >>> rows, columns = 2, 2
    >>> board = create_board(rows, columns)
    >>> board = put_piece(board, rows, 0, 'X')[1] # Puts piece "X" in column 0 of board and updates board
    >>> board = put_piece(board, rows, 0, 'O')[1] # Puts piece "O" in column 0 of board and updates board
    >>> get_piece(board, 1, 0)
    'X'
    >>> get_piece(board, 1, 1)
    '-'
    """
    return board[row][column]


def put_piece(board, max_rows, column, player):
    """Puts PLAYER's piece in the bottommost empty spot in the given column of
    the board. Returns a tuple of two elements:

        1. The index of the row the piece ends up in, or -1 if the column
           is full.
        2. The new board

    >>> rows, columns = 2, 2
    >>> board = create_board(rows, columns)
    >>> row, new_board = put_piece(board, rows, 0, 'X')
    >>> row
    1
    >>> row, new_board = put_piece(new_board, rows, 0, 'O')
    >>> row
    0
    >>> row, new_board = put_piece(new_board, rows, 0, 'X')
    >>> row
    -1
    """
    lst_new = board[:]
    i = max_rows-1
    while i >= 0:
        if get_piece(board, i, column) == '-':
            lst_new[i] = replace_elem(lst_new[i], column, player)
            break
        else:
            i -= 1
    return i, lst_new

rows, columns = 2, 2
board = create_board(rows, columns)
row, new_board = put_piece(board, rows, 0, 'X')
print(row)
row, new_board = put_piece(new_board, rows, 0, 'O')
print(row)
# row, new_board = put_piece(new_board, rows, 0, 'X')
# print(row)
