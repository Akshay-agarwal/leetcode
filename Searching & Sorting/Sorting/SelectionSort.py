def SelectionSort(nums):
    n = len(nums)
    min = 0
    for i in range(n):
        for j in range(i, n):
            if nums[j] < nums[min]:
                min = j
        nums[i],nums[min] = nums[min], nums[i]
    print(nums)

SelectionSort([21,2,43,52,6,65,76])