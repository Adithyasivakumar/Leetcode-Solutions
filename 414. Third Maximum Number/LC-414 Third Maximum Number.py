import math
class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        first = -math.inf
        second = -math.inf
        third = -math.inf

        for num in nums:
        
            if num == first or num == second or num == third:
                continue

            if num > first:
                third = second
                second = first
                first = num
                
            elif num > second:
                third = second
                second = num
                
            elif num > third:
                third = num

        if third == -math.inf:
            return first
        else:
            return third