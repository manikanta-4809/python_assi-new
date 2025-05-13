# (easy questions)
# Function basic 
def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0
print(calculate_average([7, 14, 21]))
print(calculate_average([]))

# Default Parameters
def great_user(name, greeting ="Hello"):
    return f"{greeting}, {name} !"
print(great_user("Charlie"))
print(great_user("Dana", "Welcome"))

# (Medium questions)
# Variable Arguments
def calculate_total(*prices, discount=0):
    total = sum(prices)
    return total * (1 - discount / 100)
print(calculate_total(5, 15, 25))
print(calculate_total(5, 15, 25, 5, discount=20))

# Clousers
def create_multipliers(n):
    def multiplier(x):
        return x * n
    return multiplier
quadraple = create_multipliers(4)
half = create_multipliers(0.5)
print(quadraple(6))
print(half(20))
