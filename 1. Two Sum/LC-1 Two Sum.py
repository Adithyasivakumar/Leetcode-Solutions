class Solution (object):
    def twoSum(self, nums, target):
        seen_map = {}
        for i in range (len(nums)):
            complement = target - nums[i]
            if complement in seen_map:
                return [seen_map[complement], i]
            seen_map[nums[i]] = i
        return []