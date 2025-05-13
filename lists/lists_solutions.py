# (easy questions)
# list operations
def filter_even_numbers(lst):
    return list(filter(lambda x: not x & 1,lst))
print(filter_even_numbers([1, 2, 3, 4, 5, 6]))
print(filter_even_numbers([1, 3, 5]))

# list manipulation
import heapq
def merge_sorted_lists(lst1, lst2):
    return list(heapq.merge(lst1, lst2))
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))
print(merge_sorted_lists([1, 2, 3], [4, 5, 6]))

# (medium questions)

# list comprehensions
def generate_matrix(n, m):
    return list(map(lambda i: list(map(lambda j: i * j, range(m))), range(n)))
print(generate_matrix(3,3))

# nested lists
def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(transpose_matrix(matrix))