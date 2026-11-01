# **704. Binary Search**

**Step 1: Understand the Problem**

- **Input:** A **sorted** array of integers `nums` and a `target` integer.
- **Output:** An integer representing an index.
- **Goal:**
    1. If the `target` exists in the array, return its index.
    2. If the `target` does not exist, return `1`.
- **Crucial Prerequisite:** The algorithm relies on the fact that the array is **sorted**.

---

**Step 2: Work Through Examples**

- **Example 1: `nums = [-1,0,3,5,9,12]`, `target = 9`**
    - The target `9` is found at index `4`.
    - **Output:** `4`.
- **Example 2: `nums = [-1,0,3,5,9,12]`, `target = 2`**
    - The target `2` is not in the array.
    - **Output:** `1`.

---

**Step 3: Identify the Problem Type**

- Array Searching
- **Binary Search** (the most efficient search algorithm for a sorted array)

---

**Step 4: Think About Approaches**

- **Linear Scan (O(n)):** Loop through the array from the beginning until you find the target. This is simple but less efficient than what is possible.
- **Binary Search (O(log n)):** The implemented solution. This is the optimal approach. By repeatedly dividing the search space in half, we can find the target very quickly.

---

**Step 5: Plan Before Coding**

- **Pseudocode:**
    
    `function search(nums, target):
      // 1. Set up pointers for the search space (the entire array).
      left = 0
      right = length of nums - 1
    
      // 2. Loop as long as the search space is valid (left pointer is not past the right).
      while left <= right:
        // 3. Find the middle index of the current search space.
        mid = (left + right) / 2
    
        // 4. Compare the middle element with the target.
        if nums[mid] equals target:
          return mid // Target found.
        else if nums[mid] is less than target:
          // Target must be in the right half. Discard the left half.
          left = mid + 1
        else:
          // Target must be in the left half. Discard the right half.
          right = mid - 1
    
      // 5. If the loop finishes, the target was not found in the array.
      return -1`
    

---

**Step 6: Consider Edge Cases**

- **Target not in array:** The loop will finish when `left` becomes greater than `right`. The function will correctly return `1`.
- **Empty array:** `right` will be -1, `left` will be 0. The `while` loop condition `0 <= -1` is false, so the loop is skipped and it correctly returns `1`.
- **Single-element array:** The loop runs once, checks the single element, and returns its index or -1 correctly.

---

**Step 7: Complexity Analysis**

- **Time Complexity: O(log n)**. With each step of the `while` loop, the algorithm discards half of the remaining search space. This logarithmic reduction is extremely fast.
- **Space Complexity: O(1)**. The algorithm only uses a few variables (`left`, `right`, `mid`). The memory usage is constant.

---

**Step 8: Review and Reflect**

- **Why does this work?** Binary Search is a perfect algorithm for sorted arrays because it can make intelligent decisions to eliminate large portions of the data at each step, homing in on the answer very quickly.
- **Can it be improved?** No, in terms of time and space complexity, this is the optimal solution for searching a sorted array.

---

### **Code Explanation**

### The Analogy: The Dictionary Game

Think of finding a number in a sorted array like finding a word in a physical dictionary. You don't start at page 1; you open it to the middle and decide which half to search next.

- **`nums`**: A sorted dictionary of numbers.
- **`left`, `right`**: Your hands, holding the section of the dictionary you're currently searching.
- **`mid`**: The page you open to in the middle of your section.

---

### **Step 1: The Setup**

**Code:**

Python

`left, right = 0, len(nums) - 1`

- **What it does:** It sets up your initial search space.
- **Analogy:** Your `left` hand starts at the very beginning of the dictionary (index 0), and your `right` hand starts at the very end (the last index).

---

### **Step 2: The Loop**

**Code:**

Python

`while left <= right:`

- **What it does:** This starts a loop that will keep running as long as your hands haven't crossed. If they cross (`left` becomes greater than `right`), it means the search space is empty and the word isn't in the dictionary.

---

### **Step 3: The Three Decisions**

This is the core of the Binary Search, where you decide which half of the dictionary to discard.

**Decision 1: You found it!Code:**

Python

`mid = (left + right) // 2
if nums[mid] == target:
    return mid`

- **Analogy:** You open to the middle page (`mid`) and the number you see (`nums[mid]`) is exactly your `target`. Game over! You return the page number (`mid`).

**Decision 2: The target is bigger.Code:**

Python

`elif nums[mid] < target:
    left = mid + 1`

- **Analogy:** The number on the middle page is smaller than your `target`. You know your target must be in the **right half** of your current section. So, you move your `left` hand to the page right after the middle (`mid + 1`) and completely ignore the left half.

**Decision 3: The target is smaller.Code:**

Python

`else:
    right = mid - 1`

- **Analogy:** The number on the middle page is bigger than your `target`. You know your target must be in the **left half**. So, you move your `right` hand to the page just before the middle (`mid - 1`) and completely ignore the right half.

---

### **Step 4: The Final Result (Target Not Found)**

**Code:**

Python

`return -1`

- **What it does:** This line is outside the loop. It is only ever reached if the `while` loop finishes (meaning your `left` hand has crossed your `right` hand).
- **Analogy:** If you've narrowed down your search so much that there are no pages left to check, it means the word was never in the dictionary. You report failure by returning `1`.

---

### **Analysis Summary (Deep Revision Framework)**

- **The Core Idea:**
The one-sentence summary is: "The code uses a classic Binary Search to efficiently find a target in a sorted array by repeatedly dividing the search space in half."
- **Data Structure Choice:**
The algorithm operates directly on the input **list (array)**. The most important property of this data structure for this problem is that it is **sorted**. Binary search is only possible on sorted data because that's what allows us to make intelligent decisions about which half of the array to discard.
- **Algorithm Pattern:**
This is a perfect implementation of the **Binary Search** algorithm. It is one of the most fundamental and important algorithms in computer science, used for searching in any sorted sequence.
- **Complexity:**
    - **Time Complexity: O(log n)**. With each iteration of the `while` loop, the algorithm discards half of the remaining search space. This logarithmic behavior is extremely fast.
    - **Space Complexity: O(1)**. The algorithm only uses a few variables (`left`, `right`, `mid`). Its memory usage is constant.
- **Articulate the Solution:**
    1. "My solution uses Binary Search, which is the optimal algorithm for searching in a sorted array."
    2. "I initialize `left` and `right` pointers to define the search space, which starts as the entire array."
    3. "In a `while` loop that continues as long as `left` is less than or equal to `right`, I calculate the `mid` point."
    4. "If the element at `mid` is the target, I return `mid`."
    5. "If the element at `mid` is less than the target, I know the target must be in the right half, so I discard the left half by updating `left = mid + 1`."
    6. "Otherwise, the target must be in the left half, so I discard the right half by updating `right = mid - 1`."
    7. "If the loop finishes without finding the target, I return `1`."
- **Spaced Repetition & Follow-ups:**
Binary Search is a foundational pattern. Great follow-up problems that use variations of this pattern include:
    - **LeetCode 35. Search Insert Position**: We've already discussed this. It's a slight variation where you return the insertion point if the target isn't found.
    - **LeetCode 34. Find First and Last Position of Element in Sorted Array**: Requires a modified binary search to find the boundaries of a target.
    - **LeetCode 153. Find Minimum in Rotated Sorted Array**: Applying binary search on a "broken" or rotated sorted array.