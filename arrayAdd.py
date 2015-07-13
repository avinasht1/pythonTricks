__author__ = 'atalanki'


# Given and array a contains all digits 0-9 a = [1, 4 , 2, 1] # which represents 1421 Add one to the number
# and return the array return a = [1, 4, 2, 2] # which represents 1422"

def arrayAdd(dataspace, pos):
    dataspace[pos] = (dataspace[pos] + 1) % 10
    if dataspace[pos] == 0:
        pos -= 1
        arrayAdd(dataspace, pos)
    return dataspace


array = [1, 4, 9, 9]
print arrayAdd(array, len(array) - 1)
