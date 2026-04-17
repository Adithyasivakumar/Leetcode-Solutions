# Problem Explanation

## 1299. Replace Elements with Greatest Element on Right Side

## Step 1: Understand the Problem

- **Input:** An array of integers `arr`.
- **Output:** The same (or a new) array where every element is replaced by the largest element mathematically existing to its right. The very last element is always replaced with `1` since there is nothing to its right.
- **Definition:** For any index `i`, we must look at the subarray `arr[i+1 : end]`, find the highest number, and put it at index `i`.
- **Goal:** Do this efficiently. A naive approach would repeatedly scan the rest of the array for every single element, which is far too slow for large inputs.

## Step 2: Work Through Examples

- **Example 1:**
    - `arr` = `[17, 18, 5, 4, 6, 1]`
    - Index 0 (17): Max to the right `[18, 5, 4, 6, 1]` is **18**.
    - Index 1 (18): Max to the right `[5, 4, 6, 1]` is **6**.
    - Index 2 (5): Max to the right `[4, 6, 1]` is **6**.
    - Index 3 (4): Max to the right `[6, 1]` is **6**.
    - Index 4 (6): Max to the right `[1]` is **1**.
    - Index 5 (1): Nothing to the right, so **1**.
    - **Output:** `[18, 6, 6, 6, 1, -1]`
- **Example 2:**
    - `arr` = `[400]`
    - The last (and only) element gets replaced with `1`.
    - **Output:** `[-1]`

## Step 3: Identify the Problem Type

- **Array Traversal (Reverse Order):** The most crucial realization here is that scanning left-to-right is incredibly inefficient. Scanning *right-to-left* allows us to keep a running track of the maximum value we've seen so far.
- **Greedy / Running Maximum:** Maintaining a single variable to track the highest value encountered during a single pass.

## Step 4: Think About Approaches

- **Brute Force (O(N2) Time, O(1) Space):** For every element, run an inner loop to check every element to its right.
    - *Critique:* If the array has 10,000 elements, this takes 100,000,000 operations. It will trigger a "Time Limit Exceeded" error.
- **Reverse Array Building (O(N) Time, O(N) Space):** This is your provided code.
    - Start from the back. Track the highest number seen so far. Append it to a new array. Since appending backward builds the array in reverse, flip the whole array at the end.
    - *Critique:* Highly logical and achieves the required linear time complexity.
- **In-Place Reverse Traversal (O(N) Time, O(1) Space):** The ultimate optimal way.
    - Instead of building a new array, overwrite the original `arr` array as you walk backward, using a temporary variable to help facilitate the swap. (More on this in the Key Notes!)

## Step 5: Plan Before Coding

- **Pseudocode (Based on your logic):**

Plaintext

`function replaceElements(arr):
// 1. Prepare the results bucket and the base requirement
longest = []
maximum_from_right = -1
longest.append(maximum_from_right)

// 2. Walk the array backwards (from last element to first)
for i from len(arr)-1 down to 0:
    
    // 3. Compare current element to our running maximum
    if arr[i] >= maximum_from_right:
        longest.append(arr[i])
        maximum_from_right = arr[i]
    else:
        longest.append(maximum_from_right)

// 4. Flip the bucket right-side up
longest.reverse()

// 5. Chop off the extra starting element and return
return longest[1:]`

## Step 6: Consider Edge Cases

- **Single Element Array:** `arr = [400]`. Loop runs once. `400 >= -1`, so it appends `400` and updates max. `longest` is now `[-1, 400]`. Reversing makes it `[400, -1]`. Slicing `[1:]` returns `[-1]`. Perfect!
- **All Increasing Numbers:** `[1, 2, 3, 4]`. The running maximum constantly updates. Output correctly becomes `[4, 4, 4, -1]`. Correct.

## Step 7: Complexity Analysis

- **Time Complexity:** O(N). The `for` loop iterates backward exactly N times. Reversing the list takes O(N) time. Slicing the list takes O(N) time. Dropping the constants, the overall time is linear O(N).
- **Space Complexity:** O(N). You create a brand new list (`longest`) which stores N+1 integers.

## Step 8: Review and Reflect

