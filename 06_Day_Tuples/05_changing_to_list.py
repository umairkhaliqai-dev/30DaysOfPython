# Since tuples are immutable, convert to list, modify, then convert back.
# Original tuple
level = ("low", "medium", "high")
# Convert to list
level_list = list(level)
level_list.append("very high")  # Add new item
# Convert back to tuple
level = tuple(level_list)
print("Updated tuple:", level)  # ('low', 'medium', 'high', 'very high')
