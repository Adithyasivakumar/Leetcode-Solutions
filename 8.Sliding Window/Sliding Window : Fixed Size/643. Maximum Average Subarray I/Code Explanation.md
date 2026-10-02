# Problem Explanation

## 643. Maximum Average Subarray I

## Step 1: Understand the Problem

- **Input:** An integer array `nums` and an integer `k`.
- **Output:** A floating-point number representing the maximum average value of any contiguous subarray of size `k`.
- **Definition:** The average of a subarray is the total sum of its elements divided by `k`. You must scan all possible contiguous groups of size `k` to find the one that yields the highest average.
- **Goal:** Compute this maximum average efficiently using a single pass through the array, avoiding redundant calculations of overlapping elements.

## Step 2: Work Through Examples

- **Example 1:**
    - `nums` = `[1, 12, -5, -6, 50, 3]`, `k = 4`
    - Window 1: `[1, 12, -5, -6]` → Sum = 2 → Avg = 0.5
    - Window 2: `[12, -5, -6, 50]` → Sum = 51 → Avg = 12.75
    - Window 3: `[-5, -6, 50, 3]` → Sum = 42 → Avg = 10.5
    - **Output:** `12.75` (from the subarray `[12, -5, -6, 50]`)

## Step 3: Identify the Problem Type

- **Sliding Window (Fixed Size):** Exactly as you anticipated from the previous problem! Because the length of the subarray `k` never changes, you can slide a rigid window across the array.

## Step 4: Think About Approaches

- **Brute Force (O(N×K) Time):** Re-summing every block of `k` elements starting from every index and dividing by `k`.
    - *Critique:* Extremely slow and redundant.
- **Sliding Window (O(N) Time, O(1) Space):** This is your provided code.
    - Calculate the first window, slide it by subtracting the outgoing element and adding the incoming element, and track the maximum average along the way.
    - *Critique:* Structurally flawless. However, there is a micro-optimization involving floating-point math that interviewers love to point out (see Key Notes below!).

## Step 5: Plan Before Coding

- **Pseudocode:**

Plaintext

```
function findMaxAverage(nums, k):
// 1. Edge Case
if length of nums < k: return -1

// 2. Setup initial window
current_sum = sum of first k elements
max_avg = current_sum / k

// 3. Slide the window
for i from k to end of nums:
    update current_sum by adding incoming and subtracting outgoing
    current_avg = current_sum / k
    max_avg = maximum of (max_avg, current_avg)

return max_avg
```

## Step 6: Consider Edge Cases

- **Negative Maximums:** `nums = [-1, -3, -5, -2]`, `k = 2`. Your code perfectly handles negative values. It will correctly identify that `[-1, -3]` yields an average of `2.0`, which is mathematically greater than `4.0` or `3.5`.
- **N=K:** If the array is exactly size `k`, the `for` loop is entirely bypassed, and it safely returns the average of the only possible window.

## Step 7: Complexity Analysis

- **Time Complexity:** O(N). You sum the first K elements, then do a single pass over the remaining N−K elements. The math inside the loop is executed in strictly constant O(1) time.
- **Space Complexity:** O(1) auxiliary space. Only primitive variables (`current_sum`, `max_avg`) are tracked.

## Step 8: Review and Reflect

- **Application of Knowledge:** You perfectly applied the exact sliding window template from the previous problem to this one. Recognizing that "Maximum Sum" and "Maximum Average" are mechanically identical is exactly how you scale your algorithmic pattern recognition!

# Code Explanation

## The Analogy: The Grade Assessor

Imagine you are a teacher looking at a student's long row of test scores. You want to find their best consecutive streak of `k` tests.
You place a grading frame over the first `k` tests, add them up, and calculate the average.
Instead of lifting the frame to calculate the next set of tests from scratch, you just slide the frame one test to the right. You look at the old test score that slipped out of the frame and subtract it from your total. You look at the new test score that just entered the frame and add it. You calculate this new average and jot it down if it beats the previous best.

## Step 1: Initial Window Setup

Python

```
if len(nums) < k:
    return -1

current_sum = sum(nums[:k])
max_avg = current_sum / k
```

- **What it does:** Calculates the sum of the very first window of size `k` and sets the baseline `max_avg`.

## Step 2: The Sliding Loop

Python

```
for i in range(k, len(nums)):
    current_sum = current_sum + nums[i] - nums[i - k]
```

- **What it does:** Iterates through the rest of the array. It updates `current_sum` in O(1) time by adding the incoming element (`nums[i]`) and subtracting the outgoing element (`nums[i - k]`).

## Step 3: Tracking the Maximum

Python

```
    max_avg = max(max_avg, current_sum / k)

return max_avg
```

- **What it does:** Immediately divides the new `current_sum` by `k` to get the average, compares it against the highest average seen so far, and retains the winner.

# Analysis Summary (Deep Revision Framework)

- **The Core Idea:** Finding the maximum average of a fixed-size subarray is identical to finding the maximum sum. You can slide a fixed window across the array, updating the state in O(1) time per step by subtracting the outgoing element and adding the incoming element.
- **Data Structure Choice:** Primitive variables.
- **Algorithm Pattern:** Fixed-Size Sliding Window.
- **Complexity:**
    - **Time:** O(N)
    - **Space:** O(1)
- **Articulate the Solution:** "To find the maximum average subarray, I used a fixed-size sliding window. I computed the sum of the first `k` elements to establish a baseline. Then, I iterated through the rest of the array, updating the sum in constant time by subtracting the element leaving the window and adding the element entering it. By tracking the maximum average calculated at each step, I solved the problem in O(N) time."

## Spaced Repetition & Follow-ups

Here are the foundational problems to master **Dynamic Sliding Windows** (where the window size stretches and shrinks based on constraints):

1. **LeetCode 209. Minimum Size Subarray Sum:** Find the shortest contiguous subarray whose sum is ≥ target. (Hint: Expand the right side of the window to gain sum, shrink the left side to find the minimum length!).
2. **LeetCode 3. Longest Substring Without Repeating Characters:** The most famous string window problem. Expand until you hit a duplicate character, then shrink from the left until the duplicate is gone.
3. **LeetCode 1004. Max Consecutive Ones III:** You are given an array of 0s and 1s, and you can flip at most `k` 0s. What is the longest contiguous subarray of 1s?

# Key Notes

## The Floating-Point Division Optimization

Your code is logically perfect, but in systems programming and technical interviews, **floating-point division (`/`) is mathematically much slower than integer addition/subtraction.**

In your current loop, you are forcing the CPU to do a floating-point division `current_sum / k` on *every single iteration*.

**The Optimization:** Because `k` is a constant positive integer, the window with the **Maximum Sum** is mathematically guaranteed to also be the window with the **Maximum Average**. You do not need to calculate the average inside the loop at all! You can just track the maximum integer sum, and only divide by `k` exactly once at the very end.

Python

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        if len(nums) < k:
            return -1

        current_sum = sum(nums[:k])

        # Track the sum, not the average!
        max_sum = current_sum

        for i in range(k, len(nums)):
            current_sum = current_sum + nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)

        # Do the expensive floating-point division only ONCE at the end.
        return max_sum / k
```

This small change eliminates N−K division operations, making the code significantly faster at a hardware level while keeping the exact same O(N) time complexity!