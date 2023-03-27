'''DESCRIPTION:
Given an array arr of strings, complete the function by calculating the total perimeter of all the islands. Each piece of land will be marked with 'X' while the water fields are represented as 'O'. Consider each tile being a perfect 1 x 1 piece of land. Some examples for better visualization:

['XOOXO',
 'XOOXO',
 'OOOXO',
 'XXOXO',
 'OXOOO'] 
which represents:

should return: "Total land perimeter: 24".

'''

def land_perimeter(arr):
    perimeter=0
    row = len(arr)
    col = len(arr[0])
    for i in range(row):
        for j in range(col):
            if arr[i][j] == 'X':
                if i == 0 or arr[i-1][j] == 'O':
                    perimeter += 1
                if i == row-1 or arr[i+1][j] == 'O':
                    perimeter += 1
                if j == 0 or arr[i][j-1] == 'O':
                    perimeter += 1
                if j == col-1 or arr[i][j+1] == 'O':
                    perimeter += 1
    return "Total land perimeter: " + str(perimeter)

print(land_perimeter(['XOOXO',
'XOOXO',
'OOOXO',
'XXOXO',
'OXOOO'] ))