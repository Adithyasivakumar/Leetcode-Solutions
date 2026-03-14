## **Problem Explanation**

### **414. Third Distinct Maximum**

**Step 1: Understand the Problem**

- **Input:** An array of integers, `nums`.
- **Output:** A single integer.
- **Goal:** Find the third **distinct** (unique) maximum number in the array.
- **Special Rule:** If the array does not have three distinct maximum numbers, you must return the overall maximum number instead.

---

**Step 2: Work Through Examples**

- **Example 1: `nums = [3, 2, 1]`**
    - 1st distinct max: 3
    - 2nd distinct max: 2
    - 3rd distinct max: 1
    - **Output:** `1`.
- **Example 2: `nums = [1, 2]`**
    - 1st distinct max: 2
    - 2nd distinct max: 1
    - A third distinct maximum does not exist.
    - According to the rule, we return the overall maximum.
    - **Output:** `2`.
- **Example 3: `nums = [2, 2, 3, 1]`**
    - The numbers must be distinct. The duplicate `2` is counted only once.
    - 1st distinct max: 3
    - 2nd distinct max: 2
    - 3rd distinct max: 1
    - **Output:** `1`.

---

**Step 3: Identify the Problem Type**

- Array Traversal
- Finding the Kth Largest Element
- Handling Duplicates

---

**Step 4: Think About Approaches**

- **Sorting (O(N log N)):** Remove duplicates from the array by converting it to a set, then sort it. If the resulting list has at least three elements, the answer is the third element from the end. Otherwise, it's the last element. This is simple but doesn't meet the O(n) follow-up.
- **Single Pass (O(N)):** The implemented solution. Iterate through the array just once while keeping track of the three largest distinct numbers seen so far. This is the optimal approach requested by the follow-up.

---

**Step 5: Plan Before Coding**

- **Pseudocode:**
    
    `function thirdMax(nums):
      // 1. Initialize three variables to hold the top 3 distinct scores.
      first, second, third = negative_infinity, negative_infinity, negative_infinity
    
      // 2. Loop through each number in the array.
      For each num in nums:
        // 3. Skip if this number is a duplicate of our current top 3.
        if num is equal to first, second, or third, continue.
    
        // 4. Check if the number deserves a spot on the podium.
        if num > first:
          // Shift everyone down and place num at the top.
          third = second, second = first, first = num
        else if num > second:
          // Shift second down and place num there.
          third = second, second = num
        else if num > third:
          // Place num at third.
          third = num
    
      // 5. After the loop, decide what to return.
      if a third distinct max was never found (third is still negative_infinity):
        return first // Return the overall max.
      else:
        return third // Return the third max.`
    

---

**Step 6: Consider Edge Cases**

- **Fewer than 3 elements:** e.g., `[1, 2]`. The `third` variable will never be updated. The final check correctly returns `first`.
- **Fewer than 3 *distinct* elements:** e.g., `[2, 2, 1]`. `first` will be 2, `second` will be 1. `third` will never be updated. The final check correctly returns `first`.
- **Arrays with negative numbers:** Using `math.inf` as the initial value correctly handles all negative numbers and zeros.

---

**Step 7: Complexity Analysis**

- **Time Complexity: O(N)**. The solution iterates through the array exactly once.
- **Space Complexity: O(1)**. It only uses three extra variables (`first`, `second`, `third`), so the memory usage is constant.

---

**Step 8: Review and Reflect**

- **Why does this work?** The single-pass approach is optimal. The main challenges are correctly handling the "distinct" rule (which the `continue` statement does) and correctly managing the "shift-down" logic when a new maximum is found. The final check `if third == -math.inf:` correctly implements the rule for when a third maximum doesn't exist.
- **Can it be improved?** In terms of time and space complexity, this solution is optimal and correctly addresses all parts of the problem.

---

### **Code Explanation**

### The Analogy: The Winners' Podium

Think of this problem like finding the Gold, Silver, and Bronze medal winners in a race where scores must be unique.

- `first`: The Gold medal spot (the highest score).
- `second`: The Silver medal spot (the second-highest).
- `third`: The Bronze medal spot (the third-highest).

The key rule is that to win a medal, your score must be **distinct** (different) from the scores of the people already on the podium.

---

### **Step 1: The Setup**

**Code:**

Python

`first = -math.inf
second = -math.inf
third = -math.inf`

- **What it does:** It sets up our three podium spots.
- **Why `math.inf`?**: We initialize them to negative infinity, which is the smallest possible number. This guarantees that any number from the input list will be larger, allowing the code to correctly handle all possible inputs, including negative numbers and zeros. It's like starting with an empty podium where any score is a new high score.

---

### **Step 2: The Loop and The "Distinct" Rule**

**Code:**

Python

`for num in nums:
    if num == first or num == second or num == third:
        continue`

- **What it does:** The code looks at each `num` (each runner's score) in the list one by one.
- **The `if` statement** is the crucial check for the **"distinct"** rule. It asks: "Is this number *exactly the same* as a score already on our podium?"
- If the answer is yes, `continue` tells the code to **skip** this number and move on to the next one. This prevents duplicate scores from being processed.

---

### **Step 3: Updating the Podium**

This is the core of the algorithm, where it decides if a new number deserves a spot on the podium.

**If a new Gold medalist is found:Code:**

Python

`if num > first:
    third = second
    second = first
    first = num`

- **What it does:** This checks if the current `num` is a new Gold medalist (the largest number found so far).
- **The "Shift-Down":** If it is, everyone on the podium gets bumped down one spot:
    - The old `second` place becomes the new `third`.
    - The old `first` place becomes the new `second`.
    - The new `num` takes `first` place.

**If a new Silver medalist is found:Code:**

Python

`elif num > second:
    third = second
    second = num`

- **What it does:** If the number isn't a new Gold medalist, this checks if it's a new Silver medalist.
- **The "Shift-Down":** The old `second` place is bumped down to `third`, and the new `num` takes `second` place.

**If a new Bronze medalist is found:Code:**

Python

`elif num > third:
    third = num`

- **What it does:** If the number isn't a new Gold or Silver medalist, this checks if it's a new Bronze medalist. If so, it takes the `third` place spot.

---

### **Step 4: The Final Decision**

**Code:**

Python

`if third == -math.inf:
    return first
else:
    return third`

- **What it does:** After the loop has checked every number, this final part decides what to return based on the problem's rules.
- It asks: "Did we ever even find a Bronze medalist?" (Was the `third` variable ever updated from its starting value of negative infinity?)
- **If the answer is NO:** It means there were fewer than three distinct numbers in the list. The problem states that in this case, we must return the **maximum** number, which is stored in `first`.
- **If the answer is YES:** It means we successfully found a third distinct maximum, and we return the value stored in `third`.