## **Problem Explanation**

### **167. Two Sum II - Input Array Is Sorted**

**Step 1: Understand the Problem**

- **Input:** A **sorted** array of integers `numbers` (1-indexed) and an integer `target`.
- **Output:** An array of two integers `[index1, index2]` representing the indices of the two numbers that add up to `target`.
- **Goal:** Find two numbers such that they add up to a specific target number.
- **Crucial Constraint:** The input array is **sorted in non-decreasing order**. The solution must use **constant extra space**.

---

**Step 2: Work Through Examples**

- **Example 1: `numbers = [2, 7, 11, 15], target = 9`**
    - Sum of 2 and 7 is 9. Indices are 1 and 2.
    - **Output:** `[1, 2]`.
- **Example 2: `numbers = [2, 3, 4], target = 6`**
    - Sum of 2 and 4 is 6. Indices are 1 and 3.
    - **Output:** `[1, 3]`.
- **Example 3: `numbers = [-1, 0], target = -1`**
    - Sum of -1 and 0 is -1. Indices are 1 and 2.
    - **Output:** `[1, 2]`.

---

**Step 3: Identify the Problem Type**

- Array Traversal
- **Two-Pointer Technique** (classic pattern for sorted arrays)
- Searching for a pair

---

**Step 4: Think About Approaches**

- **Hash Map (O(N) space):** The standard Two Sum approach. Works, but ignores the "sorted" property and violates the "constant space" requirement.
- **Binary Search (O(N log N)):** For each element, binary search for its complement. Better than brute force, but slower than optimal.
- **Two Pointers (The Optimal Solution):** Since the array is sorted, we can place pointers at the start and end. If the sum is too small, we move the start pointer to increase the sum. If the sum is too big, we move the end pointer to decrease the sum. This is O(N) time and O(1) space.

---

**Step 5: Plan Before Coding**

- **Pseudocode:**
    
    `function twoSum(numbers, target):
      // 1. Initialize two pointers at opposite ends.
      left = 0
      right = length of numbers - 1
    
      // 2. Loop until the pointers meet.
      while left < right:
        // 3. Calculate the current sum.
        current_sum = numbers[left] + numbers[right]
    
        // 4. Check if we found the target.
        if current_sum equals target:
          return [left + 1, right + 1] // Return 1-based indices.
    
        // 5. If sum is too large, we need a smaller number.
        else if current_sum > target:
          decrement right pointer
    
        // 6. If sum is too small, we need a larger number.
        else:
          increment left pointer
    
      // 7. No solution found (though problem guarantees one).
      return []`
    

---

**Step 6: Consider Edge Cases**

- **Minimum length array:** `[1, 2]`, `target=3`. Loop runs once, finds sum is 3, returns `[1, 2]`. Correct.
- **Negative numbers:** Sorted order handles negatives correctly (e.g., `[-3, 3]`, target `0`).

---

**Step 7: Complexity Analysis**

- **Time Complexity: O(N)**. In the worst case, the `left` and `right` pointers traverse the entire array once.
- **Space Complexity: O(1)**. We only use two integer variables for the pointers, regardless of the input size.

---

**Step 8: Review and Reflect**

- **Why does this work?** The sorted property gives us direction. We know that moving the `right` pointer left *always* decreases the sum (or keeps it same), and moving the `left` pointer right *always* increases the sum. This allows us to eliminate wrong pairs without checking them all.
- **Can it be improved?** No, this is the optimal time and space complexity.

---

### **Code Explanation**

### The Analogy: Tuning a Radio

Think of this problem like tuning a radio to a specific frequency (`target`). You have two knobs: a "Low" knob (`left`) that starts at the lowest frequency and a "High" knob (`right`) that starts at the highest.

- **`numbers`**: The available frequencies, sorted from low to high.
- **`target`**: The perfect frequency sum you want to hit.

---

### **Step 1: The Setup**

**Code:**

Python

`left = 0
right = len(numbers) - 1`

- **What it does:** It places your "Low" knob at the very beginning (smallest number) and your "High" knob at the very end (largest number).

---

### **Step 2: The Tuning Process**

**Code:**

Python

`while left < right:
    current_sum = numbers[left] + numbers[right]`

- **What it does:** You check the combined frequency of your current settings.
- **Analogy:** You listen to the sum of the Low and High knobs.

---

### **Step 3: Adjusting the Knobs**

**Case 1: Perfect MatchCode:**

Python

    `if current_sum == target:
        return [left + 1, right + 1]`

- **Analogy:** The frequency is perfect! You found the target. You report the positions of your knobs (adding 1 because the radio display is 1-indexed).

**Case 2: Too High (Too Loud)Code:**

Python

    `elif current_sum > target:
        right -= 1`

- **Analogy:** The sum is **too high**. You need a smaller number to bring the total down. Since the array is sorted, you know the only way to get a smaller number is to move the "High" knob to the left (pick the next largest number).

**Case 3: Too Low (Too Quiet)Code:**

Python

    `else:
        left += 1`

- **Analogy:** The sum is **too low**. You need a larger number to bring the total up. Since the array is sorted, you move the "Low" knob to the right (pick the next smallest number).

---

### **Analysis Summary (Deep Revision Framework)**

- **The Core Idea:**
The one-sentence summary is: "The code exploits the sorted property of the array by using two pointers starting at opposite ends, moving them inward to find the pair that sums to the target in O(N) time and O(1) space."
- **Data Structure Choice:**
The solution operates directly on the input **list (array)** using indices. Because the array is **sorted**, we don't need a hash map to find complements; the order itself guides our search.
- **Algorithm Pattern:**
This is the classic **Two Pointers (Opposite Ends)** pattern. It is the standard optimal strategy for finding pairs in a sorted array.
- **Complexity:**
    - **Time Complexity: O(N)**.
    - **Space Complexity: O(1)**.

### **Articulate the Solution:**

1. "My solution uses the two-pointer technique, which is optimal for sorted arrays."
2. "I initialize a `left` pointer at the start and a `right` pointer at the end."
3. "I loop while `left` is less than `right`, calculating the sum of the elements at these pointers."
4. "If the sum equals the target, I return the indices (adjusted by +1)."
5. "If the sum is greater than the target, I know I need a smaller sum, so I decrement the `right` pointer."
6. "If the sum is less than the target, I need a larger sum, so I increment the `left` pointer."
7. "This approach guarantees finding the unique solution in linear time without extra space."

### **Spaced Repetition & Follow-ups:**

- **LeetCode 15. 3Sum**: The most direct extension. You fix one number and use this 2-pointer logic to find the other two.
- **LeetCode 11. Container With Most Water**: Uses two pointers moving inward based on height constraints.
- **LeetCode 16. 3Sum Closest**: Finding a sum closest to a target using sorted array and pointers.