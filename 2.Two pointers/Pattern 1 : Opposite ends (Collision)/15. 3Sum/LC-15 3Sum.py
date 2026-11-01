class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        res = []
        nums.sort()

        # fix
        for i in range(len(nums)):

            if i != 0 and nums[i] == nums[i-1]:
                continue
            # optimization condition : If the anchor is > 0 then we cannot get a zero sum.
            if nums[i] > 0:
                break
            # two pointers
            l = i + 1
            r = len(nums) - 1

            while l < r:

                total = nums[i] + nums[l] + nums[r]

                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

        return res