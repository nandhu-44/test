# Tuple operations

my_tuple = (12, 1, 4, 6, 2, 8, 33)
print(f"Original tuple \t\b: {my_tuple}")

# Append to tuple
my_tuple += (5, 10, 15)
print(f"Appended tuple \t\b: {my_tuple}")

# Sorted tuple
sorted_tuple = tuple(sorted(my_tuple))
print(f"Sorted tuple \t\b: {sorted_tuple}")