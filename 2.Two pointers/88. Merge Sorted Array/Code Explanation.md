# Problem Explanation

## 88. Merge Sorted Array

## Step 1: Understand the Problem

- **Input:** Two sorted integer arrays `nums1` and `nums2`, and their respective lengths `m` and `n`. `nums1` has a total size of `m + n` to accommodate the merged elements.
- **Output:** `None`. You must modify `nums1` **in-place**.
- **Definition:** You are combining two pre-sorted arrays into a single sorted array without allocating a brand new array for the result.
- **Goal:** Avoid overwriting the existing elements in `nums1` before they have been evaluated and merged.

## Step 2: Work Through Examples

- **Example 1:**
- `nums1` = `[1, 2, 3, 0, 0, 0]`, `m = 3`
- `nums2` = `[2, 5, 6]`, `n = 3`
- *Setup:* `p1 = 2` (value `3`), `p2 = 2` (value `6`), `p3 = 5` (last zero).
- *Compare:* `3 < 6`. Place `6` at `p3`. `nums1` = `[1, 2, 3, 0, 0, 6]`. Decrement `p2`, `p3`.
- *Compare:* `3 < 5`. Place `5` at `p3`. `nums1` = `[1, 2, 3, 0, 5, 6]`. Decrement `p2`, `p3`.
- *Compare:* `3 > 2`. Place `3` at `p3`. `nums1` = `[1, 2, 3, 3, 5, 6]`. Decrement `p1`, `p3`.
- *Continue until `p1` and `p2` resolve.*
- **Output:** `nums1` becomes `[1, 2, 2, 3, 5, 6]`.

## Step 3: Identify the Problem Type

- **Two Pointers (In-Place Array / Reverse Traversal):** When dealing with in-place array modifications where elements are padded with empty space at the end, standard left-to-right pointers will overwrite data. Reversing the traversal completely solves this.

## Step 4: Think About Approaches

- **Copy and Sort ($O((M+N) \log(M+N))$ Time):** Copy `nums2` into the zeros of `nums1`, then call `nums1.sort()`.
- *Critique:* Bypasses the fact that the arrays are already sorted. Highly penalized in interviews.
- **Three Pointers Backwards ($O(M+N)$ Time, $O(1)$ Space):** This is your provided code.
- Compare the largest remaining elements of both arrays and place the winner at the absolute end of `nums1`, working backwards to the front.
- *Critique:* Excellent architectural logic. This is the optimal approach. However, there are two minor structural flaws regarding the problem constraints (detailed in the Key Notes below).

## Step 5: Plan Before Coding

- **Pseudocode:**

```
function merge(nums1, m, nums2, n):
// 1. Setup Pointers
p1 = m - 1
p2 = n - 1
p3 = m + n - 1

// 2. Merge Backwards
while p1 >= 0 and p2 >= 0:
    if nums1[p1] >= nums2[p2]:
        nums1[p3] = nums1[p1]
        p1 -= 1
    else:
        nums1[p3] = nums2[p2]
        p2 -= 1
    p3 -= 1

// 3. Handle Leftovers
while p2 >= 0:
    nums1[p3] = nums2[p2]
    p2 -= 1
    p3 -= 1

// Note: No return statement needed, modified in-place
```

## Step 6: Consider Edge Cases

- **`m = 0` (Empty `nums1` elements):** `nums1 = [0]`, `m = 0`, `nums2 = [1]`, `n = 1`.
- `p1 = -1`. The main `while` loop is skipped entirely.
- The cleanup `while p2 >= 0` loop safely copies `1` into `nums1[0]`.
- **`n = 0` (Empty `nums2`):** `nums1 = [1]`, `m = 1`, `nums2 = []`, `n = 0`.
- `p2 = -1`. Main loop is skipped. `nums1` remains unmodified, which is mathematically correct.

## Step 7: Complexity Analysis

- **Time Complexity:** $O(M+N)$. Each element from both arrays is evaluated and placed exactly once.
- **Space Complexity:** $O(1)$. All sorting and swapping happen within the existing memory allocation of `nums1`.

