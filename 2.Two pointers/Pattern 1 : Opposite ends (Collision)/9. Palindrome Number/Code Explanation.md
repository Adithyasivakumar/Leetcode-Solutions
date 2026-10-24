### 9. Palindrome Number

---

### Step 1: Understand the Problem

- **Input:** An integer `x`.
- **Output:** A boolean, `True` if `x` is a palindrome, and `False` otherwise.
- **Constraints:** A number is a palindrome if it reads the same forwards and backward. For example, 121 is a palindrome, while 123 is not. Negative numbers are not considered palindromes.

---

### Step 2: Work Through Examples

- **Example 1:**
    - `Input: x = 121`
    - `Output: True`
- **Example 2:**
    - `Input: x = -121`
    - `Output: False` (Reads as -121 from left to right, and 121- from right to left).
- **Example 3:**
    - `Input: x = 10`
    - `Output: False` (Reads as 10 from left to right, and 01 from right to left).

---

### Step 3: Identify the Problem Type

- **Integer Manipulation**
- **String Manipulation**
- **Two-Pointer Technique** (for the string-based approach)

---

### Step 4: Think About Approaches

- **Approach 1 (Convert to String - Your Approach):** Convert the integer to a string. Then, compare the string to its reverse. This is the most intuitive approach. You can do this comparison with two pointers (one at the start, one at the end, moving inwards) or by using built-in string slicing like `s == s[::-1]`.
    - *Time: O(d)*, *Space: O(d)* (where d is the number of digits).
- **Approach 2 (Revert Half the Number - Optimal):** This is the more advanced approach that solves the problem's "follow-up" challenge of not converting the number to a string. You can mathematically build a new number that is the reverse of the original, but you only need to reverse the *second half*. Then you compare the first half of the original number with the reverted second half.
    - *Time: O(d)*, *Space: O(1)*.

---

### Step 5: Plan Before Coding

- **Pseudocode (for the Optimal "Revert Half" Approach):**
    
    `function isPalindrome(x):
      // A guard clause for edge cases like negative numbers
      // or numbers ending in 0 (like 10, 120).
      if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
      reverted_half = 0
      while x > reverted_half:
        // Build the reverted number
        reverted_half = reverted_half * 10 + x % 10
        // Remove the last digit from x
        x = x // 10
    
      // Compare the two halves.
      // The second condition handles numbers with an odd number of digits.
      return x == reverted_half or x == reverted_half // 10`
    

---

### Step 6: Consider Edge Cases

- **Negative Numbers:** Must return `False`.
- **Numbers ending in 0 (but not 0 itself):** For a number like 120 to be a palindrome, it would have to start with 0, which isn't possible for positive integers. Must return `False`.
- **Single-Digit Numbers:** `0` to `9` are all palindromes. The logic should handle this.

---

### Step 7: Complexity Analysis

- **Your Approach (String Conversion):**
    - **Time Complexity:** O(d), where d is the number of digits in the integer. This is because converting the number to a string and then iterating over it takes time proportional to its length.
    - **Space Complexity:** O(d), as a new string of length d must be created to hold the number's characters.
- **Optimal Approach (Revert Half):**
    - **Time Complexity:** O(d). The `while` loop runs approximately d/2 times.
    - **Space Complexity:** O(1). This is the key advantage. It only uses a fixed number of variables for storage, regardless of the input size.

---

### Step 8: Review and Reflect

- **Why does this work?** The string method is straightforward. The mathematical "revert half" method is clever because it avoids potential integer overflow by only reversing half the number. It correctly compares the first half of the number with the reversed second half to determine if it's a palindrome.
- **Which is better for an interview?** Starting with the string conversion approach is fine because it's simple and shows you can solve the problem. However, an ideal candidate would then discuss the "follow-up" challenge and explain or code the more optimal, constant-space mathematical solution.