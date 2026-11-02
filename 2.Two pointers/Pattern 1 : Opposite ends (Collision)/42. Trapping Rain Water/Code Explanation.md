# Problem Explanation

## 42. Trapping Rain Water

## Step 1: Understand the Problem

- **Input:** An array of non-negative integers `height` representing an elevation map where the width of each bar is 1.
- **Output:** An integer representing the total units of rainwater trapped after raining.
- **Definition:** Water can only be trapped above a specific block if there are taller blocks to both its left and its right. The amount of water trapped above any single block is determined by the shortest of those two bounding walls, minus the height of the block itself.
- **Goal:** Calculate the trapped water efficiently. You provided two excellent solutions showing the evolution from O(N) space to the ultimate O(1) space mastery.

## Step 2: Work Through Examples

- **Example 1:**
    - `height` = `[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]`
    - Block at index 2 (height `0`): Left max is `1`, right max is `3`. Min wall is `1`. Water = `1 - 0 = 1`.
    - Block at index 5 (height `0`): Left max is `2`, right max is `3`. Min wall is `2`. Water = `2 - 0 = 2`.
    - **Output:** `6` total units.
- **Example 2:**
    - `height` = `[4, 2, 0, 3, 2, 5]`
    - Water traps in the valleys between the peaks.
    - **Output:** `9` total units.

## Step 3: Identify the Problem Type

- **Array Traversal & Bounding:** Calculating local capacities based on global extreme values.
- **Prefix/Suffix Arrays (Dynamic Programming):** Pre-calculating boundaries to avoid repeated work.
- **Two Pointers:** Optimizing spatial complexity by calculating boundaries on the fly from the outside in.

## Step 4: Think About Approaches

- **Brute Force (O(N2) Time, O(1) Space):** For every single block, scan all the way to the left to find the max, then all the way to the right to find the max.
    - *Critique:* Guaranteed Time Limit Exceeded (TLE) on large arrays.
- **Pre-computation / Prefix & Suffix Arrays (O(N) Time, O(N) Space):** This is your first provided solution.
    - Iterate left-to-right to build an array of the highest walls seen so far. Iterate right-to-left to build a second array of highest walls from the right.
    - *Critique:* This mathematically guarantees the correct answer by caching the brute force searches. It is structurally perfect but uses extra memory.
- **Two Pointers (O(N) Time, O(1) Space):** This is your second provided solution.
    - Use two pointers starting at the ends. Track the maximums dynamically. Move the pointer that sits under the smaller maximum.
    - *Critique:* The pinnacle of array optimization. It eliminates the auxiliary arrays entirely.

## Step 5: Plan Before Coding

- **Pseudocode (Two Pointers):**

Plaintext

```
function trap(height):
// 1. Initialize boundary pointers and local maximums
left = 0, right = length - 1
max_left = height[left], max_right = height[right]
water_trapped = 0

// 2. Converge towards the highest peak
while left < right:
    // 3. The smaller wall dictates the water level
    if max_left < max_right:
        water_trapped += max_left - height[left]
        left += 1
        max_left = max(max_left, height[left])
    else:
        water_trapped += max_right - height[right]
        right -= 1
        max_right = max(max_right, height[right])

// 4. Return total
return water_trapped
```

## Step 6: Consider Edge Cases

- **Flat Ground / No Valleys:** `[0, 0, 0]` or `[1, 2, 3]`. The maximums update, but the `max - height` calculation always results in `0`. No false water is added. Correct.
- **Pyramid Shape:** `[1, 3, 5, 3, 1]`. The pointers climb up to the peak (5). Since the current height equals the running max at every step, water added is `0`. Correct.

## Step 7: Complexity Analysis

- **Time Complexity:** O(N). The two pointers traverse the array exactly once, meeting in the middle or at the highest peak.
- **Space Complexity:** O(1) auxiliary space. Only scalar variables (`left`, `right`, `max_left`, `max_right`, `water_trapped`) are used, discarding the need for the `max_left` and `max_right` lists from the first approach.

## Step 8: Review and Reflect

- **The "Aha!" Moment:** Why does the Two Pointer approach work without knowing the *entire* other side? The formula for water is `min(max_left, max_right) - height`. If `max_left < max_right`, we already know the `min` is `max_left`. It doesn't matter if there's an even bigger wall hiding further to the right; `max_left` is the bottleneck! By always processing the side with the smaller bottleneck, we guarantee absolute mathematical accuracy.

