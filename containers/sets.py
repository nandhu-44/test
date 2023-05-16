# Set operations

my_list = [12, 1, 4, 6, 2, 8, 33, 1, 6, 1, 4, 8, 9, 1, 4, 5, 1]
my_set = set(my_list)

print(f"Original list \t\b\b: {my_list}")
print(f"Set from list \t\b\b: {my_set}")

# Add to set
my_set.update([5, 10, 15])
print(f"Updated set \t\b\b: {my_set}")

my_set_2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Difference of sets
print(f"Difference \t\b\b: {my_set.difference(my_set_2)}")