## Step 8: Review and Reflect

- **The In-Place Paradigm:** This problem forces you to think about memory safety. By starting from the back, you guarantee that you are only writing into the "empty" padded `0` space, ensuring you never crush an un-evaluated element in `nums1`.

---

# Code Explanation

## The Analogy: The Filing Cabinet

Imagine a large filing cabinet drawer (`nums1`). The front half is packed tightly with folders sorted alphabetically (`m`), and the back half is totally empty space. You have a stack of new folders on your desk (`nums2`), also sorted alphabetically (`n`).
If you try to shove the new folders into the front of the drawer, you have to shift every existing folder backwards to make room, which is exhausting.
Instead, you look at the absolute last folder in the cabinet, and the absolute last folder on your desk. You pick whichever one comes last in the alphabet, and you place it at the very back of the empty space in the cabinet (`p3`). You repeat this until both the cabinet and your desk are perfectly merged.

## Step 1: Pointer Initialization

```python
p1 = m - 1
p2 = n - 1
p3 = m + n - 1
```

- **What it does:** Sets up the read pointers (`p1`, `p2`) at the end of the *valid* data, and the write pointer (`p3`) at the absolute end of the array buffer.

## Step 2: The Backward Merge

```python
while p1 >= 0 and p2 >= 0:
    if nums1[p1] >= nums2[p2]:
        nums1[p3] = nums1[p1]
        p1 -= 1
    else:
        nums1[p3] = nums2[p2]
        p2 -= 1
    p3 -= 1
```

- **What it does:** Greedily pulls the maximum available value from either array and writes it to the back of the buffer.

## Step 3: The Leftover Cleanup

```python
while p2 >= 0:
    nums1[p3] = nums2[p2]
    p2 -= 1
    p3 -= 1
```

- **What it does:** If `nums1` is exhausted first, it means the remaining elements in `nums2` are strictly smaller than everything placed so far. This loop rapidly flushes the remaining `nums2` elements into the front of `nums1`.

---

# Analysis Summary (Deep Revision Framework)

- **The Core Idea:** To merge two sorted arrays in-place without overwriting data, iterate backward. Use three pointers: two reading the largest remaining elements of each array, and one writing to the empty padding at the back of the destination array.
- **Data Structure Choice:** In-Place Array Modification.
- **Algorithm Pattern:** Two Pointers (Reverse Traversal).
- **Complexity:**
- **Time:** $O(M + N)$
- **Space:** $O(1)$
- **Articulate the Solution:** "To merge the arrays in-place optimally, I used a reverse three-pointer approach. Because `nums1` is padded with zeros at the end, iterating from left to right would overwrite unread elements. Instead, I placed pointers at the end of the valid elements in both arrays and a write pointer at the absolute end of `nums1`. I compared the elements, writing the larger one to the back and decrementing the respective pointers. Finally, I flushed any remaining elements from `nums2` into `nums1`, achieving an $O(M+N)$ time complexity and strictly $O(1)$ space."

---

# Key Notes

## Optimization: The Redundant Cleanup Loop

In your provided code, you included a cleanup loop for `nums1`:

```python
# You wrote this in your code:
while p1 >= 0:
    nums1[p3] = nums1[p1]
    p1 -= 1
    p3 -= 1
```

**This loop is mathematically useless and should be deleted.**
Why? Because `p1` and `p3` are both operating inside `nums1`. If `p2` is exhausted, it means all of `nums2` has been merged. The remaining elements at `p1` are *already physically sitting in their correct sorted positions inside `nums1*`. Writing them to themselves just wastes CPU cycles.

## The Return Statement

```python
# You wrote:
return nums1
```

The LeetCode function signature is `def merge(...) -> None:`. The problem explicitly demands you do not return anything, but modify `nums1` in place. While Python doesn't crash if you return a value here, automated testing suites in FAANG interviews often strictly check the return type. Always return nothing when the signature asks for `None`.