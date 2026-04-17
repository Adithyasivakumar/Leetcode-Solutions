class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        longest = []

        maximum_from_right = -1
        longest.append(maximum_from_right)

        n = len(arr)

        for i in range(n-1, -1, -1):
            if arr[i] >= maximum_from_right:
                longest.append(arr[i])
                maximum_from_right = arr[i]
            
            elif arr[i] <= maximum_from_right:
                longest.append(maximum_from_right)

        longest.reverse()

        return longest[1:]