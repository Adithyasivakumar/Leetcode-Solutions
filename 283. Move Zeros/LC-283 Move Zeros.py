class Solution:
    def moveZeros(self, nums: list[int]) -> None:
        
        i = 0
        
        for j in range(len(nums)):
            
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                
        return i 