# Code Explanation

## The Analogy: The Two Canyon Inspectors

Imagine two inspectors standing at the far ends of a mountain range. Inspector Left walks rightward, and Inspector Right walks leftward. They want to measure deep puddles.
Inspector Left shouts, "The tallest mountain I've seen so far is 40 feet!"
Inspector Right shouts back, "The tallest I've seen is 100 feet!"
Because Inspector Left's mountain is shorter, Inspector Left knows with 100% certainty that any valley they are currently standing in can only hold water up to 40 feet. It doesn't matter if there's a 200-foot mountain behind Inspector Right; the 40-foot mountain on the left is the spillway.
Inspector Left calculates the puddle at their feet, takes a step forward, updates their personal tallest mountain record, and shouts out the new number. They take turns moving based entirely on whoever is reporting the shorter maximum mountain!

## Step 1: The Starting Positions

Python

```
left, right = 0, len(height) - 1
max_left, max_right = height[left], height[right]
water_trapped = 0
```

- **What it does:** Sets the inspectors at index 0 and the final index. Initializes their personal "tallest wall seen" records to the height of the blocks they are currently standing on.

## Step 2: The Convergence Loop

Python

```
while left < right:
```

- **What it does:** The loop continues until the two inspectors bump into each other. They will always meet at the absolute highest peak in the entire array.

## Step 3: Processing the Left Bottleneck

Python

```
    if max_left < max_right:
        water_trapped += max_left - height[left]
        left += 1
        max_left = max(max_left, height[left])
```

- **What it does:** If the left side has the shorter limiting wall, we process the left pointer.
    1. We calculate trapped water: `max_left - height[left]`. (If the current block is the tallest we've seen, this evaluates to `0`, preventing negative water).
    2. We step the pointer inward.
    3. We update `max_left` to see if this new block is our new tallest left wall.
    *(Note: Updating `max_left` after calculating the water is safe because your initial setup logged the height of the first block).*

## Step 4: Processing the Right Bottleneck

Python

```
    else:
        water_trapped += max_right - height[right]
        right -= 1
        max_right = max(max_right, height[right])
```

- **What it does:** If the right side has the shorter (or equal) limiting wall, we mirror the logic. We calculate the water held by the right bottleneck, step inward, and update the right maximum.

# Analysis Summary (Deep Revision Framework)

- **The Core Idea:** Water trapped above any block is limited by the shorter of its highest left and right boundaries. By using two pointers converging from the outside in, we can dynamically track these boundaries and calculate the trapped water on the fly, always advancing the pointer associated with the shorter boundary.
- **Data Structure Choice:** Array with Two Pointers.
- **Algorithm Pattern:** Two Pointers (Opposite Ends) / Bottleneck Resolution.
- **Complexity:**
    - **Time:** O(N).
    - **Space:** O(1).
- **Articulate the Solution:** "To optimize Trapping Rain Water to O(1) space, I implemented a two-pointer approach from the outside in. I maintained a `max_left` and `max_right` variable. At each step, I compared these two maximums. Because the trapped water is determined by the minimum of the two boundaries, I calculated the trapped water for the pointer with the smaller maximum, advanced that pointer inward, and updated its respective maximum. This dynamically calculates the volumes in O(N) time without pre-computing suffix arrays."

## Spaced Repetition & Follow-ups:

- **LeetCode 11. Container With Most Water:** A very similar Two Pointer problem, but instead of adding up all the water in the valleys, you just want to find the single largest rectangular container. (You also solve it by moving the pointer of the shorter wall!).
- **LeetCode 407. Trapping Rain Water II:** The terrifying 3D version of this problem. Instead of a 2D slice, you are given a 3D grid. (Hint: You can't use simple Two Pointers here; you must use a Min-Heap/Priority Queue to process the lowest boundaries first!).

# Key Notes

- **Evolution of a Programmer:** Providing both solutions in an interview setting is a massive flex. You walk the interviewer through the O(N) space Dynamic Programming solution first to prove you deeply understand the `min(left, right) - height` formula. Then, you say, *"We can actually optimize this space away..."* and deploy the Two Pointer solution. It shows a complete command of algorithmic evolution.