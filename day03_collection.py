numbers = list(range(11, -1, -1))

#print(numbers)


def function1():
    numbers = [10, 3, 4, 5, 6, 2, 3, 5]
    print(numbers)

    # reverse the order of the list members
    numbers.reverse()

    print(numbers)


#function1()

def function5():
    numbers = [1, 2, 3, 4, 5]
    print(numbers)

    # add 10 at index 1
    numbers.insert(1, 10)

    print(numbers)

    # add 10 at index 1
    numbers.insert(10, 20)
    numbers.insert(40, 80)

    print(numbers)

function5()