def find_the_duplicate(nums):
    setOfElems = set()
    for elem in nums:
        if elem in setOfElems:
            return elem
        else:
            setOfElems.add(elem)         
    return True


print(find_the_duplicate([2, 1, 3, 4]))