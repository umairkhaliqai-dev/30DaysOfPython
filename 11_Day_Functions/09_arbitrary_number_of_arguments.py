# *args lets a function accept any number of positional arguments as a tuple.
def total(*nums):
    return sum(nums)

print(total(1, 2, 3))       # → 6
print(total(10, 20, 30, 40)) # → 100