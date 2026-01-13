class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        bracket_map = {')':'(','}' : '{', ']' : '['}

        for char in s:

            if char in bracket_map.values():
                stack.append(char)

            elif char in bracket_map:
                top_element = stack.pop() if stack else '#'

                if bracket_map[char] != top_element:
                    return False
            else:
                continue

        return not stack
        