# Problem Explanation

## 16. 3Sum Closest

## Step 1: Understand the Problem

- **Input:** An integer array `nums` and an integer `target`.
- **Output:** The sum of the three integers in `nums` that is closest to `target`.
- **Definition:** You need to pick exactly three distinct elements that, when added together, have the smallest absolute mathematical difference from the target number.
- **Goal:** Avoid the $O(N^3)$ brute-force trap of checking every possible triplet. Sort the array to unlock the directional two-pointer technique.

## Step 2: Work Through Examples

- **Example 1:**
- `nums` = `[-1, 2, 1, -4]`, `target = 1`
- *Sort:* `[-4, -1, 1, 2]`
- *Anchor `i = 0` (-4):* `l = 1` (-1), `r = 3` (2). Sum = `4 + -1 + 2 = -3`. Distance to 1 is 4. Closest is `3`.
- *Too small (-3 < 1):* Move `l` up. `l = 2` (1). Sum = `4 + 1 + 2 = -1`. Distance to 1 is 2. Closest updates to `1`.
- *Anchor `i = 1` (-1):* `l = 2` (1), `r = 3` (2). Sum = `1 + 1 + 2 = 2`. Distance to 1 is 1. Closest updates to `2`.
- **Output:** `2`

## Step 3: Identify the Problem Type

- **Sorting + Two Pointers (Opposite Ends):** Any time a problem asks for combinations of numbers (pairs, triplets) that meet a sum condition, and you do not need to return the original indices, sorting the array is the immediate first step.

## Step 4: Think About Approaches

- **Brute Force ($O(N^3)$ Time):** Three nested loops checking every combination.
- *Critique:* Guaranteed Time Limit Exceeded.
- **Sorting + Two Pointers ($O(N^2)$ Time, $O(1)$ Space):** This is your provided code.
- Lock one number in place. Use two pointers on the remaining array to aggressively hunt for the best complement to reach the target.
- *Critique:* Flawless. You included the duplicate-skipping optimization and the early exit condition, making this a production-grade FAANG solution.

## Step 5: Plan Before Coding

- **Pseudocode:**

```
function threeSumClosest(nums, target):
// 1. Setup
sort(nums)
closest = infinity

// 2. Lock the first number
for i from 0 to length of nums:
    // Skip duplicate anchors to save time
    if i > 0 and nums[i] == nums[i-1]: continue

    // 3. Hunt with Two Pointers
    l = i + 1
    r = length of nums - 1

    while l < r:
        current_sum = nums[i] + nums[l] + nums[r]

        // 4. Update closest
        if distance(current_sum, target) < distance(closest, target):
            closest = current_sum

        // 5. Shift pointers
        if current_sum == target: return current_sum
        if current_sum > target: r -= 1
        else: l += 1

return closest
```

## Step 6: Consider Edge Cases

- **Exact Match Found:** If `current_sum == target`, your code immediately returns. It is mathematically impossible to get a difference smaller than 0, so this saves unnecessary loop cycles.
- **Array size is exactly 3:** The outer loop locks `i=0`, `l=1`, `r=2`. It calculates the sum, updates `closest`, the `while` loop terminates, and it returns the only possible sum.

## Step 7: Complexity Analysis

- **Time Complexity:** $O(N^2)$. Sorting takes $O(N \log N)$ time. The outer loop runs $N$ times, and the inner `while` loop runs at most $N$ times. $N \times N = O(N^2)$, which swallows the sorting time.
- **Space Complexity:** $O(1)$ or $O(\log N)$ depending on the language's sorting algorithm (Python's Timsort uses $O(N)$ space under the hood, but algorithmically we consider the extra space $O(1)$).

## Step 8: Review and Reflect

- **Duplicate Skipping Insight:** Your inclusion of `if i != 0 and nums[i] == nums[i-1]: continue` is excellent. While it is strictly required in standard *3Sum* to prevent duplicate triplets in the output, it acts as a massive performance optimization here in *3Sum Closest* by preventing the algorithm from re-evaluating identical anchors.

---

# Code Explanation

## The Analogy: The Temperature Dials

Imagine you are trying to mix hot and cold water to reach an exact target temperature.
First, you set the baseline temperature dial (`i`).
Then, you put your left hand on the Cold dial (`l`) and your right hand on the Hot dial (`r`).
You check the water. If the water is too hot (`current_sum > target`), you turn down the Hot dial (`r -= 1`).
If the water is too cold (`current_sum < target`), you turn up the Cold dial (`l += 1`).
Every time you adjust a dial, you check if this is the closest you've gotten to the perfect temperature so far. If you hit the exact temperature, you stop mixing immediately.

## Step 1: The Distance Check

```python
if abs(current_sum - target) < abs(closest - target):
    closest = current_sum
```

- **What it does:** Uses absolute values to measure the mathematical distance between the current triplet sum and the target. Initializing `closest = float('inf')` guarantees the very first triplet will overwrite it.

## Step 2: The Directional Shift

```python
if current_sum == target:
    return current_sum
elif current_sum > target:
    r -= 1
else:
    l += 1
```

- **What it does:** Dictates the pointer movement. Because the array is sorted, moving `r` left *guarantees* the sum will decrease. Moving `l` right *guarantees* the sum will increase. This logical certainty is what allows you to skip evaluating every single combination.

---

# Analysis Summary (Deep Revision Framework)

- **The Core Idea:** To find the closest sum of three numbers, sort the array first. Lock one number, then use two opposite-end pointers on the remaining array to dynamically close the gap toward the target. Update the closest sum whenever the absolute difference shrinks.
- **Data Structure Choice:** Sorted Array.
- **Algorithm Pattern:** Two Pointers (Opposite Ends).
- **Complexity:**
- **Time:** $O(N^2)$
- **Space:** $O(1)$ auxiliary.
- **Articulate the Solution:** "To optimize 3Sum Closest, I first sorted the array to enable a directional two-pointer approach. I iterated through the array, locking one element as an anchor and skipping duplicate anchors for efficiency. For the remaining subarray, I placed pointers at the start and end. I calculated the sum and updated my closest tracking variable if the current absolute difference to the target was smaller. Depending on whether the sum was too large or too small, I shifted the right or left pointer inward, achieving an optimal $O(N^2)$ solution."

---

# Key Notes

## 3Sum vs. 3Sum Closest

You have successfully implemented the logic for 3Sum Closest. However, the standard **15. 3Sum** (where target = 0) is actually slightly harder.

In standard 3Sum, you must return *all unique triplets*. This means if you find a valid triplet, you cannot just return it—you must save it, and then **skip duplicates for both the `l` and `r` pointers** to avoid returning identical arrays.