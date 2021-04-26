# Project Euler
# Problem 1 - Multiples of 3 and 5
# https://projecteuler.net/problem=1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Inititalize variable to contain total sum
sum = 0

# Loop through all numbers between 1 and 999
# Determine whether number is multiple of 3 or 5
# If yes, add to sum, otherwise skip
for number in range(1, 1000):
    if number % 3 == 0 or number % 5 == 0:
        sum += number

# Print result
print(f"The sum is: {sum}.")
