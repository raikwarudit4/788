# slicing
# - retrive only part of collection
# - syntax
#   <collection>[<lower>:<upper>:<stride>]
#   - the slicing will never include the upper bound


def function1():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # for index in range(4):
    #     print(numbers[index])

    print(numbers[0:4])
    print(numbers[4:9])
    print(numbers[-5:-1])
    print(numbers[-5:])
    print(numbers[0:])
    print(numbers[1:])
    print(numbers[1::2])
    print(numbers[::2])
    print(numbers[::])
    print(numbers[:5:])
    print(numbers[1::2])
    print(numbers[0::-1])




function1()


def function2():
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # get all the values
    print(numbers[0:10])

    # get all the values from even positions
    print(numbers[0:10:2])

    # get all the values from odd positions
    print(numbers[1:10:2])


    # index_values = list(range(1, len(numbers), 2))
    # print(index_values)
    #
    # for index in index_values:
    #     print(numbers[index])

#function2()