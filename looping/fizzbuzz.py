# Problem: FizzBuzz

# Complete the function below. For a number N, print all the numbers starting
# from 1 to N, except
# 1. For numbers divisible by 3, print "Fizz"
# 2. For numbers divisible by 5, print "Buzz"
# 3. For numbers divisible by both 3 and 5, print "FizzBuzz"

# Example:
# Input: N = 20
# Output:
# 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14,
# FizzBuzz, 16, 17, Fizz, 19, Buzz

def fizzbuzz(n):
    nums = range(1, n+1)
    for num in nums:
        if num % 15 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)
    return

if __name__ == "__main__":
    fizzbuzz(100)
