## **1. Two Sum**

**LeetCode #1**

### Problem Statement

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

---

### Step 1: Understand the Problem

- **Input:** Array of integers `nums`, integer `target`
- **Output:** Indices of two numbers in `nums` that add up to `target`
- **Constraints:** Each input has exactly one solution; cannot use the same element twice.

---

### Step 2: Work Through Examples

**Example:**

- Input: `nums = [2,7,11,15]`, `target = 9`
- Output: `[0,1]` (because `nums[0] + nums[1] = 2 + 7 = 9`)

---

### Step 3: Identify the Problem Type

- Array problem
- Looking for a pair of numbers that sum to a target
- Classic use case for hash maps (dictionaries)

---

### Step 4: Think About Approaches

### Brute Force

- Check every pair of numbers.
- Time Complexity: O(n²)

### Optimized Approach

- Use a hash map to store numbers and their indices as you iterate.
- For each number, check if `target - num` exists in the hash map.
- Time Complexity: O(n)

---

### Step 5: Plan Before Coding

**Pseudocode:**

1. Create an empty hash map.
2. For each index and number in `nums`:
    - If `target - num` is in the hash map, return `[hash_map[target - num], index]`
    - Else, add `num` and its index to the hash map.

---

### Step 6: Consider Edge Cases

- Negative numbers
- Duplicates in the array
- Only one solution guaranteed

---

### Step 7: Complexity Analysis

- **Time Complexity:** O(n)
- **Space Complexity:** O(n)

---

### Step 8: Review and Reflect

- Why does this work? The hash map allows us to check for the complement in constant time.
- Can it be improved? This is already optimal for this problem.
