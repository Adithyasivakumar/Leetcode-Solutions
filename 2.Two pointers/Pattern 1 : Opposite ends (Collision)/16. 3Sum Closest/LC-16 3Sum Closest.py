class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        
        closest = float('inf')
        nums.sort()
        # fix
        for i in range(len(nums)):

            if i != 0 and nums[i] == nums[i-1]:
                continue
            # two pointers
            l = i + 1
            r = len(nums) - 1

            while l < r:

                current_sum = nums[i] + nums[l] + nums[r]
                # check
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum
                # pointer movement following two pointers
                if current_sum == target:
                    return current_sum
                elif current_sum > target:
                    r -= 1
                else:
                    l += 1

        return closest