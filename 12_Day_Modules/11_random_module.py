# The random module generates pseudo-random numbers and makes random selections — great for games, sampling, and testing.
import random

print(random.random())             # float between 0.0–1.0
print(random.randint(1, 10))       # random int 1–10
print(random.choice(['a','b','c'])) # random item

nums = [1,2,3,4,5]
random.shuffle(nums)
print(nums)                        # shuffled list