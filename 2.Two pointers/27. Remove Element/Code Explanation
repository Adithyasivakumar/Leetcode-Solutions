## **27. Remove Element**

### Problem Statement

Given an array `nums` and a value `val`, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

---

### Step 1: Understand the Problem

- **Input:** Array `nums`, integer `val`
- **Output:** Length of array after removing all instances of `val` (in-place)
- **Constraints:** Modify in-place, use O(1) extra space

---

### Step 2: Work Through Examples

**Example:**

- Input: `nums = [3,2,2,3]`, `val = 3`
- Output: `2`, `nums = [2,2,_,_]`

---

### Step 3: Identify the Problem Type

- Array manipulation
- In-place removal of specific value
- Two-pointer technique is common

---

### Step 4: Think About Approaches

### Brute Force

- Shift elements left each time you find `val` (inefficient).

### Optimal Approach (Two Pointers)

- Use one pointer to track the position to overwrite (`i`).
- Use another pointer to scan the array (`j`).

---

### Step 5: Plan Before Coding

**Pseudocode:**

1. Initialize `i = 0`.
2. For each `j` in `nums`:
    - If `nums[j] != val`, set `nums[i] = nums[j]` and increment `i`.
3. Return `i` (new length).

---

### Step 6: Consider Edge Cases

- Empty array
- `val` not present in array
- All elements are `val`

---

### Step 7: Complexity Analysis

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

### Step 8: Review and Reflect

- Why does this work? It overwrites only the elements not equal to `val`.
- Can it be improved? This is optimal for in-place removal.