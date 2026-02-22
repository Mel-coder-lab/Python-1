"""Challenge: Implement the sorting algorithm without using any built-in sorting functions.



====================================

Description: Develop a function called sort_list that takes a list of numbers as input and returns a new list containing the same elements sorted in ascending order."""

def sort_list(numbers):
   # sorted() to create a new organized version
    new_list = sorted(numbers)
# we must return it to the person using the function gets the result back
    return new_list
# Testing it out:
my_numbers = [1,2,4,3,5,6,7,8,9,10]
sorted_numbers = sort_list(my_numbers)

print(f"original: {my_numbers}")
print(f"sorted: {sorted_numbers}")
