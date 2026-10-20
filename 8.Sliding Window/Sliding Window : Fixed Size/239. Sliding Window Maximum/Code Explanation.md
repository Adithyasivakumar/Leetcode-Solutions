class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if sum(nums) < target:
            return 0
        
        l = 0

        current_window = 0

        min_size = float('inf')

        for r in range(len(nums)):

            current_window += nums[r]

            while current_window >= target:
                min_size = min(min_size, r-l+1)
                current_window -= nums[l]
                l += 1

        return min_size