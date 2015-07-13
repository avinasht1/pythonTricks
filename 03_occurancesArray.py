__author__ = 'atalanki'
# Find number of occurrences in sorted array
import math


def searchCount(searchString, searchArray):
    """ Counts the occurances in sorted array    """
    startIndex = 0
    endIndex = len(searchArray)
    while endIndex - startIndex:
        midIndex = (endIndex + startIndex) / 2
        print "--------------"
        print startIndex
        print midIndex
        print endIndex
        print "--------------"
        if searchString == searchArray[midIndex]:
            return midIndex
        elif searchString < searchArray[midIndex]:
            endIndex = midIndex
        else:
            startIndex = midIndex


def firstOccr(searchString, dataspace, low, high):
    while high > low:
        mid = (low + high) / 2
        print "-------------"
        print low
        print mid
        print high
        print "-------------"
        raw_input("Enter")
        if dataspace[mid] == dataspace[mid - 1] and dataspace[mid] == searchString:
            high = mid
        elif dataspace[mid] == searchString:
            return mid
        elif dataspace[mid] > searchString:
            high = mid
        else:
            low = mid
    return -1


def lastOccr(searchString, dataspace, low, high):
    while high > low:
        mid = (low + high) / 2
        print "-------------"
        print low
        print mid
        print high
        print "-------------"
        if dataspace[mid] == searchString:
            if mid == len(dataspace) - 1:
                return mid
            elif dataspace[mid] == dataspace[mid + 1]:
                low = mid
            else:
                return mid
        elif dataspace[mid] > searchString:
            high = mid
        else:
            low = mid
    return -1


def searchCountArray(searchString, searchArray):
    firstIndex = firstOccr(searchString, searchArray, 0, len(searchArray))
    return firstIndex


#     if firstIndex == -1:
#         return -1

#     lastIndex = lastOccr(searchString,searchArray,firstIndex,len(searchArray))

#     print "first index: %s" %firstIndex
#     print "last index: %s" %lastIndex
#     return lastIndex - firstIndex + 1

print searchCountArray(2, [0, 0, 1, 1, 3, 4, 5, 5, 5, 6, 7, 8, 8, 8, 9])
