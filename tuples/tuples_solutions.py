# (easy questions)
# tuple basic

def swap_pairs(t):
    t = list(t)
    for i in range(0, len(t) - 1,2):
        t[i], t[i + 1] = t[i + 1], t[i]
    return tuple(t)
    
print(swap_pairs((1, 2, 3, 4)))
print(swap_pairs((1, 2, 3)))

# tuple unpacking
def get_status(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    return (minimum, maximum, total, average)
print(get_status([1, 2, 3, 4, 5]))

# (medium questions)
# named tuples
from collections import namedtuple
Student = namedtuple('Students', ['name', 'age', 'grades'])
def top_students(students):
    return max(students, key=lambda s: sum(s.grades) / len(s.grades))
alice = Student("Alice", 20, (85, 90, 95))
bob = Student("Bob", 19, (70, 80, 90))
charlie = Student("Charlie", 21, (90, 92, 93))
print(top_students([alice, bob, charlie]))

# tuple as keys
def count_coordinate_occurances(coords):
    count_dict = {}
    for coord in coords:
        if coord in count_dict:
            count_dict[coord] += 1
        else:
            count_dict[coord] = 1
    return count_dict
coords = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
print(count_coordinate_occurances(coords))