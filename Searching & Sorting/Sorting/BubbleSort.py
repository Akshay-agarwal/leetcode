def BubbleSort(nums):
    n = len(nums) - 1
    for i in range(n):
        for j in range(n - i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    print(nums)

BubbleSort([])
