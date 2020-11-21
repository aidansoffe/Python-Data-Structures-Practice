def sum_floats(nums):
    return sum([num for num in nums if isinstance(num, float)])

print(sum_floats([1.5, 2.4, 'awesome', [], 1]))