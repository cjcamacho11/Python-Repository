#xgv3cj Christian Camacho
def mean_all(table):
    count = 0
    total = 0
    for sublist in table:
        for c in sublist:
            total += c
            count += 1
    return total / count
'''This function adds up all numbers within the given table and takes the average of it'''

def mean_by_row(table):
    rowmeans = []
    avg = 0
    for sublist in table:
        total = 0
        count = 0
        for value in sublist:
            total += value
            count += 1
            avg = total / count
        rowmeans.append(avg)
    return rowmeans
'''This function takes in a table and adds up all the values 
of the row in the given table and returns the average of it'''
def mean_by_col(table):
    colmeans = []
    for index in range(len(table[0])):
        total = 0
        count = 0
        for element in table:
            total += element[index]
            count += 1
        avg = total / count
        colmeans.append(avg)
    return colmeans
'''this function takes in a table and takes the average of the values within their respective columns 
and returns it'''


