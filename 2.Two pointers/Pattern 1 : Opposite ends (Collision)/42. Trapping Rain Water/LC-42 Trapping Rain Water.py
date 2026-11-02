# Pre-computation / Dynamic Programming (Prefix and Suffix Arrays) pattern

# Time complexity : O(n)
# Space complexity : O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        
        max_left = []
        max_right = []

        current_max_left = 0

        current_max_right = 0

        for i in range(len(height)):

            if height[i] > current_max_left:
                current_max_left = height[i]

            max_left.append(current_max_left)

        for i in range(len(height)-1, -1, -1):

            if height[i] > current_max_right:
                current_max_right = height[i]

            max_right.append(current_max_right)

        water_trapped = 0
        max_right.reverse()

        for i in range(len(height)):

            cur_min = min(max_left[i], max_right[i])

            result = cur_min - height[i]

            if result > 0:
                water_trapped += result

        return water_trapped


# Two pointers : Most Optimal Solution

# Time complexity : O(n)
# Space Complexity : O(1)

class Solution:
    def trap(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1

        max_left, max_right = height[left], height[right]

        water_trapped = 0

        while left < right:

            if max_left < max_right:

                water_trapped += max_left - height[left]
                left += 1
                max_left = max(max_left, height[left])

            else:

                water_trapped += max_right - height[right]
                right -= 1
                max_right = max(max_right, height[right])

        return water_trapped