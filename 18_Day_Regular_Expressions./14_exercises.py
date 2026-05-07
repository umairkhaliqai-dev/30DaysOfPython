def level1_exercises():
    print("\n=== Level 1 Exercises ===")
    import re 

    
    # Exercise 1: Find all words starting with 'c' in a sentence
    print("\n1. Words starting with 'c':")
    sentence1 = "The cat and cow chased a chicken around the castle"
    c_words = re.findall(r'\bc\w+', sentence1, re.IGNORECASE)
    print(f"   Sentence: {sentence1}")
    print(f"   Result: {c_words}")  # Output: ['cat', 'cow', 'chased', 'chicken', 'castle']
    
    # Exercise 2: Find all 4-letter words
    print("\n2. All 4-letter words:")
    sentence2 = "The quick brown fox jumps over the lazy dog near the tree"
    four_letter_words = re.findall(r'\b\w{4}\b', sentence2)
    print(f"   Sentence: {sentence2}")
    print(f"   Result: {four_letter_words}")  # Output: ['over', 'lazy', 'near', 'tree']
    
    # Exercise 3: Find all digits in a string
    print("\n3. All digits in a string:")
    text_with_digits = "My phone number is 123-456-7890 and I am 25 years old"
    all_digits = re.findall(r'\d', text_with_digits)
    print(f"   Text: {text_with_digits}")
    print(f"   Result: {all_digits}")  # Output: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '2', '5']
    
    # Bonus: Find all numbers (not just single digits)
    print("\n   Bonus - All numbers (multi-digit):")
    all_numbers = re.findall(r'\d+', text_with_digits)
    print(f"   Result: {all_numbers}")  # Output: ['123', '456', '7890', '25']