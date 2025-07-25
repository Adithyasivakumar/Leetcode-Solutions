#Two Sum
#main logic
class solution (object):
    def twoSum(self, nums, target):
        map = {}
        for i in range (len(nums)):
            complement = target - nums[i]
            if complement in map:
                return [map[complement], i]
            map[nums[i]] = i
        return []
#input logic
nums = list(map(int, input("Enter the values (Space - separated): ").split()))
target = int(input("Enter the target value: "))
#output logic
sol = solution()
index_pos = sol.twoSum(nums, target)
print("The solution is:", index_pos)  
        