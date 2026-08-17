## **35. Search Insert Position**

### Problem Statement

Given a sorted array of distinct integers and a target value, return the index if the target is found.

If not, return the index where it would be if it were inserted in order.

---

### Step 1: Understand the Problem

- **Input:** Sorted array `nums`, integer `target`
- **Output:** Index of `target` if found, else index where it should be inserted
- **Constraints:** No duplicates, array is sorted

---

### Step 2: Work Through Examples

**Example:**

- Input: `nums = [1,3,5,6]`, `target = 5`Output: `2`
- Input: `nums = [1,3,5,6]`, `target = 2`Output: `1`
- Input: `nums = [1,3,5,6]`, `target = 7`Output: `4`

---

### Step 3: Identify the Problem Type

- Array search
- Sorted array → Binary search is optimal

---

### Step 4: Think About Approaches

### Brute Force

- Linear scan to find the position (O(n))

### Optimal Approach (Binary Search)

- Use binary search to find the target or the insert position (O(log n))

---

### Step 5: Plan Before Coding

**Pseudocode:**

1. Set `left = 0`, `right = len(nums) - 1`
2. While `left <= right`:
    - Compute `mid = (left + right) // 2`
    - If `nums[mid] == target`, return `mid`
    - If `nums[mid] < target`, move `left` to `mid + 1`
    - Else, move `right` to `mid - 1`
3. Return `left` (insert position)

---

### Step 6: Consider Edge Cases

- Target smaller than all elements
- Target larger than all elements
- Target in the middle

---

### Step 7: Complexity Analysis

- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)

---

### Step 8: Review and Reflect

- Why does this work? Binary search efficiently finds the position in a sorted array.
- Can it be improved? This is optimal for this problem.