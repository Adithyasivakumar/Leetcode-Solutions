# Problem Explanation

## 11. Container With Most Water (Optimal Two Pointers)

## Step 1: Understand the Problem

- **Input:** An integer array `height` of length $N$, where each element represents the height of a vertical line drawn on a graph.
- **Output:** An integer representing the maximum amount of water a container can store.
- **Definition:** You must choose two lines to form the walls of a container. The width of the container is the distance between the two lines (their index difference). The height of the water is strictly limited by the **shorter** of the two lines. The volume (area) is simply $Width \times Height$.
- **Goal:** Find the two lines that together form a container capable of holding the absolute maximum area of water in $O(N)$ time.

## Step 2: Work Through Examples

- **Example 1:**
    - `height` = `[1, 8, 6, 2, 5, 4, 8, 3, 7]`
    - If we pick index 1 (height `8`) and index 8 (height `7`):
    - Width = $8 - 1 = 7$.
    - Limiting Height = $min(8, 7) = 7$.
    - Area = $7 \times 7 = 49$.
    - **Output:** `49`
- **Example 2:**
    - `height` = `[1, 1]`
    - Width = $1 - 0 = 1$.
    - Height = $min(1, 1) = 1$.
    - Area = $1 \times 1 = 1$.
    - **Output:** `1`

## Step 3: Identify the Problem Type

- **Two Pointers (Opposite Ends):** You are searching for an optimal pairing of two elements from across an array.
- **Greedy Search:** You want to maximize an area, so you start with the maximum possible width and greedily move inward, only discarding the shorter walls in hopes of finding taller ones.

## Step 4: Think About Approaches

- **Brute Force ($O(N^2)$ Time, $O(1)$ Space):** Check every single possible pair of lines in a nested loop, calculate the area for each pair, and keep the maximum.
    - *Critique:* Too slow. Will trigger a Time Limit Exceeded (TLE) error on LeetCode for arrays with $10^5$ elements.
- **Greedy Two Pointers ($O(N)$ Time, $O(1)$ Space):** This is your provided code.
    - Start with pointers at the absolute far left and far right ends.
    - Calculate the area and update your running maximum.
    - To find a potentially larger area, you *must* move one of the pointers inward. Moving the taller line inward cannot possibly increase the area (because the height is still bottlenecked by the shorter line, and the width just shrank). Therefore, you always step the pointer pointing to the **shorter** line inward.
    - *Critique:* This is the universally accepted optimal solution.

## Step 5: Plan Before Coding

- **Pseudocode (Your Approach):**

Plaintext

```
function maxArea(height):
// 1. Initialize boundary pointers and tracking variables
width = length of height - 1
left = 0
right = length of height - 1
max_water_stored = 0

// 2. Converge towards the center
while left < right:
    // 3. The shorter line dictates the water level
    if height[left] <= height[right]:
        current_area = height[left] * width
        max_water_stored = maximum of (max_water_stored, current_area)
        left += 1 // Discard the shorter left wall
    else:
        current_area = height[right] * width
        max_water_stored = maximum of (max_water_stored, current_area)
        right -= 1 // Discard the shorter right wall

    // 4. Shrink the width for the next iteration
    width -= 1

// 5. Return the highest recorded area
return max_water_stored
```

## Step 6: Consider Edge Cases

- **Identical Heights:** `[5, 5, 5, 5]`. If the walls are perfectly equal, it technically doesn't matter which one you move. Your `if height[left] <= height[right]:` handles this safely by defaulting to moving the left pointer.
- **Massive Drops:** `[1000, 1, 1, 1, 1000]`. The pointers start at the ends. They see the two `1000`s and immediately record the massive area. Any inward movement will shrink the area significantly, but the algorithm will safely evaluate them all and return the original massive area it recorded on step 1.

## Step 7: Complexity Analysis

- **Time Complexity:** $O(N)$. The two pointers traverse the array exactly once, meeting in the middle.
- **Space Complexity:** $O(1)$ auxiliary space. You only maintain four simple integer variables (`left`, `right`, `width`, `max_water_stored`).

