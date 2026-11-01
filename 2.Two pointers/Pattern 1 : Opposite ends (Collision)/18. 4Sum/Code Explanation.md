# Problem Explanation

## 18. 4Sum

## Step 1: Understand the Problem

- **Input:** An integer array `nums` and an integer `target`.
- **Output:** A list of all unique quadruplets `[nums[i], nums[j], nums[l], nums[r]]` that sum perfectly to `target`.
- **Definition:** You are expanding the 3Sum architecture. Instead of finding three numbers, you must find four. Crucially, the solution set must not contain duplicate quadruplets.
- **Goal:** Avoid the catastrophic $O(N^4)$ brute-force runtime. Sort the array, lock down *two* anchors, and use opposite-end pointers on the remaining subarray to hunt for the final two components.

## Step 2: Work Through Examples

- **Example 1:**
- `nums` = `[1, 0, -1, 0, -2, 2]`, `target = 0`
- *Sort:* `[-2, -1, 0, 0, 1, 2]`
- *Anchor `i = 0` (-2):*
- *Anchor `j = 1` (-1):* `l = 2` (0), `r = 5` (2). Sum = -2 + -1 + 0 + 2 = -1 (Too small). `l` moves up.
- `l = 3` (0), `r = 5` (2). Sum = 0. Match! Add `[-2, -1, 0, 2]`. Move `l` and `r`.
- *Anchor `j = 2` (0):* `l = 3` (0), `r = 5` (2). Sum = 0. Match! Add `[-2, 0, 0, 2]`.
- *Anchor `i = 1` (-1):*
- *Anchor `j = 2` (0):* `l = 3` (0), `r = 4` (1). Sum = 0. Match! Add `[-1, 0, 0, 1]`.
- **Output:** `[[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]` (Order of triplets doesn't matter).

## Step 3: Identify the Problem Type

- **Sorting + Two Pointers (K-Sum Extension):** Whenever a problem asks for combinations of $K$ elements summing to a target, you sort the array, use $K-2$ nested loops to lock down anchors, and use a 2-pointer sweep for the final two elements.

## Step 4: Think About Approaches

- **Brute Force ($O(N^4)$ Time):** Four nested loops checking every single quadruplet combination.
- *Critique:* Massive Time Limit Exceeded (TLE).
- **Sorting + Two Anchors + Two Pointers ($O(N^3)$ Time, $O(1)$ Space):** This is your provided code.
- Sort the array. Loop `i` to lock the first number. Loop `j` to lock the second number. Use `l` and `r` to find the remaining sum.
- *Critique:* Absolutely flawless. You successfully scaled the 3Sum logic up a dimension, and you perfectly nailed the most difficult edge case: skipping duplicates for the nested `j` anchor.

## Step 5: Plan Before Coding

- **Pseudocode:**

```
function fourSum(nums, target):
// 1. Setup
sort(nums)
res = empty list

// 2. First Anchor
for i from 0 to length - 3:
    // Skip duplicate i
    if i > 0 and nums[i] == nums[i-1]: continue

    // 3. Second Anchor
    for j from i + 1 to length - 2:
        // Skip duplicate j
        if j > i + 1 and nums[j] == nums[j-1]: continue

        // 4. Two Pointer Hunt
        l = j + 1
        r = length - 1

        while l < r:
            calculate current_sum
            if current_sum > target: r -= 1
            else if current_sum < target: l += 1
            else:
                append quadruplet to res
                move l and r inward
                skip duplicates for l
                skip duplicates for r

return res
```

## Step 6: Consider Edge Cases

- **Array too small:** `nums = [1, 2, 3]`. The `for` loops still operate safely. `j` loop won't have enough space to establish `l < r`, preventing errors. The function returns `[]`.
- **Identical elements:** `nums = [2, 2, 2, 2, 2]`, `target = 8`.
- `i=0` (2), `j=1` (2), `l=2` (2), `r=4` (2). Match found! Adds `[2, 2, 2, 2]`.
- `l` and `r` skip duplicates and cross.
- `j` increments to `2`, but `j != i + 1` activates, skipping the duplicate anchor.
- `i` increments to `1`, `i != 0` activates, skipping the duplicate anchor.
- Returns strictly `[[2, 2, 2, 2]]`. Handled perfectly.

## Step 7: Complexity Analysis

- **Time Complexity:** $O(N^3)$. Sorting takes $O(N \log N)$. The `i` loop runs $N$ times. The `j` loop runs $N$ times. The `l` and `r` pointers traverse the remainder of the array once per `j` loop, taking $O(N)$ time. Total mathematical bounds: $O(N \times N \times N) = O(N^3)$.
- **Space Complexity:** $O(1)$ auxiliary space (or $O(N)$ depending on the underlying sorting algorithm), excluding the output array `res`.

## Step 8: Review and Reflect

- **The Duplicate Skipping Trap:** The most common failure point for FAANG candidates on 4Sum is writing `if j != 0 and nums[j] == nums[j-1]: continue`. That breaks the code because `j` can never be `0`. You correctly wrote `if j != i + 1 ...`, ensuring that `j` is allowed to process the very first element of its *own* specific sub-array, but skips subsequent duplicates. This proves a deep, structural understanding of array indexing.

---

# Code Explanation

## The Analogy: The Four-Dial Safe

Imagine a safe with four combination dials. You know the exact mathematical target the dials must sum to.
Checking every combination is too slow. Because the numbers are sorted, you logically lock the first dial (`i`). Then, you lock the second dial (`j`).
With two dials locked, you only have two dials left (`l` and `r`). You can now use your hot-and-cold strategy: if the sum is too high, you turn the right dial down. If the sum is too low, you turn the left dial up.
Whenever you find a valid combination, you write it down. To avoid writing down the exact same combination again, you fast-forward any dials that are sitting on identical duplicate numbers.

## Step 1: The Outer Anchors and Bounds

```python
if i != 0 and nums[i] == nums[i-1]:
    continue
```

- **What it does:** Locks the first element of the quadruplet. By skipping elements identical to the previous one, it prevents generating the exact same search space twice, which is a massive time-saver and guarantees unique output.

## Step 2: The Nested Anchor

```python
if j != i + 1 and nums[j] == nums[j-1]:
    continue
```

- **What it does:** Locks the second element. The logic `j != i + 1` is paramount. If `nums = [2, 2, 2, 2]`, when `i = 0`, `j` starts at `1`. You *need* `nums[0]` and `nums[1]` to both be `2` to reach the target of `8`. The `i + 1` check protects the first usage of `2` for the `j` pointer, while aggressively skipping the 3rd and 4th `2`s.

## Step 3: The 2-Pointer Hunt & Deduplication

```python
else:
    res.append([nums[i], nums[j], nums[l], nums[r]])
    l += 1
    r -= 1

    while l < r and nums[l] == nums[l-1]:
        l += 1
    while l < r and nums[r] == nums[r+1]:
        r -= 1
```

- **What it does:** When a perfect match is found, it logs it. It physically moves both pointers inward (since neither pointer can form a new unique match using the same number). It then uses inner `while` loops to physically step over any adjacent duplicate values, ensuring the next iteration tests a brand new combination.

---

# Analysis Summary (Deep Revision Framework)

- **The Core Idea:** To find unique quadruplets summing to a target, sort the array and iterate with two nested loops to establish two anchors. Use two pointers on the remaining elements to find pairs that complete the target sum. Skip duplicates at all four pointer levels (`i`, `j`, `l`, `r`) to guarantee uniqueness.
- **Data Structure Choice:** Sorted Array.
- **Algorithm Pattern:** Two Pointers (K-Sum / Opposite Ends).
- **Complexity:**
- **Time:** $O(N^3)$
- **Space:** $O(1)$ auxiliary.
- **Articulate the Solution:** "To solve 4Sum, I extended the 3Sum algorithm by adding a second anchor. After sorting the array, I used two nested loops to lock the first two numbers, skipping duplicates for both to ensure unique combinations. For the remaining subarray, I used two opposite-end pointers to hunt for the final two numbers. When the sum was too high, I shifted the right pointer; when too low, the left pointer. Upon finding a valid quadruplet, I recorded it and advanced both pointers, using inner while loops to skip consecutive duplicates, resulting in an optimal $O(N^3)$ solution."

---

# Key Notes

## Generalized K-Sum (The Recursive Template)

You have now written Two Sum II ($O(N)$), 3Sum ($O(N^2)$), and 4Sum ($O(N^3)$). What if an interviewer asks you to write **5Sum**, or even a generic **K-Sum** function?

Instead of writing $K-2$ nested `for` loops, you can write a highly elegant recursive function that breaks *any* K-Sum down into the base case of Two Sum!

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []

            # Edge case bounds
            if not nums or nums[0] * k > target or nums[-1] * k < target:
                return res

            # Base Case: Two Pointers
            if k == 2:
                l, r = 0, len(nums) - 1
                while l < r:
                    total = nums[l] + nums[r]
                    if total < target: l += 1
                    elif total > target: r -= 1
                    else:
                        res.append([nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]: l += 1
                        while l < r and nums[r] == nums[r+1]: r -= 1
                return res

            # Recursive Step: Anchor and reduce K
            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i-1]:
                    # Find combinations for (target - nums[i]) using (k-1) elements
                    subsets = kSum(nums[i+1:], target - nums[i], k - 1)
                    for subset in subsets:
                        res.append([nums[i]] + subset)
            return res

        return kSum(nums, target, 4)
```