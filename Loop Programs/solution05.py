# Find the first non-repeated character

"""
Given a string, find the first non-repeated character.
"""

input_str = input("Enter a string: ").strip().lower()

"""
Solution - 1
str.count() -> traverses the entire string each time it is called.
O(n) operation inside a loop that also runs O(n) time. => O(n^2) 
"""
# for char in input_str:
#     if input_str.count(char) == 1:
#         print(f"First non-repeated character is: {char}")
#         break

"""
Solution - 2
The first loop counts the occurrences of each character (O(n))
The second loop find the first non-repeated character (O(n))
O(n) + O(n) = O(n)
"""
char_count = {}

# counts the occurences of each charcater
for char in input_str:
    char_count[char] = char_count.get(char, 0) + 1

# Find the first occurenace that occurs only once
for char in input_str:
    if char_count[char] == 1:
        print(f"First non-repeated character is: {char}")
        break