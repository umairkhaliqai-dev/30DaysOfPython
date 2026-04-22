# A set holds unique, unordered items. Use {} or set().
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)  # Order may vary — sets are unordered!
# emptyt set = set() not {}

print()
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print("\n1. Length of it_companies:", len(it_companies))
it_companies.add('Twitter')
print(it_companies)
print("\n2. After adding 'Twitter':")
print(it_companies)
print("Length:", len(it_companies))
print()
it_companies.remove('IBM')
print("\n4a. After removing 'IBM' using remove():")
print(it_companies)

print()
print("\n" + "=" * 50)
print("5. DIFFERENCE BETWEEN remove() AND discard():")
print("=" * 50)
print("""
remove() - Removes specified element from set
          • Raises KeyError if element not found
          • Use when you're sure element exists
          • Example: fruits.remove('apple')
          
discard() - Removes specified element from set
           • Does NOT raise error if element not found
           • Safer to use when element might not exist
           • Example: fruits.discard('apple')
           
pop() - Removes and returns an ARBITRARY (random) element
       • Raises KeyError if set is empty
       • Useful when you don't care which element is removed
""")

print()
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print("Original Sets:")
print(f"A = {A}")
print(f"B = {B}")
print(f"Length of A: {len(A)}")
print(f"Length of B: {len(B)}")
print("=" * 60)

print()
# Exercise 5: Join A with B and B with A
print("\n5. JOIN A WITH B AND B WITH A:")
# Method 1: Using update() - modifies the original set
A_copy = A.copy()  # Save original for demonstration
B_copy = B.copy()

A_copy.update(B)
print(f"A ∪ B (using update on A): {A_copy}")

B_copy.update(A)
print(f"B ∪ A (using update on B): {B_copy}")

print("Note: update() modifies the set in place, while union() returns a new set")