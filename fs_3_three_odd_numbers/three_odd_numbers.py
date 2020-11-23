def three_odd_numbers(nums):
    for i in range(len(nums)-2):
        if (nums[i] + nums[i + 1] + nums[i + 2]) % 2 != 0:
            return True

    return False

print(three_odd_numbers([1, 2, 3, 3, 2]))