## Step 8: Review and Reflect

- **Your "Cleaner Version" Micro-Optimization:** Most standard solutions to this problem calculate the width directly inside the loop every single time using `(right - left)`. By explicitly tracking `width` outside the loop and doing `width -= 1` at the end of each cycle, you saved the CPU from performing a subtraction operation on every single iteration. This is a very clean, low-level optimization!

# Code Explanation

## The Analogy: The Pool Builders

Imagine two architects trying to design the largest possible rectangular swimming pool. They have a blueprint with a bunch of vertical support beams of varying heights (`height`).

They start by placing their walls as far apart as physically possible (`left = 0`, `right = len(height)-1`) to maximize the width.

They calculate the volume of the pool. However, water will spill out over the top of the shorter wall, so the depth of the pool is strictly limited by the smaller support beam.

To try and build a bigger pool, they have to move one of the walls closer to the center.

If they move the taller wall inward, the pool gets narrower, but the depth is *still* limited by the shorter wall. The pool is guaranteed to hold less water!

Therefore, the only logical choice is to abandon the shorter wall (`left += 1` or `right -= 1`) and move it inward, hoping to strike a massive, taller support beam that makes up for the loss in width!

## Step 1: Initialization

Python

```
width = len(height)-1
left, right = 0, len(height)-1
max_water_stored = 0
```

- **What it does:** Sets the pointers to the extreme opposite ends of the array. Initializes the active `width` of the container and sets the overall record tracker to zero.

## Step 2: The Evaluation Loop

Python

```
while left < right:
```

- **What it does:** Ensures the pointers continue evaluating containers until they physically bump into each other (at which point a container can no longer be formed).

## Step 3: Resolving the Left Bottleneck

Python

```
    if height[left] <= height[right]:
        max_water_stored = max(max_water_stored, height[left] * width)
        left += 1
```

- **What it does:** If the left wall is the bottleneck (shorter), it dictates the height. It calculates the area `height[left] * width`, checks if it breaks the all-time high score using `max()`, and then steps the left pointer inward to discard the weak wall.

## Step 4: Resolving the Right Bottleneck

Python

```
    else:
        max_water_stored = max(max_water_stored, height[right] * width)
        right -= 1
```

- **What it does:** If the right wall is the bottleneck, it mirrors the logic. It calculates the area using `height[right]`, updates the record, and steps the right pointer inward.

## Step 5: Width Maintenance

Python

```
    width -= 1
```

- **What it does:** Because one pointer *always* moved exactly one step inward during this cycle, the overall width of our container has shrunk by exactly 1 unit. This readies the variable for the next loop.

# Analysis Summary (Deep Revision Framework)

- **The Core Idea:** We maximize the rectangular area by starting with the widest possible container and greedily moving the pointer pointing to the shorter boundary inward, seeking a taller boundary to compensate for the decreasing width.
- **Data Structure Choice:** Array with Two Pointers.
- **Algorithm Pattern:** Two Pointers (Opposite Ends) / Greedy Area Maximization.
- **Complexity:**
    - **Time:** $O(N)$.
    - **Space:** $O(1)$.
- **Articulate the Solution:** "To find the container with the most water, I used a two-pointer approach starting at opposite ends of the array to maximize the initial width. In a loop, I calculated the area using the shorter of the two lines multiplied by the current width, updating the maximum area recorded. To optimize, I continually advanced the pointer situated at the shorter line inward, as moving the taller line would strictly decrease the area. I manually decremented a tracked `width` variable to avoid redundant subtraction, executing the entire search in $O(N)$ time and $O(1)$ space."

## Spaced Repetition & Follow-ups:

- **LeetCode 42. Trapping Rain Water:** You just conquered this! Notice how both use converging Two Pointers, but *Container With Most Water* looks for a single global maximum rectangle, whereas *Trapping Rain Water* adds up all the micro-valleys.
- **LeetCode 167. Two Sum II - Input Array Is Sorted:** Re-familiarize yourself with the Two Pointer pattern used to find a target sum instead of an area.