# Problem Explanation

## 219. Contains Duplicate II

## Step 1: Understand the Problem

- **Input:** An integer array `nums` and an integer `k`.
- **Output:** A boolean (`True` or `False`).
- **Definition:** You are looking for any two elements in the array that have the exact same value, but their physical distance from each other (the difference in their indices) is less than or equal to `k`.
- **Goal:** Efficiently check for nearby duplicates without scanning backwards for `k` steps on every single element.

## Step 2: Work Through Examples

- **Example 1:**
    - `nums` = `[1, 2, 3, 1]`, `k = 3`
    - Index 0: `1`. Map: `{1: 0}`
    - Index 1: `2`. Map: `{1: 0, 2: 1}`
    - Index 2: `3`. Map: `{1: 0, 2: 1, 3: 2}`
    - Index 3: `1`. It's in the map! Previous index was `0`. Distance = `3 - 0 = 3`.
    - Is 3≤3? Yes!
    - **Output:** `True`
- **Example 2:**
    - `nums` = `[1, 2, 3, 1, 2, 3]`, `k = 2`
    - Index 3 (`1`): Previous was index 0. Distance = 3. Is 3≤2? No. Map updates to `{1: 3}`.
    - Index 4 (`2`): Previous was index 1. Distance = 3. Is 3≤2? No. Map updates to `{2: 4}`.
    - Index 5 (`3`): Previous was index 2. Distance = 3. Is 3≤2? No. Map updates to `{3: 5}`.
    - **Output:** `False`

## Step 3: Identify the Problem Type

- **Hash Map (State Tracking) / Fixed Sliding Window:** You need to remember the *most recent* location of every number. A Hash Map is perfect for mapping `value -> last_seen_index`.

## Step 4: Think About Approaches

- **Brute Force (O(N×K) Time):** For every element, use a nested loop to check the next `k` elements.
    - *Critique:* If N is 100,000 and K is 50,000, this will cause a Time Limit Exceeded (TLE) error.
- **Hash Map Tracking (O(N) Time, O(N) Space):** This is your provided code.
    - Store the most recent index of each number.
    - If you see the number again, instantly calculate the distance. If it's valid, return True.
    - If it's not valid, overwrite the old index with the new index.
    - *Critique:* Flawless, highly readable, and optimal logic.

## Step 5: Plan Before Coding

- **Pseudocode:**

Plaintext

```python
function containsNearbyDuplicate(nums, k):
// 1. Setup Hash Map
seen_map = empty dictionary

// 2. Iterate with indices
for index, num in nums:
    // 3. Check historical index
    if num is in seen_map:
        if index - seen_map[num] <= k:
            return True

    // 4. Record/Update latest index
    seen_map[num] = index

// 5. No valid pairs found
return False
```

## Step 6: Consider Edge Cases

- **Multiple Duplicates (`nums = [1, 0, 1, 1], k = 1`):**
    - At index 2 (`1`), the previous was index 0. Distance is 2. Target is 1. Fails.
    - **Crucial Step:** Your code executes `seen_map[num] = index`, updating the stored index for `1` to `2`.
    - At index 3 (`1`), the previous is now index 2. Distance is 1. Target is 1. Succeeds! Your map update logic handles this perfectly.
- **k=0:** If k=0, you are looking for an element that occupies the exact same index as itself, which is impossible for distinct indices. The distance `index - seen_map[num]` will always be >0, correctly returning `False`.

## Step 7: Complexity Analysis

- **Time Complexity:** O(N). You iterate over the array exactly once. Dictionary lookups (`in seen_map`) and insertions take amortized O(1) time.
- **Space Complexity:** O(N) auxiliary space. In the worst-case scenario (an array with no duplicates), every single element gets added to the Hash Map.

## Step 8: Review and Reflect

- **Pythonic Mastery:** Using `enumerate(nums)` instead of `for i in range(len(nums))` is exactly how senior Python engineers write loops. It is cleaner, faster, and prevents indexing errors.

# Code Explanation

## The Analogy: The Store Logbook

Imagine a small store that gives out a free prize if you visit twice within `k` days.
To track this, the cashier keeps a logbook (`seen_map`).
When you walk in (`num`), the cashier checks the book. If your name is in there, they look at the date of your last visit. If the difference between today (`index`) and your last visit is ≤k days, you win the prize (`return True`)!
If you visited too long ago, you don't get the prize. However, the cashier crosses out your old visit date and writes down *today's* date (`seen_map[num] = index`), because today is now your best chance to win the prize on a future visit!

## Step 1: The Hash Map

Python

```
seen_map = {}
for index, num in enumerate(nums):
```

- **What it does:** Initializes the dictionary to map values to their latest indices. `enumerate` unpacks both the physical location (`index`) and the value (`num`) simultaneously.

## Step 2: The Distance Check

Python

```
    if num in seen_map:
        if abs(seen_map[num] - index) <= k:
            return True
```

- **What it does:** If the number has been seen before, it calculates the distance.
    - *Note on `abs()`:* Because your loop processes left-to-right, `index` will mathematically *always* be larger than `seen_map[num]`. You can safely write this as `if index - seen_map[num] <= k:` to save a microsecond of compute time, though `abs()` reads very safely.

## Step 3: The State Update

Python

```
    seen_map[num] = index
return False
```

- **What it does:** This is the most important line of the code. Whether this is the first time seeing the number, or the second time seeing it but the distance was too far, it overwrites the map with the *newest* index. This ensures future identical numbers are compared against the closest possible match.

# Analysis Summary (Deep Revision Framework)

- **The Core Idea:** To find nearby duplicates, map each array value to its most recently seen index. When a duplicate is encountered, compute the distance between the current index and the stored index. If it is within the threshold K, return true. Otherwise, update the stored index to the current one.
- **Data Structure Choice:** Hash Map (Dictionary).
- **Algorithm Pattern:** State Tracking.
- **Complexity:**
    - **Time:** O(N)
    - **Space:** O(N)
- **Articulate the Solution:** "To solve Contains Duplicate II efficiently, I used a Hash Map to track the most recent index of every element. As I iterated through the array using `enumerate`, I checked if the current element was already in the map. If it was, and the difference between the current index and the mapped index was less than or equal to K, I returned True. If not, I updated the map with the current index to ensure future duplicates are compared against the most recent occurrence. This single-pass solution yields an O(N) time complexity."

This Hash Map approach is perfectly optimal for time, but there is an alternative approach using a HashSet that caps the Space Complexity to strictly O(K). Want to see how?

Hash Set (Sliding Window) Approach

Contains Duplicate III

# Key Notes

- **The Hash Set (Sliding Window) Variation:**
While your Hash Map solution is O(N) space, you can actually solve this using a fixed-size sliding window with a `set()`.
If you maintain a `set` that only ever holds `k` elements, you can just check if `num in window_set`. If the set size exceeds `k`, you just `remove(nums[i - k])`.Python

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for i, num in enumerate(nums):
            if num in window:
                return True

            window.add(num)

            # Maintain the sliding window size of k
            if len(window) > k:
                window.remove(nums[i - k])

        return False
```

This bounds the space complexity strictly to O(min(N,K)).