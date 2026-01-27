import math
import random
def randomSearch(items:list, target) -> int:
    tries = 0
    while True:
        index = random.randint(0, len(items) - 1)
        # print(index)
        if items[index] == target:
            break
        tries+=1
    #Modify the below function such that it takes in a list of items and a target value.
    #Randomly choose an item from the list and if it isn't the target value try again.
    #print out the amount of tries it took and return the index of the target value
    print(tries)
    return index

def linearSearch(items:list, target) ->tuple[int,int]:
    #Modify the below function such that it implements linear search.
    #Return the index of the target value and the amount of checks it took
    #if the value is not within the list return -1 as the index.
    # print(target)
    checks = 0
    for item in items:
        checks += 1
        # print("item stuff", item, ", ", i)
        if item == target:
            # print("returned: ", i, ", ", i+1)
            return checks - 1, checks
    return -1, checks
# print("search", linearSearch([1,3,4,5,6,7,8,9],9))
# assert linearSearch([1,3,4,5,6,7,8,9],1)==(0,1)
# assert linearSearch([1,3,4,5,6,7,8,9],9)==(7,8)
# assert linearSearch([1,3,4,5,6,7,8,10],9)==(-1,8)

def binarySearch(items:list, target) -> tuple[int,int]:
    # Modify the below function such that it implements linear search.
    # Return the index of the target value and the amount of checks it took
    # if the value is not within the list return -1 as the index.
    checks = 0
    low = 0
    high = len(items) - 1
    # debug state check
    # print("state check = pre-loop", " checks = ", checks, " low = ", low, " high = ", high)

    while low <= high:
        checks += 1   # every loop, add one to the checks6
        mid = ((low + high) / 2).__floor__()    # index that is the center of range, rounded down
        mid_value = items[mid]
        print("looping, checks: ", checks, " low = ", low, " high = ", high, " mid = ", mid, " mid_value = ", mid_value)
        if target == mid_value:
            print("target = mid_value")
            return mid, checks
        elif target < mid_value:
            print("target < mid_value")
            high = mid - 1
        else: # target > mid_value
            print("target > mid_value")
            low = mid + 1
    return -1, checks

test0 = binarySearch([1,3,5,7,9],5)
print(test0)
assert binarySearch([1,3,5,7,9],5) == (2,1)

test1 = binarySearch([1,3,5,7,9],7)
print(test1)
assert test1 == (3,2)

test2 = binarySearch([1,3,5,7,9],9)
print(test2)
assert binarySearch([1,3,5,7,9],9) == (4,3)
test3 = binarySearch([1,3,5,7,9],1)
print(test3)
assert binarySearch([1,3,5,7,9],1) == (0,2) # originally was (0,2), but doing it manually, it should be 0,3
test4 = binarySearch([1,3,5,7,9],3)
print(test4)
assert binarySearch([1,3,5,7,9],3) == (1,3) # same as above but (1,3) -> (1,2)
test5 = binarySearch([1,3,5,7,9],10)
print(test5)
assert binarySearch([1,3,5,7,9],10) == (-1,3)

