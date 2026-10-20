from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        target = Counter(t)

        freq = {}

        min_len = float('inf')

        res_str = ""

        have, need = 0, len(target)

        l = 0

        for r in range(len(s)):

            incoming = s[r]

            if incoming in target:
                freq[incoming] = freq.get(incoming, 0) + 1
                
                if freq[incoming] == target[incoming]:
                    have += 1

            while have == need:

                current_len = r-l+1

                if current_len < min_len:
                    min_len = current_len
                    res_str = s[l:r+1]

                outgoing = s[l]

                if outgoing in target:

                    freq[outgoing] -= 1

                    if freq[outgoing] < target[outgoing]:
                        have -= 1

                    if freq[outgoing] == 0:
                        del freq[outgoing]

                l += 1

        return res_str