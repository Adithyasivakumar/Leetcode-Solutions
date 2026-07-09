# **Problem Explanation**

## **905. Sort Array By Parity**

### **Step 1: Understand the Problem**

- **Input:** An integer array `nums`.
- **Output:** An array where all even integers appear before all odd integers.
- **Order:** The relative order of the even numbers or odd numbers does *not* matter. Any valid permutation is accepted.
- **Goal:** Move all evens to the front and odds to the back.

### **Step 2: Work Through Examples**

- **Example 1:** `nums = [3, 1, 2, 4]`
    - Evens: `2, 4`
    - Odds: `3, 1`
    - **Possible Output:** `[2, 4, 3, 1]`, `[4, 2, 3, 1]`, `[2, 4, 1, 3]`, etc. All are valid.
- **Example 2:** `nums = [0]`
    - **Output:** `[0]`.

### **Step 3: Identify the Problem Type**

- **Array Partitioning:** Separating elements based on a condition (parity).
- **Two Pointers (Optimal):** Can be done in-place.
- **Auxiliary Array (Your Solution):** Easier to implement but uses extra space.

### **Step 4: Think About Approaches**

- **Approach 1: Two Pass / Auxiliary Arrays (Your Solution)**
    - Create two lists: `even` and `odd`.
    - Iterate through `nums`. If even, add to `even`. If odd, add to `odd`.
    - Concatenate `even + odd`.
    - *Pros:* Very intuitive, easy to write.
    - *Cons:* Uses $O(N)$ extra space.
- **Approach 2: In-Place Swap (Two Pointers)**
    - Maintain a pointer `i` at the start and `j` at the end.
    - If `nums[i]` is odd and `nums[j]` is even, swap them.
    - If `nums[i]` is even, it's in the correct place, so increment `i`.
    - If `nums[j]` is odd, it's in the correct place, so decrement `j`.
    - *Pros:* $O(1)$ space.
- **Approach 3: In-Place Partition (QuickSort logic)**
    - Maintain a pointer `j` that tracks the position of the last even element found.
    - Iterate `i` through the array. If `nums[i]` is even, swap `nums[i]` with `nums[j]` and increment `j`.

### **Step 5: Plan Before Coding (Your Approach)**

**Pseudocode:**

Plaintext

`function sortArrayByParity(nums):
    even_list = empty list
    odd_list = empty list

    for num in nums:
        if num is even:
            add num to even_list
        else:
            add num to odd_list

    return combine(even_list, odd_list)`

### **Step 6: Consider Edge Cases**

- **Empty Array:** Loop doesn't run. Returns empty list. Correct.
- **All Evens:** `odd` list is empty. Returns `even + []`. Correct.
- **All Odds:** `even` list is empty. Returns `[] + odd`. Correct.

### **Step 7: Complexity Analysis**

- **Time Complexity:** $O(N)$. We iterate through the array once.
- **Space Complexity:** $O(N)$. We create new lists that hold a copy of all elements.

### **Step 8: Review and Reflect**

- **Why does this work?** It explicitly separates the data into buckets and rejoins them. It guarantees the condition (evens first) is met. While not space-optimal, it is perfectly valid and very readable.

---

# **Code Explanation**

### **The Analogy: The Playground Line-Up**

Imagine a teacher wants to line up students.

- **Rule:** Students with blue shirts (Evens) must stand at the front. Students with red shirts (Odds) must stand at the back.
- **Strategy (Your Code):** The teacher points to two different empty benches.
    - "If you have a blue shirt, go sit on Bench A."
    - "If you have a red shirt, go sit on Bench B."
    - Once everyone is seated, the teacher tells Bench A to line up first, followed immediately by Bench B.

### **Step 1: Bucketing**

**Code:**

Python

        `even = []
        odd = []`

- **What it does:** Creates two temporary storage spaces.

### **Step 2: Filtering**

**Code:**

Python

        `for num in nums:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)`

- **What it does:**
    - The modulo operator `% 2` checks for parity.
    - `0` remainder means Even.
    - `1` remainder means Odd.
    - We distribute the numbers into their respective buckets.

### **Step 3: Merging**

**Code:**

Python

        `final_array = even + odd
        return final_array`

- **What it does:** Python's list addition `+` concatenates the two lists. The `even` list comes first, satisfying the problem requirement.

---

# **Analysis Summary (Deep Revision Framework)**

### **The Core Idea:**

The one-sentence summary is: **"We iterate through the array, distributing numbers into separate 'even' and 'odd' lists based on their modulo 2 value, and then concatenate them to form the result."**

### **Data Structure Choice:**

- **Lists (Dynamic Arrays):** Used to temporarily hold the partitioned data.

### **Algorithm Pattern:**

- **Filtering / Two-Pass:** Technically a single pass to filter, then a merge operation.

### **Complexity:**

- **Time:** $O(N)$.
- **Space:** $O(N)$.

### **Articulate the Solution:**

"I created two separate lists, one for even numbers and one for odd numbers."

"I iterated through the input array. If a number was divisible by 2, I appended it to the even list; otherwise, I appended it to the odd list."

"Finally, I concatenated the even list with the odd list and returned the result."

### **Spaced Repetition & Follow-ups:**

- **Follow-up:** "Can you solve this in $O(1)$ space (in-place)?"
    - **Answer:** Yes, use the Two Pointer technique. Start pointers at `0` and `n-1`. Swap elements if `left` is odd and `right` is even.
- **Follow-up:** "Sort Array By Parity II" (LeetCode 922). (Evens at even indices, odds at odd indices).

---

# **Key Notes**

- **Trade-off:** Your solution is optimized for **Readability** and development speed. The In-Place solution is optimized for **Memory**. In an interview, start with this (if allowed) and offer the in-place optimization if asked.
- **Stability:** This approach is **stable** (it preserves the relative order of evens and odds). The in-place swap method is usually **unstable**.