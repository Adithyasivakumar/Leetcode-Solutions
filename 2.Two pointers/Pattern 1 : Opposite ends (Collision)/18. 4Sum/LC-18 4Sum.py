class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        
        nums.sort()
        res = []
        # fix 1
        for i in range(len(nums)):

            if i != 0 and nums[i] == nums[i-1]:
                continue

            # fix 2
            for j in range(i+1, len(nums)):

                if j != i + 1 and nums[j] == nums[j-1]:
                    continue

                # two pointers
                l = j + 1
                r = len(nums) - 1

                while l < r:

                    current_sum = nums[i] + nums[j] + nums[l] + nums[r]

                    if current_sum > target:
                        r -= 1
                    elif current_sum < target:
                        l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1

        return res