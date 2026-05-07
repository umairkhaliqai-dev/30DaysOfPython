# Definition: Basic tasks – read a txt file, write to txt file, append.


# Example: read lines & count words
with open("sample.txt", "r") as f:
    words = f.read().split()
    print(len(words))

print()
