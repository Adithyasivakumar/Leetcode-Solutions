# **Problem Explanation**

## **242. Valid Anagram**

### **Step 1: Understand the Problem**

- **Input:** Two strings `s` and `t`.
- **Output:** `True` if `t` is an anagram of `s`, otherwise `False`.
- **Definition:** An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
- **Goal:** Determine if both strings contain the exact same characters with the exact same frequencies.

### **Step 2: Work Through Examples**

- **Example 1:** `s = "anagram"`, `t = "nagaram"`
    - `s` counts: `a:3, n:1, g:1, r:1, m:1`
    - `t` counts: `n:1, a:3, g:1, r:1, m:1`
    - Match? Yes.
    - **Output:** `True`.
- **Example 2:** `s = "rat"`, `t = "car"`
    - `s` has 't', `t` does not.
    - **Output:** `False`.
- **Example 3:** `s = "a"`, `t = "ab"`
    - Different lengths. Impossible.
    - **Output:** `False`.

### **Step 3: Identify the Problem Type**

- **String Manipulation:** Checking character composition.
- **Sorting / Hashing:** Comparing collections of elements.

### **Step 4: Think About Approaches**

- **Approach 1: Sorting (Your Solution):**
    - Sort string `s` alphabetically.
    - Sort string `t` alphabetically.
    - Compare the sorted versions. If they are identical strings (e.g., both become "aaagmnr"), they are anagrams.
    - *Critique:* Simple one-liner. Time complexity is dominated by sorting ($O(N \log N)$).
- **Approach 2: Hash Map / Frequency Array ($O(N)$):**
    - Use a dictionary (or array of size 26) to count characters in `s`.
    - Decrement counts for characters in `t`.
    - If all counts return to 0, it's an anagram.
    - *Critique:* Faster for very long strings, but uses slightly more code.

### **Step 5: Plan Before Coding (Sorting Approach)**

**Pseudocode:**

Plaintext

`function isAnagram(s, t):
    // 1. Quick Check
    if length(s) != length(t):
        return False

    // 2. Normalize
    sorted_s = sort characters of s
    sorted_t = sort characters of t

    // 3. Compare
    if sorted_s == sorted_t:
        return True
    else:
        return False`

### **Step 6: Consider Edge Cases**

- **Different Lengths:** `s="a"`, `t="aa"`. Handled by length check.
- **Empty Strings:** `s=""`, `t=""`. `sorted` returns `[]`. `[] == []` is True. Correct.
- **Case Sensitivity:** Problem implies lowercase English letters. If mixed case, would need `.lower()`.

### **Step 7: Complexity Analysis**

- **Time Complexity:** $O(N \log N)$. This is the cost of sorting the strings. Comparing them takes $O(N)$, so sorting dominates.
- **Space Complexity:** $O(N)$. Python's `sorted()` function returns a new list of characters, consuming memory proportional to the string length.

### **Step 8: Review and Reflect**

- **Why does this work?** Sorting canonicalizes the data. It forces the characters into a specific order. If the "ingredients" are the same, the sorted result must be identical.

---

# **Code Explanation**

### **The Analogy: The Lego Castle**

Imagine you have two Lego castles built with random blocks. You want to know if they are made of the **exact same** set of bricks.

- **Method (Sorting):** You smash both castles completely and line up every single brick in a straight line by color and size (Red 2x2s, then Red 2x4s, then Blue...).
- If the two lines of bricks look exactly identical, the original castles were anagrams.

### **Step 1: The Length Check**

**Code:**

Python

        `if len(s) != len(t):
            return False`

- **What it does:**
    - If the two strings have a different number of characters, they mathematically cannot be anagrams.
    - This is an $O(1)$ check that saves time.

### **Step 2: Sorting and Comparing**

**Code:**

Python

        `return sorted(s) == sorted(t)`

- **What it does:**
    - `sorted(s)`: Takes string `"cab"` and creates a list `['a', 'b', 'c']`.
    - `sorted(t)`: Takes string `"abc"` and creates a list `['a', 'b', 'c']`.
    - `==`: Compares the two lists element by element. If they match perfectly, it returns `True`.

---

# **Analysis Summary (Deep Revision Framework)**

### **The Core Idea:**

The one-sentence summary is: **"Two strings are anagrams if and only if they become identical when their characters are sorted alphabetically."**

### **Data Structure Choice:**

- **List (via Sorting):** Used to hold the organized characters for comparison.

### **Algorithm Pattern:**

- **Sorting:** Canonicalization of data to make comparison trivial.

### **Complexity:**

- **Time:** $O(N \log N)$ (due to Timsort).
- **Space:** $O(N)$ (to store sorted lists).

### **Articulate the Solution:**

"I first checked if the strings had different lengths; if so, I returned False immediately."

"Then, I sorted both strings using Python's built-in sort function."

"Finally, I compared the sorted versions. If they were equal, the strings were anagrams."

### **Spaced Repetition & Follow-ups:**

- **Interview Follow-up:** "Can you solve this in $O(N)$ time?"
    - **Answer:** Yes, use a Hash Map (Dictionary) or a fixed-size array (26 integers) to count character frequencies.
- **Unicode:** "What if the inputs contain unicode characters?"
    - **Answer:** Sorting still works perfectly. The Hash Map approach would require a generalized map (like Python's `dict`) rather than a fixed-size array.

---

# **Key Notes**

- **Performance:** While $O(N \log N)$ is technically slower than $O(N)$ hashing, for short strings (common in interview inputs), the sorting approach is very fast and extremely concise (1 line).
- **Python Specific:** `sorted()` returns a **list**. If you wanted a string back, you would need `''.join(sorted(s))`. However, comparing the lists directly works fine.
- **Space Trade-off:** Be aware that `sorted()` creates new lists. If space is tight (embedded systems), this might not be optimal compared to counting.