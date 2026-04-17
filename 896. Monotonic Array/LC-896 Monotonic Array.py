class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True

        is_increasing = True
        is_decreasing = True

        for i in range(n-1):
            if nums[i] < nums[i + 1]:
                is_decreasing = False
            
            if nums[i] > nums[i + 1]:
                is_increasing = False

        return is_increasing or is_decreasing