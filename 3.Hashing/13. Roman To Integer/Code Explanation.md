### 13. Roman to Integer

---

### Step 1: Understand the Problem

- **Input:** A string `s` representing a Roman numeral.
- **Output:** The integer equivalent of the input string.
- **Constraints:** The input is guaranteed to be a valid Roman numeral in the range from 1 to 3999. The core challenge lies in handling the six instances where subtraction is used:
    - `I` can be placed before `V` (5) and `X` (10) to make 4 and 9.
    - `X` can be placed before `L` (50) and `C` (100) to make 40 and 90.
    - `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

---

### Step 2: Work Through Examples

- **Example 1:**
    - `Input: s = "III"`
    - `Output: 3` (Simple addition: 1 + 1 + 1)
- **Example 2:**
    - `Input: s = "LVIII"`
    - `Output: 58` (L=50, V=5, III=3)
- **Example 3:**
    - `Input: s = "IV"`
    - `Output: 4` (Subtractive case: -1 + 5)
- **Example 4:**
    - `Input: s = "MCMXCIV"`
    - `Output: 1994` (M=1000, CM=900, XC=90, IV=4)

---

### Step 3: Identify the Problem Type

- **String Manipulation**
- **Hash Map** (or Dictionary) for mapping symbols to values.
- **String Parsing** with specific character-by-character rules.

---

### Step 4: Think About Approaches

- **Approach 1 (Left-to-Right Pass with Lookahead):** This is the excellent method you've implemented. Iterate through the string from left to right. At each character, check the *next* character. If the next character represents a larger value, you know the current character is part of a subtractive pair (like the 'I' in 'IV'), so you subtract its value. Otherwise, you add its value.
- **Approach 2 (Right-to-Left Pass):** An alternative is to iterate from right to left. This can be slightly simpler as you don't need to "look ahead." You process a character and add its value. If the current character's value is less than the value of the character to its right (which you've already processed), you subtract it twice (effectively turning its previous addition into a subtraction). A simpler version of this is to just subtract if the current value is less than the previous, and add otherwise.

---

### Step 5: Plan Before Coding

- **Pseudocode (for your provided left-to-right approach):**
    
    `function romanToInt(s):
      map = {'I': 1, 'V': 5, 'X': 10, ...}
      total = 0
      length = length of s
    
      for i from 0 to length-1:
        current_value = map[s[i]]
    
        // Check if we are not at the last character AND
        // if the next character's value is greater than the current one
        if i < length-1 and current_value < map[s[i+1]]:
          // This is a subtractive case
          total = total - current_value
        else:
          // This is an additive case
          total = total + current_value
    
      return total`
    

---

### Step 6: Consider Edge Cases

- **Single character numeral:** `"M"`. The loop runs, the lookahead condition `i + 1 < n` is always false, so it correctly adds 1000.
- **Purely additive numeral:** `"LVII"`. The lookahead condition is always false, resulting in simple addition.
- **Purely subtractive numeral:** `"IX"`. On 'I', the condition `1 < 10` is true, so `total` becomes -1. On 'X', the else block runs, `total` becomes -1 + 10 = 9. Correct.
- **Complex mixed numeral:** `"MCMXCIV"`. The logic correctly handles each pair (`100 + 1000`, `10 + 100`, `1 + 5`).

---

### Step 7: Complexity Analysis

- **Your Provided Approach:**
    - **Time Complexity:** O(N), where N is the number of characters in the string `s`. We iterate through the string exactly once. (Since the problem constrains N to be at most 15, you could also argue the complexity is technically O(1), but O(N) is the more general and standard answer).
    - **Space Complexity:** O(1). The hash map stores a fixed number of symbols (7), so its size is constant and does not depend on the length of the input string.

---

### Step 8: Review and Reflect

- **Why does this work?** The algorithm correctly identifies that Roman numerals are largely additive, with the single exception of the subtractive principle. The `if` condition precisely targets this exception by looking one character ahead. By subtracting the smaller value when it precedes a larger one, it perfectly resolves pairs like `IV` (`1 + 5 = 4`) and `CM` (`100 + 1000 = 900`).
- **Can it be improved?** No, this solution is optimal. It achieves linear time and constant space, which is the best possible for this problem. The logic is clean and directly solves the problem as defined.