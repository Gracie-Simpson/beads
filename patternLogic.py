def advance(matrix, row, column):
    if(column+1 < len(matrix[row])):
        column += 1
    elif(column+1 >= len(matrix[row]) and row+1 < len(matrix)):
        row += 1
        column = 0
    else:
        row = 0
        column = 0
    return row,column


def regress(matrix, row, column):
    if(column-1 >= 0):
        column -= 1
    elif(column-1 < 0 and row-1 >= 0):
        row -= 1
        column = len(matrix[row])-1
    else:
        row = len(matrix)-1
        column = len(matrix[len(matrix)-1])-1
    return row,column


def regress_row(matrix, row, past_column, current_column, future_column):
    if(row-1 >= 0):
        row -= 1
        past_column = current_column = future_column = len(matrix[row])-1
    else:
        row = len(matrix)-1
        past_column = current_column = future_column = len(matrix[len(matrix)-1])-1
    return row, past_column, current_column, future_column


def advance_row(matrix, row, past_column, current_column, future_column):
    if (row+1 < len(matrix)):
        row += 1
        past_column = current_column = future_column = len(matrix[row])-1
    else:
        row = 0
        past_column = current_column = future_column = len(matrix[row])-1
    return row, past_column, current_column, future_column