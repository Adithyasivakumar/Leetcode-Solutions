from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        frequency_count = Counter(nums)

        for num, count in frequency_count.items():

            if count > 1:
                return True
        
        return False