- **The "Shift" Explanation:** Why did you have to return `longest[1:]`? Because on the very first iteration of your loop, you compare the last element (e.g., `1`) to `1`. Since `1 >= -1`, you append `1` to `longest` *and then* update the max to `1`. This means your `longest` array successfully logs the maximums, but it's shifted over by one index (it tracks the max *including* the current element, rather than strictly to the right). Slicing the list perfectly corrects this offset!

---

# Code Explanation

## The Analogy: The King of the Hill

Imagine walking backward up a mountain trail, starting from the very end.
At the end of the trail, the "tallest mountain to your right" is nothing (represented by `-1`).
As you take a step backward, you look at the mountain you are standing on. Is it taller than the tallest mountain you've seen so far?
If it is, you write down its height, and that becomes your new "Tallest Mountain."
If it isn't, you just write down the height of the old "Tallest Mountain."
Because you walked backward, your list of mountain heights is written backward. You flip the notebook over (`.reverse()`) to read it from start to finish!

## Step 1: Initializing the Tracker

Python

`longest = []
maximum_from_right = -1
longest.append(maximum_from_right)`

- **What it does:** Sets up an empty list to track the answers. Crucially, it seeds the list with `1`, which fulfills the problem's strict rule that the final space to the right is always `1`.

## Step 2: The Reverse Walk

Python

`n = len(arr)
for i in range(n-1, -1, -1):`

- **What it does:** Uses Python's `range()` function to step backward. It starts at the last index (`n-1`), stops before `1` (meaning it includes `0`), and takes a step of `1` (moving in reverse).

## Step 3: Updating the Ledger

Python

    `if arr[i] >= maximum_from_right:
        longest.append(arr[i])
        maximum_from_right = arr[i]
        
    elif arr[i] <= maximum_from_right:
        longest.append(maximum_from_right)`

- **What it does:** The core logic. If the current number is bigger than our running max, we append the new number to our ledger and update the "King of the Hill." If it is smaller, we simply append the reigning "King of the Hill" to the ledger.

## Step 4: Correcting the Order

Python

`longest.reverse()
return longest[1:]`

- **What it does:** Because we walked backward, our answers are backward. `.reverse()` flips the array right-side up. Because our logic appended the current element's max *including* itself, the array is one element too long. Slicing `[1:]` chops off the unwanted first element, perfectly aligning the answers.

---

# Analysis Summary (Deep Revision Framework)

- **The Core Idea:** We solve the problem in O(N) time by traversing the array from right to left, keeping track of the running maximum value, and appending it to a new array that we eventually reverse.
- **Data Structure Choice:** Array/List (for dynamic appending).
- **Algorithm Pattern:** Reverse Linear Traversal & Greedy Max Tracking.
- **Complexity:**
    - **Time:** O(N).
    - **Space:** O(N).
- **Articulate the Solution:** "To avoid an O(N2) nested loop, I iterated through the array in reverse. I maintained a variable to track the maximum value seen so far, initially set to -1. At each step, I compared the current element to my running maximum, appending the greater value to a result array, and updating the running maximum if necessary. Finally, I reversed the result array and sliced off the initial offset to return the correct sequence."

## Spaced Repetition & Follow-ups:

- **LeetCode 238. Product of Array Except Self:** Another classic array problem where calculating prefix and suffix values in forward and reverse passes is the key to an O(N) solution.
- **LeetCode 739. Daily Temperatures:** A slightly harder variation where you must look to the right to find the *distance* to the next greater element (requires a Monotonic Stack).

---

# Key Notes

- **The O(1) Space Optimization:** In an interview, once you explain your logic, the interviewer will ask: *"Can you do this without creating the `longest` array?"* You can! You do it by modifying the input array **in-place**. Here is how you write that:Python
    
    `def replaceElements(self, arr: List[int]) -> List[int]:
        max_so_far = -1
    
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]          # Save the current value
            arr[i] = max_so_far    # Overwrite the current value with the max to its right
            max_so_far = max(max_so_far, temp) # Update the running max
    
        return arr`
    
    This is shorter, uses exactly O(1) auxiliary memory, and avoids the need to `.reverse()` or slice! Memorize this `temp` variable trick.