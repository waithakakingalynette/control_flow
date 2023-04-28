#Write a function that uses while, if and continue statements to print all the even numbers between 0 and 50. 
def print_even_numbers():
    num = 0
    while num < 50:
        if num % 2 == 0:
            print(num)
        num += 1
        continue

#Write a function that takes an integer argument and prints "Prime" if the number is prime, and "Not prime" if the number is not prime.
def is_prime(num):
    if num <= 1:
        print("Not prime")
        return
    for i in range(2, int(num/2) + 1):
        if (num % i) == 0:
            print("Not prime")
            break
    else:
        print("Prime")

#Write a function that takes a list of integers as input and prints the sum of all the even numbers in the list.
def sum_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    print("Sum of even numbers:", total)

#Write a function that takes any two integers as input, and prints the sum of all the numbers between the two integers (inclusive) that are divisible by 3.
def sum_divisible_by_three(start, end):
    total = 0
    for num in range(start, end + 1):
        if num % 3 == 0:
            total += num
    print("Sum of numbers divisible by 3:", total)