### **Problem Explanation**

**28. Find the Index of the First Occurrence in a String**

**Step 1: Understand the Problem**

- **Input:** Two strings, `haystack` and `needle`.
- **Output:** An integer representing the index.
- **Goal:** Find the starting index of the **first occurrence** of the substring `needle` within the string `haystack`.
- **Constraint:** If `needle` is not part of `haystack`, return `1`.

---

**Step 2: Work Through Examples**

- **Example 1: `haystack = "sadbutsad", needle = "sad"`**
    - "sad" appears at index 0 and index 6.
    - The first occurrence is at index 0.
    - **Output:** `0`.
- **Example 2: `haystack = "leetcode", needle = "leeto"`**
    - "leeto" is not in "leetcode".
    - **Output:** `1`.
- **Example 3: `haystack = "hello", needle = "ll"`**
    - "ll" starts at index 2.
    - **Output:** `2`.

---

**Step 3: Identify the Problem Type**

- String Manipulation
- **Substring Search / Pattern Matching**
- **Sliding Window**

---

**Step 4: Think About Approaches**

- **Built-in Functions (Optimal for Real World):** Use `haystack.find(needle)` or `haystack.index(needle)`. Fast and clean.
- **Sliding Window (Your Implementation):** Iterate through `haystack`. At each position, check if the substring starting there matches `needle`. This is O(N*M) time.
- **KMP Algorithm (Advanced):** Uses preprocessing to skip characters and achieve O(N+M) time. (Usually overkill for interviews unless specified).

---

**Step 5: Plan Before Coding**

- **Pseudocode (Sliding Window):**
    
    `function strStr(haystack, needle):
      // 1. Get lengths of both strings.
      n = length of haystack
      m = length of needle
    
      // 2. Loop through haystack. We stop when the remaining part is shorter than needle.
      //    Range is 0 to n - m + 1.
      For i from 0 to n - m:
        // 3. Extract substring of length m starting at i.
        substring = haystack[i : i + m]
    
        // 4. Compare substring with needle.
        if substring equals needle:
          return i // Found match.
    
      // 5. If loop finishes without match.
      return -1`
    

---

**Step 6: Consider Edge Cases**

- **Empty `needle`:** Should return 0 (standard convention).
- **`needle` longer than `haystack`:** Loop range will be empty, returns -1. Correct.
- **`needle` equals `haystack`:** Loop runs once at index 0. Returns 0. Correct.

---

**Step 7: Complexity Analysis**

- **Time Complexity: O((N - M) * M)**, which simplifies to **O(N * M)**. We check `N-M` positions, and each check involves comparing/slicing `M` characters.
- **Space Complexity: O(1)** (auxiliary). Python slicing creates a temporary string copy of size M, so strictly it's O(M).

---

**Step 8: Review and Reflect**

- **Why does this work?** It systematically checks every possible starting position for the `needle`. If a match exists, this brute-force scan is guaranteed to find the first one.

---

### **Code Explanation**

### The Analogy: The Stencil

Think of `needle` as a stencil word cut out of a piece of cardboard. You slide this stencil over the long text (`haystack`) one letter at a time to see if the letters underneath perfectly match the cutout.

- **`haystack`**: The long text on the page.
- **`needle`**: The stencil word.
- **`i`**: The position of the left edge of your stencil.

---

### **Step 1: The Loop Range**

**Code:**

Python

`for i in range(n - m + 1):`

- **What it does:** This decides how far you can slide the stencil.
- **Analogy:** If the text is 10 letters long and your stencil is 3 letters long, you can't place the stencil starting at the 9th letter (index 8) because it would hang off the edge of the paper. You stop when the stencil just fits at the very end.

---

### **Step 2: The Window Check**

**Code:**

Python

    `if haystack[i : i + m] == needle:
        return i`

- **What it does:**
    - `haystack[i : i + m]`: This looks through the stencil. It grabs the exact chunk of text under the stencil.
    - `== needle`: It asks, "Does this chunk look exactly like the word on my stencil?"
- **Analogy:** If the letters match perfectly, you shout "Found it!" and point to the starting position `i`.

---

### **Step 3: Not Found**

**Code:**

Python

`return -1`

- **What it does:** If you slide the stencil all the way to the end and never find a match, you report `1`.

---

### **Analysis Summary (Deep Revision Framework)**

- **The Core Idea:**
The one-sentence summary is: "The code manually implements substring search by sliding a window of length `m` across the `haystack` and comparing it directly to the `needle` at every possible starting position."
- **Data Structure Choice:String Slicing**. Python's slicing feature creates a copy of the substring, making the comparison `haystack[i:i+m] == needle` very readable and easy to write.
- **Algorithm Pattern:Fixed-Size Sliding Window**. We check a window, if it doesn't match, we slide it one step to the right.
- **Complexity:**
    - **Time Complexity:** **O(N * M)**. In the worst case (e.g., `haystack = "aaaaaaab"`, `needle = "aab"`), we compare almost the entire needle at every single step.
    - **Space Complexity:** **O(1)** (Auxiliary). While slicing creates temporary strings, we don't store them, so memory usage is minimal.
- **Articulate the Solution:**
    1. "I chose a sliding window approach to manually implement the search."
    2. "First, I get the lengths of both strings, `n` and `m`."
    3. "I iterate through the `haystack` with an index `i`, stopping at `n - m` because any substring starting after that would be too short."
    4. "Inside the loop, I take a slice of `haystack` starting at `i` with length `m`."
    5. "I compare this slice directly to the `needle`."
    6. "If they match, I return `i`. If the loop finishes without a match, I return `1`."
- **Spaced Repetition & Follow-ups:**
    - **LeetCode 459. Repeated Substring Pattern**: Can you check if a string is made of a repeating substring?
    - **LeetCode 214. Shortest Palindrome**: Finding a specific pattern at the start of a string.