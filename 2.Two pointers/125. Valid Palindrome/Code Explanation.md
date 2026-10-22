# **Problem Explanation**

# **125. Valid Palindrome**

## **Step 1: Understand the Problem**

- **Input:** A string `s`.
- **Output:** A boolean (`True` or `False`).
- **Goal:** Determine if the string is a palindrome after performing two transformations:
    1. Convert all uppercase letters to lowercase.
    2. Remove all non-alphanumeric characters (anything that isn't a letter or a number).

---

## **Step 2: Work Through Examples**

- **Example 1: `s = "A man, a plan, a canal: Panama"`**
    - After converting to lowercase and removing non-alphanumeric characters, the string becomes `"amanaplanacanalpanama"`.
    - This string reads the same forwards and backward.
    - **Output:** `True`.
- **Example 2: `s = "race a car"`**
    - After sanitizing, the string becomes `"raceacar"`.
    - Forwards: `"raceacar"`. Backwards: `"racaecar"`. They are not the same.
    - **Output:** `False`.
- **Example 3: `s = " "`**
    - After removing non-alphanumeric characters, the string becomes empty (`""`).
    - An empty string reads the same forwards and backward.
    - **Output:** `True`.

---

## **Step 3: Identify the Problem Type**

- String Manipulation
- **Two-Pointer Technique**
- In-place validation

---

## **Step 4: Think About Approaches**

- **Simple Approach (O(n) space):** Create a new, sanitized string by iterating through the input `s`, keeping only alphanumeric characters, and converting them to lowercase. Then, check if this new string is equal to its reverse (`new_s == new_s[::-1]`). This is easy to write but uses extra memory.
- **Optimal Approach (Two Pointers, O(1) space):** The implemented solution. Use two pointers, one at the start and one at the end of the original string. Move the pointers inward, skipping any non-alphanumeric characters. When both pointers are on valid characters, compare them (case-insensitively). This avoids creating a new string.

---

## **Step 5: Plan Before Coding**

- **Pseudocode (for the Two-Pointer solution):**
    
    `function isPalindrome(s):
      // 1. Set up two pointers at the ends of the string.
      left = 0
      right = length of s - 1
    
      // 2. Loop until the pointers meet or cross.
      while left < right:
        // 3. From the left, find the next valid character.
        while left < right and s[left] is not alphanumeric:
          increment left
    
        // 4. From the right, find the next valid character.
        while left < right and s[right] is not alphanumeric:
          decrement right
    
        // 5. Compare the two valid characters found (case-insensitive).
        if lowercase(s[left]) is not equal to lowercase(s[right]):
          return False
    
        // 6. Move pointers inward for the next comparison.
        increment left
        decrement right
    
      // 7. If the loop completes, it's a palindrome.
      return True`
    

---

## **Step 6: Consider Edge Cases**

- **Empty string `""` or string with only non-alphanumeric characters `".,?"`:** The pointers will meet or cross without the main comparison ever failing. The loop will terminate, and it will correctly return `True`.
- **Single valid character string `"a"` or `"a.,"`:** The loop `while l < r` will not run. It correctly returns `True`.

---

## **Step 7: Complexity Analysis**

- **Time Complexity: O(n)**, where `n` is the length of the string `s`. In the worst case, each pointer will traverse the entire string once.
- **Space Complexity: O(1)**. The algorithm only uses a few variables for the pointers. No new string is created, so the memory usage is constant.

---

## **Step 8: Review and Reflect**

- **Why does this work?** The two-pointer technique is perfectly suited for checking symmetry. The key to this specific problem is the "skipping" logic. By nesting `while` loops to advance the pointers past invalid characters, the algorithm correctly compares only the characters that matter, all while working on the original string to save memory.
- **Can it be improved?** No, this is the optimal O(1) space solution for this problem.

---

## **Code Explanation**

### The Analogy: Checking a Sentence on Paper

Think of checking if a sentence is a palindrome like checking a sentence written on paper. You'll use your left and right index fingers to scan the sentence.

**Example:** The sentence is "A man, a plan, a canal: Panama"

- **`l` (left pointer)**: Your left index finger.
- **`r` (right pointer)**: Your right index finger.

---

### **Step 1: The Setup**

**Code:**

Python

`l , r = 0, len(s)-1`

- **What it does:** It sets up your two "fingers". The left finger `l` starts at the very beginning of the sentence, and the right finger `r` starts at the very end.

---

### **Step 2: The Loop**

**Code:**

Python

`while l <= r:`

- **What it does:** This starts a loop that will keep running as long as your left finger hasn't crossed your right finger.

---

### **Step 3: The "Skip" Logic**

This is where you find the next valid letter to compare.

**Code:**

Python

    `while l < r and not s[l].isalnum():
        l += 1
    while l < r and not s[r].isalnum():
        r -= 1`

- **Analogy:**
    - You look at the character under your left finger. Is it a space, a comma, or a colon? If so, it's not a letter, so you just slide your finger to the right (`l += 1`) until you land on a real letter or number.
    - You do the same with your right finger, sliding it to the left (`r -= 1`) until you find a real letter or number.

---

### **Step 4: The Comparison**

**Code:**

Python

    `if s[l].lower() != s[r].lower():
        return False`

- **What it does:** Now that both fingers are on valid alphanumeric characters, you compare them.
- **Analogy:** You look at the letter under your left finger (e.g., 'A') and the letter under your right finger (e.g., 'a'). `s[l].lower()` makes sure you ignore whether they are big or small. If the letters don't match, you know it's not a palindrome, and you can stop immediately by returning `False`.

---

### **Step 5: Move Inward**

**Code:**

Python

    `l += 1
    r -= 1`

- **What it does:** If the letters matched, the sentence might still be a palindrome.
- **Analogy:** You move both fingers one step closer to the middle to check the next pair of letters. The loop then repeats from Step 2.

---

### **Step 6: The Final Result**

**Code:**

Python

`return True`

- **What it does:** This line is outside the loop. If the `while` loop finishes completely, it means your fingers met in the middle and you **never** found a single mismatch.
- **Analogy:** If you check every pair of letters and they all match, you can confidently declare "It's a palindrome!" by returning `True`.

---

## **Analysis Summary (Deep Revision Framework)**

- **The Core Idea:**
The one-sentence summary is: "The code uses two pointers moving inward to check for symmetry in-place, while cleverly skipping over any non-alphanumeric characters to compare only the relevant parts of the string."
- **Data Structure Choice:**
The algorithm operates directly on the input **string**. The key is that it uses no auxiliary data structures that scale with the input size. This is what allows it to achieve **O(1) space complexity**. The built-in functions `.isalnum()` and `.lower()` are essential tools for the logic.
- **Algorithm Pattern:**
This is a classic **Two-Pointer Technique**. It is the standard pattern for problems that involve checking for symmetry from opposite ends of a sequence. The "skipping" logic is a common variation of this pattern.
- **Complexity:**
    - **Time Complexity: O(n)**. Each pointer traverses the string at most once.
    - **Space Complexity: O(1)**.
- **Articulate the Solution:**
    1. "My solution uses the two-pointer technique to solve this problem in O(n) time and with O(1) constant space."
    2. "I initialize a `left` pointer at the start of the string and a `right` pointer at the end."
    3. "In a `while` loop that runs as long as `left` is less than `right`, I first advance my `left` pointer until it's on an alphanumeric character."
    4. "I do the same for my `right` pointer, moving it backward until it's on an alphanumeric character."
    5. "Once both pointers are on valid characters, I compare them, ignoring case. If they don't match, I immediately return `False`."
    6. "If they do match, I move both pointers one step closer to the center and repeat the process."
    7. "If the loop completes without finding any mismatches, it means the string is a valid palindrome, and I return `True`."
- **Spaced Repetition & Follow-ups:**
This is a fundamental pattern. Great follow-ups include:
    - **LeetCode 9. Palindrome Number**: The simpler version of this problem without character filtering.
    - **LeetCode 680. Valid Palindrome II**: A harder version where you are allowed to delete *at most one* character to make the string a palindrome. This requires a clever modification of this same two-pointer approach.
    - **LeetCode 5. Longest Palindromic Substring**: A much harder problem that involves finding the longest palindromic *substring* within a larger string.

---