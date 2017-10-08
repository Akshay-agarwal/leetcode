def  LinearSearch(nums, target):
    for num in nums:
        if num == target:
            return True
    return False

l = [1,2,423,34,5,34,256,76,24]
print(LinearSearch(l, 50))