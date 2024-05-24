# Sum of even numbers

"""
Calculate the sum of even numbers up to a given number n.
"""

while True:
    try:
        number = int(input("Give a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter an interger value.")

sum_even = 0

for n in range(1, number+1):
    # Check if number is even
    if n % 2 == 0:
        sum_even += n

print(sum_even)