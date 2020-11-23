def multiply_even_numbers(nums):

    product = 1
    for i in nums:
        if i%2 == 0:
            product *= i
    return product

print(multiply_even_numbers([2, 3, 4, 5, 6]))