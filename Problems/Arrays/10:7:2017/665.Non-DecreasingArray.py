class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                count += 1
                if i == 0:
                    nums[i] = nums[i+1]
                elif nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i-1]
                else:
                    nums[i+1] = nums[i]
            if count == 2:
                return False
        return True