import math

"""
Name: Linus Agwu
Date: 2023-04-03
Purpose: Implementation of "detecting primes" algorithm in 
to test if user input integer is prime or composite, calculate the probability of it being prime, 
and output the number of steps taken by the algorithm for primality testing.
Time complexity of the algorithm: O(sqrt(number)).
The maximum size integer that can be evaluated with this algorithm 
depends on the computational resources available.
    """
def prime_Num(N_number):
    
    if N_number <= 1:
        return False
    elif N_number <= 3:
        return True
    elif N_number % 2 == 0 or N_number % 3 == 0:
        return False
    
    # Check if N_number is divisible by any prime number <= sqrt(N_number)
    for i in range(5, int(math.sqrt(N_number)) + 1, 6):
        if N_number % i == 0 or N_number % (i + 2) == 0:
            return False
    
    # N_number is prime if it is not divisible by any prime number <= sqrt(N_number)
    return True


# Get user input for an integer value to test for primality
N_number = int(input("Enter an integer value: "))

# Call the prime_Num function to determine if the value is prime or not
if prime_Num(N_number):
    print("Yes, this is a prime Number")
else:
    print("No, this is a composite Number")

# Calculate the probability that the value is prime using the Prime Number Theorem
prob = 1 / math.log(N_number)
print("Probability that it is prime:", prob)

# Count the N_number of steps (time complexity) taken by the prime_Num function to determine primality
steps = int(math.sqrt(N_number)) // 6 + 1
print("Number of steps:", steps)

