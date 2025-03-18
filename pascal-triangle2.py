def pascal(row, column):
    if column == 0:
        return 1
    elif row == 0:
        return 0
    else:
        return pascal(row-1, column) + pascal(row-1, column-1)
    
print(pascal(5,4))