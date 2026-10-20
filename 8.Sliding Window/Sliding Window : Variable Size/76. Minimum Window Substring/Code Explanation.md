# Problem Explanation

## 76. Minimum Window Substring

## Step 1: Understand the Problem

- **Input:** A master string `s` and a target string `t`.
- **Output:** The shortest contiguous substring in `s` that contains every character from `t`, including duplicates. If none exists, return an empty string `""`.
- **Definition:** If `t` is `"AABC"`, your window must contain at least two 'A's, one 'B', and one 'C'. It can contain extra characters, but it must satisfy the minimum frequencies.
- **Goal:** Efficiently track when all requirements are met without recounting the entire window at every step.

## Step 2: Work Through Examples

- **Example 1:**
    - `s` = `"ADOBECODEBANC"`, `t = "ABC"`
    - Target counts: `A:1, B:1, C:1`. `need` = 3.
    - *Expand:* `"ADOBEC"` → Contains A, B, C. `have` = 3. Valid! Size = 6.
    - *Shrink:* Drop A. `"DOBEC"` → `have` drops to 2. Invalid.
    - *Expand:* `"DOBECODEBA"` → Contains B, C, A. `have` = 3. Valid! Size = 10.
    - *Shrink:* Drop D, O, B, E. `"CODEBA"` → Valid! Size = 6.
    - *Shrink:* Drop C. `"ODEBA"` → Invalid.
    - *Expand:* `"ODEBANC"` → Contains B, A, C. `have` = 3. Valid! Size = 7.
    - *Shrink:* Drop O, D, E. `"BANC"` → Valid! Size = 4.
    - **Output:** `"BANC"`

## Step 3: Identify the Problem Type

- **Dynamic Sliding Window + Two Hash Maps:** The ultimate test of the sliding window pattern. You need one map to store the static target requirements, and one map to track the dynamic state of your window.

## Step 4: Think About Approaches

- **Brute Force (O(N2) Time):** Check every substring. Re-count all characters for every substring to see if it matches `t`.
    - *Critique:* Massive Time Limit Exceeded (TLE).
- **Dynamic Sliding Window with `have` and `need` (O(N) Time):** This is your provided code.
    - Instead of comparing two entire Hash Maps on every iteration (which would take O(26) or O(128) time per step), you use two integer counters: `have` and `need`.
    - You only increment `have` when a character's frequency in the window *exactly* matches its requirement in `t`.
    - *Critique:* Flawless. This is the exact optimal solution expected in FAANG interviews for this famous "Hard" problem.

## Step 5: Plan Before Coding

- **Pseudocode:**

Plaintext

```
function minWindow(s, t):
// 1. Setup Target and Trackers
target = frequency map of t
freq = empty map
have = 0, need = length of target's unique keys

// 2. Expand Window
for r from 0 to length of s:
    incoming = s[r]
    if incoming is in target:
        increment freq[incoming]
        if freq[incoming] exactly equals target[incoming]:
            have += 1

    // 3. Shrink Window
    while have == need:
        update min_len and res_str if current window is smaller

        outgoing = s[l]
        if outgoing is in target:
            decrement freq[outgoing]
            if freq[outgoing] falls below target[outgoing]:
                have -= 1 // Breaks the loop!

        l += 1

return res_str
```

## Step 6: Consider Edge Cases

- **`s` is shorter than `t`:** `s = "a", t = "aa"`. The `have == need` condition will literally never trigger. The function naturally skips the inner loop and returns `""`.
- **Excess duplicate characters:** `s = "AAAA", t = "A"`. The `have` counter only increments when `freq['A'] == target['A']` (at exactly 1). For the 2nd, 3rd, and 4th 'A', `have` is untouched, meaning it never exceeds `need` and doesn't break the logic.

## Step 7: Complexity Analysis

- **Time Complexity:** O(N+M), where N is the length of `s` and M is the length of `t`. Building the target counter takes O(M). The sliding window `r` and `l` pointers traverse `s` exactly once each, taking O(N). Because you use `have` and `need`, you never iterate over the dictionaries to compare them, keeping the inner loop work strictly O(1).
- **Space Complexity:** O(1) auxiliary space (or O(U) where U is the number of unique characters in the alphabet). The Hash Maps will never exceed 128 keys (standard ASCII), which counts as constant space regardless of string size.

## Step 8: Review and Reflect

- **Mastery Reached:** You took the hint about `have` and `need` from the previous turn and implemented it perfectly. This separates average candidates from top-tier candidates. Comparing dictionaries directly inside a loop is the most common mistake here, and you bypassed it completely.

# Code Explanation

## The Analogy: The Scavenger Hunt Checklist

