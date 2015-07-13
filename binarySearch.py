__author__ = 'atalanki'


def binarySearch(searchString, dataspace):
    low = 0
    high = len(dataspace)
    while high > low:
        mid = (low + high) / 2
        print "-------------"
        print low
        print mid
        print high
        print "-------------"
        '''raw_input("Enter")'''
        if dataspace[mid] == dataspace[mid - 1] and dataspace[mid] == searchString:
            high = mid
        elif dataspace[mid] == searchString:
            return mid
        elif dataspace[mid] > searchString:
            high = mid
        else:
            low = mid
    return -1


print binarySearch(8, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 7, 8, 8, 8, 9])
