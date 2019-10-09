#Generates a two-dimensional array
row_num = int(input("Input number of rows: ")
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

print(multi_list)
"""
multi_list = [0 for col in range(col_num)]
print(multi_list)
//"It will print 0 upto col_num(somenumber of times)"

multi_list = [[0 for col in range(col_num)] for row in range(row_num)]
print(multi_list)
//"It will print col_num upto row_num(somenumber of times)"
"""
