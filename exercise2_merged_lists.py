"""The purpose of the file is to """

# Requirements: Write a function that takes in two lists and returns the two lists merged together and sorted
# Hint: You can use the .sort() method


def merge_equal_items_in_two_lists(list_1, list_2):
    pass


# inputs
list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [3, 4, 5, 6, 7, 8, 10]


# permanently sort each list and create a new list for each to hold the new ordered list
# list 1 permanently sorted
list_1.sort(reverse=False)
print(list_1)

# list 2 permanently sorted
list_2.sort(reverse=False)
print(list_2)

# empty container
combined_list = []

for item1 in list_1:
    combined_list.append(item1)
    for item2 in list_2:
        combined_list.append(item2)

print(combined_list)


"""
cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True)

print(cars)
"""
