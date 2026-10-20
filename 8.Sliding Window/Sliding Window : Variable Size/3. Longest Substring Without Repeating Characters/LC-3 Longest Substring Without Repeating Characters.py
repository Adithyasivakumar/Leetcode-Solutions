# Optimal solution using set()

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()

        max_len = 0

        l = 0

        for r in range(len(s)):

            incoming = s[r]

            while incoming in seen:
                seen.remove(s[l])
                l += 1

            seen.add(incoming)

            cur_len = r-l+1

            if cur_len > max_len:
                max_len = cur_len

        return max_len