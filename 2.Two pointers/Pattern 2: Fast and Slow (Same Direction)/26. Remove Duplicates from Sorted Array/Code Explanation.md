## **26. Remove Duplicates from Sorted Array**

### Problem Statement

Given a sorted array `nums`, remove the duplicates in-place such that each element appears only once and return the new length.

Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

---

### Step 1: Understand the Problem

- **Input:** Sorted array `nums`
- **Output:** Length of array after removing duplicates (in-place)
- **Constraints:** Must modify in-place, use O(1) extra space

---

### Step 2: Work Through Examples

**Example:**

- Input: `nums = [1,1,2]`
- Output: `2`, `nums = [1,2,_]` (the underscore means it doesn't matter)

---

### Step 3: Identify the Problem Type

- Array manipulation
- In-place removal of duplicates
- Two-pointer technique is common for this type

---

### Step 4: Think About Approaches

### Brute Force

- Remove duplicates by shifting elements, but this is inefficient.

### Optimal Approach (Two Pointers)

- Use one pointer (`i`) for the place to insert the next unique element.
- Use another pointer (`j`) to scan through the array.

---

### Step 5: Plan Before Coding

**Pseudocode:**

1. If array is empty, return 0.
2. Initialize `i = 0`.
3. For `j` from 1 to end:
    - If `nums[j] != nums[i]`, increment `i` and set `nums[i] = nums[j]`.
4. Return `i + 1` (length of unique elements).

---

### Step 6: Consider Edge Cases

- Empty array
- Array with all unique elements
- Array with all duplicates

---

### Step 7: Complexity Analysis

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

### Step 8: Review and Reflect

- Why does this work? The two-pointer method efficiently overwrites duplicates.
- Can it be improved? This is optimal for in-place removal.