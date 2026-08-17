class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []

        for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        
        final_array = even + odd
        return final_array