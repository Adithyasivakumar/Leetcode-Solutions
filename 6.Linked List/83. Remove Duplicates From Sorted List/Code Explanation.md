## **83. Remove Duplicates from Sorted List**

### Problem Statement

Given the head of a sorted linked list, delete all duplicates such that each element appears only once.

Return the linked list sorted as well.

---

### Step 1: Understand the Problem

- **Input:** Head of a sorted singly linked list
- **Output:** Head of the linked list with duplicates removed (in-place)
- **Constraints:** Must operate in-place, O(1) extra space

---

### Step 2: Work Through Examples

**Example:**

- Input: `1 -> 1 -> 2`
- Output: `1 -> 2`

---

### Step 3: Identify the Problem Type

- Linked list manipulation
- In-place removal of duplicates
- One-pass traversal

---

### Step 4: Think About Approaches

### Brute Force

- Use extra space to track seen values (not allowed by constraints).

### Optimal Approach (One Pointer)

- Since the list is sorted, duplicates are consecutive.
- Traverse the list, compare current node with next node.
- If duplicate, skip the next node.

---

### Step 5: Plan Before Coding

**Pseudocode:**

1. Initialize `current = head`
2. While `current` and `current.next` exist:
    - If `current.val == current.next.val`, skip `current.next`
    - Else, move `current` forward

---

### Step 6: Consider Edge Cases

- Empty list
- List with all unique elements
- List with all duplicates

---

### Step 7: Complexity Analysis

- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

---

### Step 8: Review and Reflect

- Why does this work? The sorted property ensures duplicates are adjacent.
- Can it be improved? This is optimal for in-place removal.