Imagine you are on a scavenger hunt. The required list (`target`) says you need 2 Apples, 1 Banana, and 1 Carrot. You have exactly 3 unique *categories* to fulfill (`need = 3`).
You walk down a street (`s`) collecting items in your backpack (`freq`).
When you pick up your 1st Apple, your category requirement isn't met yet. When you pick up your 2nd Apple, you check off the "Apple" category on your list (`have += 1`). Picking up a 3rd Apple is fine, but you don't check the box again.
Once you check off all 3 categories (`while have == need`), you know your backpack is valid!
Because you are lazy and don't want to carry a heavy backpack, you start dropping items from the bottom of your bag (`outgoing`). You drop a 3rd Apple? Fine, the box is still checked. You drop the 2nd Apple? Uh oh! You uncheck the "Apple" category (`have -= 1`), and you must resume walking down the street to find a replacement.

## Step 1: The Checklist Setup

Python

```
target = Counter(t)
freq = {}
min_len = float('inf')
res_str = ""
have, need = 0, len(target)
```

- **What it does:** Uses Python's `Counter` to instantly map the requirements. `need` is set to the number of *unique* characters required (the length of the dictionary), not the total length of string `t`.

## Step 2: Fulfilling the Categories

Python

```
for r in range(len(s)):
    incoming = s[r]

    if incoming in target:
        freq[incoming] = freq.get(incoming, 0) + 1

        if freq[incoming] == target[incoming]:
            have += 1
```

- **What it does:** Expands the right pointer. It strictly ignores characters that aren't in the target string. If an incoming character pushes its current frequency to exactly match the required frequency, a category is fulfilled (`have += 1`).

## Step 3: Shrinking the Backpack

Python

```
    while have == need:
        current_len = r-l+1
        if current_len < min_len:
            min_len = current_len
            res_str = s[l:r+1]
```

- **What it does:** Triggers only when all requirements are met. It checks if the current physical window is the shortest found so far, and if so, records it.

## Step 4: Unchecking the Boxes

Python

```
        outgoing = s[l]
        if outgoing in target:
            freq[outgoing] -= 1
            if freq[outgoing] < target[outgoing]:
                have -= 1
            if freq[outgoing] == 0:
                del freq[outgoing]
        l += 1
```

- **What it does:** Looks at the character about to be dropped from the left. If it's a target character, it removes it from our backpack (`freq`). If dropping it causes our held amount to fall *strictly below* the required amount, we uncheck the category (`have -= 1`), which immediately terminates the `while` loop and forces `r` to expand again!

# Analysis Summary (Deep Revision Framework)

- **The Core Idea:** To find the minimum window containing a target string's characters, use two pointers to create a dynamic sliding window. Maintain two Hash Maps (one for target counts, one for current window counts) and two integers (`have` and `need`) to track how many unique character requirements are fully satisfied. Expand the window until `have == need`, then shrink from the left to optimize length, updating `have` dynamically.
- **Data Structure Choice:** Two Hash Maps (`collections.Counter` and `dict`).
- **Algorithm Pattern:** Dynamic Sliding Window.
- **Complexity:**
    - **Time:** O(N+M)
    - **Space:** O(1) (Bounded by alphabet size).
- **Articulate the Solution:** "I used a dynamic sliding window combined with frequency maps. To avoid comparing dictionaries in O(26) time on every loop, I introduced a `have` and `need` counter. `need` represents the number of unique characters in `t`. As I expanded the right pointer, I incremented `have` whenever a character's window frequency perfectly matched its target frequency. Once `have` equaled `need`, I recorded the window size and shrank the left pointer until `have` dropped below `need`. This achieved an optimal O(N+M) linear time solution."

# Key Notes

## A High-Performance Micro-Optimization

Your logic is pristine, but there is one line that can slow down your code in a strict production environment:

Python

```
# Inside the while loop
res_str = s[l:r+1]
```

**The Issue:** Slicing a string in Python creates a brand-new string object in memory. If the string is massive, performing this string allocation repeatedly inside the `while` loop takes extra time and memory.

**The Fix:** Instead of slicing the string at every step, just store the raw `left` and `right` indices! Only slice the string exactly *once* at the very end of the function.

Python

```
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # ... setup ...
        res_l, res_r = -1, -1  # Track indices instead of strings

        # ... loop logic ...
        while have == need:
            if (r - l + 1) < min_len:
                min_len = r - l + 1
                res_l, res_r = l, r  # Just save the integers!

            # ... shrinking logic ...

        return s[res_l : res_r + 1] if min_len != float('inf') else ""
```

This avoids creating useless intermediate strings and pushes the solution to maximum hardware efficiency.