### 20. Valid Parentheses

---

### Step 1: Understand the Problem

- **Input:** A string `s` containing just the characters '(', ')', '{', '}', '[' and ']'.
- **Output:** A boolean value: `True` if the input string is valid, `False` otherwise.
- **Constraints:** An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.

---

### Step 2: Work Through Examples

- **Example 1:**
    - `Input: s = "()"`
    - `Output: True`
- **Example 2:**
    - `Input: s = "()[]{}"`
    - `Output: True`
- **Example 3:**
    - `Input: s = "(]"`
    - `Output: False` (Mismatched types)
- **Example 4:**
    - `Input: s = "([)]"`
    - `Output: False` (Wrong order)
- **Example 5:**
    - `Input: s = "{[]}"`
    - `Output: True` (Correctly nested)

---

### Step 3: Identify the Problem Type

- **Stack Data Structure:** This is the quintessential problem for using a stack. The Last-In, First-Out (LIFO) nature of a stack perfectly models the nested structure of parentheses.
- **String Parsing** and **Validation**.

---

### Step 4: Think About Approaches

- **Approach 1 (Stack and Hash Map - Optimal):** This is the method you've used. Iterate through the string. If you see an opening bracket, push it onto a stack. If you see a closing bracket, pop from the stack and check if it’s the corresponding opening bracket. A hash map is used for instant lookups of bracket pairs.
    - *Time: O(N)*, *Space: O(N)*
- **Approach 2 (String Replacement - Inefficient):** Continuously find and replace valid pairs like "()", "[]", and "{}" with an empty string. If the final string is empty, the original was valid. This is much slower (O(N2)) and less elegant than the stack approach.

---

### Step 5: Plan Before Coding

- **Pseudocode (for your provided stack approach):**
    
    `function isValid(s):
      // Use a list as a stack
      stack = new Stack()
      // Use a map for quick pair lookups
      map = {')': '(', '}': '{', ']': '['}
    
      for each character c in s:
        if c is an opening bracket (a value in the map):
          push c onto the stack
        else if c is a closing bracket (a key in the map):
          if stack is empty OR map[c] does not match pop(stack):
            return False // Found a close bracket with no matching open bracket
    
      // If loop finishes, stack must be empty for the string to be valid
      return true if stack is empty, else false`
    

---

### Step 6: Consider Edge Cases

- **Empty String `""`:** The loop never runs, `not stack` is `True`. Correct.
- **Only Opening Brackets `"(("`:** The loop finishes, but the stack is not empty. `not stack` is `False`. Correct.
- **Only Closing Brackets `"))"`:** The code tries to pop from an empty stack, which your implementation correctly handles, leading to a `False` return. Correct.
- **Odd Length String:** An odd-length string can never be valid. The logic naturally handles this.

---

### Step 7: Complexity Analysis

- **Your Provided Approach (Stack):**
    - **Time Complexity:** O(N), because we iterate through the input string of length N exactly once.
    - **Space Complexity:** O(N) in the worst case. For an input like `"((((("`, the stack would grow to size N.

---

### Step 8: Review and Reflect

- **Why does this work?** A stack's LIFO (Last-In, First-Out) property perfectly mirrors how parentheses must be nested. The most recently opened bracket must be the first one to be closed. The algorithm enforces this rule elegantly. Pushing open brackets and popping to match them with close brackets is a direct simulation of this logic.
- **Can it be improved?** No, this algorithm is optimal. You must look at every character at least once, so O(N) time is the best possible. The space complexity is also unavoidable for inputs with deep nesting.

---

### Important Feedback on Your Provided Code

1. **Excellent Implementation:** This is a high-quality, robust solution. Using a hash map for bracket pairs and handling the empty stack case (`stack.pop() if stack else '#'`) are signs of a strong implementation.
2. **Code Style:**
    - For Python, class names typically use `CamelCase`, so `class Solution:` is the standard convention.
    - The `else: continue` is redundant. A Python `for` loop automatically proceeds to the next item if none of the `if/elif` conditions are met. You can safely remove that `else` block to make the code a little more concise.
3. **Key Takeaway:** You've correctly identified and implemented the two key data structures for this problem: a **Stack** for managing the LIFO order of brackets and a **Hash Map** for efficient O(1) lookups of bracket pairs. This is exactly what an interviewer would want to see.

# The Goal 🎯

The goal is to check if a string containing `()`, `{}`, and `[]` is "valid." This means every opening bracket is eventually closed by the same type of bracket, and the order of opening and closing is correct. The code uses a **stack** data structure, which is perfect for solving problems involving "Last-In, First-Out" logic, like matching nested brackets.

---

### Step-by-Step Explanation

Let's trace your code's logic with an example like `s = "{[]}"`.

### 1. Setup

Python

`stack = []
bracket_map = {')':'(', '}':'{', ']':'['}`

- `stack = []`: You create an empty list that will act as a stack. You'll add opening brackets to it as you find them.
- `bracket_map = {...}`: You create a dictionary that maps each **closing** bracket (the key) to its corresponding **opening** bracket (the value). This is used for quick lookups.

### 2. The Loop

The code iterates through each character of the string. There are three possibilities for each character.

### **Possibility 1: The character is an OPENING bracket**

Python

`if char in bracket_map.values():
    stack.append(char)`

- This line checks if the character is one of the values in your map (`(`, `{`, `[`).
- If it is, it's an opening bracket and gets pushed onto the stack to wait for its partner.
- **Example (`s = "{[]}"`):**
    - First `char` is `{`. It's an opening bracket, so `stack` becomes `['{']`.
    - Next `char` is `[`. It's an opening bracket, so `stack` becomes `['{', '[']`.

### **Possibility 2: The character is a CLOSING bracket**

Python

`elif char in bracket_map:
    top_element = stack.pop() if stack else '#'
    if bracket_map[char] != top_element:
        return False`

- This line checks if the character is one of the keys in your map (`)`, `}`, `]`).
- If it is, two things happen:
    1. `top_element = stack.pop() if stack else '#'`: This is a "safe pop." It tries to pop the most recent opening bracket from the stack. If the stack is empty (meaning a closing bracket appeared with no opener), it assigns a dummy value `'#'` to `top_element` to prevent an error.
    2. `if bracket_map[char] != top_element:`: This is the validation step. It checks if the popped bracket is the correct partner for the current closing bracket. If not, the string is invalid, and it returns `False` immediately.
- **Example (`s = "{[]}"`):**
    - Next `char` is `]`. It's a closing bracket.
    - The code pops from the stack. `top_element` becomes `'['`.
    - It checks: Is `bracket_map[']']` (which is `'['`) different from `top_element` (which is `'['`)? No, they match. The code continues.
    - Next `char` is `}`. It's a closing bracket.
    - The code pops from the stack. `top_element` becomes `'{'`.
    - It checks: Is `bracket_map['}']` (which is `'{'`) different from `top_element` (which is `'{'`)? No, they match.

### **Possibility 3: The character is not a bracket**

Python

`else:
    continue`

- If the character is anything else, this code simply ignores it and moves to the next character.

### 3. The Final Check

Python

`return not stack`

- After the loop finishes, this line determines the final answer.
- If the `stack` is empty, it means every opening bracket found a matching closing partner. `not []` evaluates to **`True`**.
- If the `stack` is not empty (e.g., `s = "(("`), it means there are unclosed opening brackets. `not ['(', '(']` evaluates to **`False`**.
- For our example `s = "{[]}"`, the stack is empty at the end, so the function correctly returns **`True`**.