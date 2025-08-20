#Main logic
class solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

nums = [1, 2, 3, 4]
val = int(input("Enter the value:"))
sol = solution()
k = sol.removeElement(nums, val)
print("The values after removing element are: ", nums[:k])
print("Numbers of elements left:", k)
