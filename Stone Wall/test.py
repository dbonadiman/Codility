from solution import solution

def test_solution():
    input1 =[8,8,5,7,9,8,7,4,8]
    print("test1: {} => {}".format(input1, []))
    assert solution(input1) == 7

def test_solution2():
    input1 =[8,8,8,8,8]
    print("test1: {} => {}".format(input1, []))
    assert solution(input1) == 1
