matrix = [
    [0.5, -1, 1, 6],
    [3,2, 1,6],
    [5, -1, -3, -1]
]

def show_matrix(matrix):
    for row in matrix:
        str_values = list(map(str,row))
        print(" ".join(str_values) + "\n" ,end="")

def sort_rows(matrix, target_column):
    return sorted(matrix, key=lambda row:abs(row[target_column]),reverse=True)

def get_column(matrix, column):
    return [row[column] for row in matrix]

def get_pivot(matrix, target_column):
    column_values = get_column(matrix, target_column)
    abs_values = [abs(value) for value in column_values]

    max_value = max(abs_values)
    index_pivot = abs_values.index(max_value)

    return column_values[index_pivot]

def get_multiplier(matrix, target_row, target_column, pivot):
    next_row_val = matrix[target_row][target_column]
    return next_row_val/pivot

def apply_multiplier(matrix, pivot_row, target_row, multiplier):
    for i,l2 in enumerate(matrix[target_row]):
        matrix[target_row][i] = matrix[target_row][i] - (matrix[pivot_row][i] * multiplier)

if __name__ == "__main__":

    for current_column in range(0,2):
        matrix = sort_rows(matrix,current_column) 
        pivot = get_pivot(matrix[current_column:], current_column)

        for current_row in range(current_column+1,3):
            multiplier = get_multiplier(matrix, current_row, current_column, pivot)
            apply_multiplier(matrix, current_column, current_row, multiplier)

    show_matrix(matrix)