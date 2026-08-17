## **Move Zeroes**

### Problem Statement

Given an integer array `nums`, move all zeros to the end of the array while maintaining the relative order of the non-zero elements. Do this in-place without making a copy of the array.

---

### Step 1: Understand the Problem

- **Input:** List of integers `nums`
- **Output:** The same list with all zeros moved to the end, non-zero elements in original order
- **Constraints:**
    - 1 ≤ len(nums) ≤ 10⁴
    - 2³¹ ≤ nums[i] ≤ 2³¹ - 1

---

### Step 2: Work Through Examples

**Example 1:**

- Input: `nums = [0,1,0,3,12]`
- Output: `[1,3,12,0,0]`

**Example 2:**

- Input: `nums = [0,0,1]`
- Output: `[1,0,0]`

- `i` tracks the next position to place a non-zero.
- `j` iterates through the array.
- When a non-zero is found at `j`, it is swapped to position `i`, and `i` is incremented.
- All zeros are pushed to the end, and the order of non-zeros is preserved.

---

### Step 3: Identify the Problem Type

- Array manipulation
- In-place modification
- Two-pointer technique

---

### Step 4: Think About Approaches

### Brute Force

- Create a new array, copy non-zero elements, then fill the rest with zeros.
- **Time Complexity:** O(n), **Space Complexity:** O(n)

### Optimal Approach (Two Pointers)

- Use two pointers: one (`i`) for the position to place the next non-zero, and one (`j`) to iterate through the array.
- Swap non-zero elements to the front as you find them.
- **Time Complexity:** O(n), **Space Complexity:** O(1)

---

### Step 5: Plan Before Coding

**Pseudocode:**

1. Initialize `i = 0`
2. For each `j` from 0 to len(nums) - 1:
    - If `nums[j]` is not zero:
        - Swap `nums[i]` and `nums[j]`
        - Increment `i`
3. The array is now modified in-place with all zeros at the end.

---

### Step 6: Consider Edge Cases

- All elements are zero (array remains the same)
- No zeros (array remains the same)
- Zeros at the start, middle, or end

---

### Step 7: Complexity Analysis

- **Time Complexity:** O(n) (single pass through the array)
- **Space Complexity:** O(1) (in-place)

---

### Step 8: Review and Reflect

- **Why does this work?**The algorithm ensures every non-zero is moved to the front in order, and zeros are pushed to the back by swapping.
- **Can it be improved?**This is optimal for time and space.