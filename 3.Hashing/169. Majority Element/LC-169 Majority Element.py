#Approach 1

class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        majority = None
        count = 0

        for num in nums:
            
            if count == 0:
                majority = num 

            if num == majority:
                count += 1              

            elif num != majority:
                count -= 1
        
        return majority

#Approach 2

from collections import Counter

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        n = len(nums)
        
        frequency_count = Counter(nums)
        
        for num, count in frequency_count.items():
            
            if count > n / 2:
                return num
        
        return False