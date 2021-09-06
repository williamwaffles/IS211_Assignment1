
def listDivide(numbers, divide = 2):
    """
    The function returns the number of elements in the numbers list that are divisibleby divide
    """


    result = 0
    for i in numbers:
        if i % divide == 0:
            result += 1
    return result

# one liner function that appears to do the same as above
# return sum(n % divide == 0 for n in numbers)

#test case for
#print(listDivide([1 ,3 ,6 ,2 ,4]))

def testListDivide():
    """
    Test listDivide
    """
    assert listDivide([1 ,2 ,3 ,4 ,5]) == 2
    assert listDivide([2 ,4 ,6 ,8 ,10]) == 5
    assert listDivide([30, 54, 63 ,98, 100], divide=10) == 2
    assert listDivide([]) == 0
    assert listDivide([1 ,2 ,3 ,4 ,5], 1) == 5
    
if __name__ == "__main__":
    testListDivide()
