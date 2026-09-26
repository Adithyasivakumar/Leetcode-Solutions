## **349. Intersection of Two Arrays**

### Problem Statement

Given two integer arrays `nums1` and `nums2`, return an array of their intersection.

Each element in the result must be unique, and you may return the result in any order.

---

### Step 1: Understand the Problem

- **Input:** Two integer arrays `nums1` and `nums2`
- **Output:** Array of unique elements present in both arrays
- **Constraints:** Result must have unique elements; order does not matter

---

### Step 2: Work Through Examples

**Example:**

- Input: `nums1 = [1,2,2,1]`, `nums2 = [2,2]`
    
    Output: `[2]`
    
- Input: `nums1 = [4,9,5]`, `nums2 = [9,4,9,8,4]`
    
    Output: `[9,4]` or `[4,9]`
    

---

### Step 3: Identify the Problem Type

- Set intersection
- Remove duplicates

---

### Step 4: Think About Approaches

### Brute Force

- For each element in `nums1`, check if it exists in `nums2` and not already in result (O(n*m))

### Optimal Approach (Using Sets)

- Convert both arrays to sets to remove duplicates
- Find intersection using set operations (O(n + m))

---

### Step 5: Plan Before Coding

**Pseudocode:**

1. Convert `nums1` and `nums2` to sets
2. Find intersection of the two sets
3. Return the intersection as a listresult ^= num

---

### Step 6: Consider Edge Cases

- One or both arrays are empty
- No intersection
- All elements intersect

---

### Step 7: Complexity Analysis

- **Time Complexity:** O(n + m) (where n and m are lengths of nums1 and nums2)
- **Space Complexity:** O(n + m) (for the sets)

---

### Step 8: Review and Reflect

- Why does this work? Sets automatically handle uniqueness and intersection is efficient.
- Can it be improved? This is optimal for this problem.