- **Example 1: `nums = [-1, 0, 1, 2, -1, -4]`**
    - Sorted: `[-4, -1, -1, 0, 1, 2]`
    - Fix `1`: Search for pair summing to `1`. Found `[-1, 2]` and `[0, 1]`. Triplets: `[-1, -1, 2]`, `[-1, 0, 1]`.
    - Fix next `1`: Skip (duplicate).
    - **Output:** `[[-1, -1, 2], [-1, 0, 1]]`.

---

**Step 3: Identify the Problem Type**

- Array Traversal
- **Sorting** + **Two Pointers**
- "N-Sum" Pattern

---

**Step 4: Think About Approaches**

- **Brute Force (O(N³)):** Three nested loops checking every combination. Too slow.
- **Hash Map (O(N²)):** Fix `i` and `j`, check for `(nums[i] + nums[j])` in a hash set. Handling duplicate triplets is very messy with this approach (requires sorting the result triplets and storing in a set).
- **Sorting + Two Pointers (Optimal):** Sort the array first. Fix one number (`i`), then use the "Two Sum II" logic (two pointers) to find the other two. Sorting makes avoiding duplicates easy: just skip adjacent identical numbers.

---

**Step 5: Plan Before Coding**

- **Pseudocode:**
    
    `function threeSum(nums):
      sort(nums)
      result = []
    
      For i from 0 to len(nums)-1:
        // Skip duplicates for the first number
        if i > 0 and nums[i] == nums[i-1], continue.
    
        // Optimization: If smallest number > 0, we can't sum to 0.
        if nums[i] > 0, break.
    
        left = i + 1, right = len(nums) - 1
        target = 0 - nums[i]
    
        while left < right:
           sum = nums[left] + nums[right]
           if sum == target:
             add [nums[i], nums[left], nums[right]] to result
             // Skip duplicates for the second/third numbers
             while left < right and nums[left] == nums[left+1], left++
             while left < right and nums[right] == nums[right-1], right--
             left++, right--
           elif sum < target:
             left++
           else:
             right--
      return result`
    

---

**Step 6: Complexity Analysis**

- **Time Complexity: O(N²)**. Sorting takes O(N log N). The outer loop runs N times, and the inner two-pointer scan takes O(N). Total is roughly $N^2$.
- **Space Complexity: O(1)** or **O(N)** depending on the sorting implementation (ignoring the space for the output list).

---

**Step 7: Review and Reflect**

- **Why does this work?** Sorting is the superpower here. It allows us to convert the problem into N iterations of "Two Sum II". It also makes duplicate detection trivial (just check neighbors).

---

### **Code Explanation**

### The Analogy: The Anchor and the Search Party

Think of finding a triplet as a team effort.

- **`nums[i]`**: The **Anchor**. This person stands still at a specific number and says, "I am part of the team. Find me two partners that make our total zero."
- **`left` and `right`**: The **Search Party**. They run the standard "Two Sum II" strategy on the rest of the line to find the perfect partners for the Anchor.

---

### **Step 1: The Setup (Sorting)**

**Code:** `nums.sort()`

- **Why?** Without sorting, we can't use the Two Pointer technique, and skipping duplicates would be a nightmare. Sorting organizes the chaos.

---

### **Step 2: The Anchor Loop**

**Code:** `for i in range(n):`

- **What it does:** We iterate through the list, selecting one number at a time to be the "Anchor".

Duplicate Check:

Code: if i > 0 and nums[i] == nums[i - 1]: continue

- **Analogy:** If the current Anchor (`nums[i]`) is exactly the same number as the *previous* Anchor (`nums[i-1]`), we skip it. Why? Because the previous Anchor has already found *all* possible triplets involving that number. Doing it again would just produce duplicates.

Early Exit:

Code: if nums[i] > 0: break

- **Why?** Since the array is sorted, if the Anchor is positive (e.g., 5), all numbers to the right are also positive. It is impossible to add three positive numbers to get 0.

---

### **Step 3: The Search Party (Two Pointers)**

**Code:**

Python

`left = i + 1
right = n - 1
while left < right:`

- **Analogy:** We set up our `left` and `right` pointers on the *remainder* of the array (to the right of the Anchor). We are now solving **Two Sum** where the target is `nums[i]`.

---

### **Step 4: Finding a Match**

**Code:** `if total > 0: right -= 1` ... `elif total < 0: left += 1`

- Standard Two Sum logic. If the sum is too big, move the big pointer left. If too small, move the small pointer right.

**Code:** `else: result.append(...)`

- We found a valid triplet! We add it to the list.

---

### **Step 5: Skipping Duplicates (Inner Loop)**

**Code:**

Python

`while left < right and nums[left] == nums[left - 1]: left += 1
while left < right and nums[right] == nums[right + 1]: right -= 1`

- **Note:** Your code actually put these checks *after* `left += 1` and `right -= 1`, checking `nums[left] == nums[left - 1]`. This is correct logic (checking current against previous after moving).
- **Analogy:** Once the Search Party finds a valid pair (e.g., -2 and 2), they must check if the *next* available numbers are identical. If `left` is currently at -2 and the next number is also -2, using it would create a duplicate triplet. So, they skip all identical numbers to find fresh candidates.

---

### **Analysis Summary (Deep Revision Framework)**

- The Core Idea:
    
    "The code sorts the array to handle duplicates and then iterates through it, fixing one number (the anchor) and using the two-pointer technique to find pairs that sum to the negative of the anchor."
    
- Data Structure Choice:
    
    List (Sorted). Sorting is essential here. It enables the O(N) two-pointer scan and makes duplicate detection an O(1) check against the previous element.
    
- Algorithm Pattern:
    
    Two Pointers (Nested). It's the "Two Sum II" pattern nested inside a for loop. This is the standard solution for 3Sum, 3Sum Closest, and 4Sum.
    
- **Complexity:**
    - **Time:** $O(N^2)$. (Outer loop N * Inner loop N).
    - **Space:** $O(1)$ or $O(N)$ depending on sort implementation.
- **Articulate the Solution:**
    1. "First, I sort the array. This is critical for the two-pointer approach and avoiding duplicates."
    2. "I loop through the array with index `i`. `nums[i]` is my first number."
    3. "If `nums[i]` is the same as the previous number, I skip it to avoid duplicate triplets."
    4. "I set `left` to `i+1` and `right` to the end of the array."
    5. "I calculate the sum. If it's < 0, I increment `left`. If > 0, I decrement `right`."
    6. "If it's 0, I record the triplet. Then, crucially, I increment `left` and decrement `right`, AND loop to skip any subsequent values that are identical to the ones I just used."
- **Spaced Repetition & Follow-ups:**
    - **LeetCode 16. 3Sum Closest**: Very similar, but instead of `sum == 0`, you track the minimum difference `abs(sum - target)`.
    - **LeetCode 18. 4Sum**: Adds another layer of loops. You fix `i`, then fix `j`, then use two pointers for `k` and `l`. (Complexity $O(N^3)$).