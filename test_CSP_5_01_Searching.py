import CSP_5_01_Searching as HW
def test_random_search():
    assert HW.randomSearch([1,3,5,9,7,12,11,10,2,4,6,8],5) == 2

def test_linear_search():
    assert HW.linearSearch([1,3,4,5,6,7,8,9],1)==(0,1)
    assert HW.linearSearch([1,3,4,5,6,7,8,9],9)==(7,8)
    assert HW.linearSearch([1,3,4,5,6,7,8,10],9)==(-1,8)


def test_binary_search():
    assert HW.binarySearch([1,3,5,7,9],5) == (2,1)
    assert HW.binarySearch([1,3,5,7,9],7) == (3,2)
    assert HW.binarySearch([1,3,5,7,9],9) == (4,3)
    assert HW.binarySearch([1,3,5,7,9],1) == (0,2) # originally was (0,2), but doing it manually, it should be 0,3
    assert HW.binarySearch([1,3,5,7,9],3) == (1,3) # same as above but (1,3) -> (1,2)
    assert HW.binarySearch([1,3,5,7,9],10) == (-1,3)
    li = []
    for i in range(500):
        li.append(i+1)
    assert HW.binarySearch(li,-1) == (-1, 8)
