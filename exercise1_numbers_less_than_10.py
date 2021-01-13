"""The purpose of this file is to """

# Requirements: Given a list as a parameter,write a function that returns a list of numbers that are less than ten
# For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]


def new_function(a_list):
    list_passed = a_list
    return_list = []

    for item in list_passed:
        if item < 10:
            return_list.append(item)
        else:
            pass

    print(return_list)

    # input
selected = [1, 11, 14, 5, 8, 9]
new_function(selected)
