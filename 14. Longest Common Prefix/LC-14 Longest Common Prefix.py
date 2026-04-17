class solution:
    def Longest_common_prefix(self, strs: list[str]) -> str:
    
        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            char_to_check = strs[0][i]
            
            for j in range(1, len(strs)):
            
                if i >= len(strs[j]) or strs[j][i] != char_to_check:
                    return strs[0][:i]
                    
        return strs[0]