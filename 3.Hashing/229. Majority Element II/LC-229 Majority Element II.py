from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n = len(nums)

        frequency_count = Counter(nums)

        result = []

        for num, count in frequency_count.items():

            if count > n // 3:
                result.append(num)
                            
        return result