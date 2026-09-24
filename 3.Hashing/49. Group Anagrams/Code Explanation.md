# Problem Explanation

## 49. Group Anagrams

## Step 1: Understand the Problem

- **Input:** An array of strings `strs`.
- **Output:** A list of lists, where each inner list contains words that are anagrams of each other.
- **Definition:** An anagram is a word formed by rearranging the letters of a different word. Therefore, all anagrams must consist of the exact same characters in the exact same quantities.
- **Goal:** Group these related words together efficiently without writing a massive O(N2) loop that manually compares every string against every other string.

## Step 2: Work Through Examples

- **Example 1:**
    - `strs` = `["eat", "tea", "tan", "ate", "nat", "bat"]`
    - `"eat"`, `"tea"`, `"ate"` all contain 1 'a', 1 'e', 1 't'. Sorted: `"aet"`.
    - `"tan"`, `"nat"` all contain 1 'a', 1 'n', 1 't'. Sorted: `"ant"`.
    - `"bat"` contains 1 'a', 1 'b', 1 't'. Sorted: `"abt"`.
    - **Output:** `[["bat"], ["nat","tan"], ["ate","eat","tea"]]` *(Note: the order of groups does not matter).*

## Step 3: Identify the Problem Type

- **Hash Map (Categorization):** You have a collection of items that need to be grouped by a shared underlying trait. Whenever you need to "group by X", a Hash Map is almost always the correct data structure.

## Step 4: Think About Approaches

- **Sort Every Word (Your Approach):**
    - Sort each string alphabetically. Use the sorted string as the key in a Hash Map. Append the original string to the list of values for that key.
    - *Critique:* Highly readable, very Pythonic, and generally accepted as a fantastic solution in interviews for standard input sizes.
- **Character Frequency Array (O(N×K) Time):**
    - Instead of sorting, count the characters. Create a 26-element array/tuple representing the counts of 'a' through 'z'. Use this tuple as the Hash Map key.
    - *Critique:* The absolute most optimal solution. It completely eliminates the O(KlogK) sorting penalty (detailed in Key Notes below).

## Step 5: Plan Before Coding

- **Pseudocode:**

Plaintext

```python
function groupAnagrams(strs):
// 1. Setup Hash Map
anagram_map = dictionary mapping strings to lists

// 2. Process each word
for word in strs:
    // Create the unique signature
    signature = alphabetically sort(word)

    // Group the word
    append word to anagram_map[signature]

// 3. Extract the groups
return all values from anagram_map
```

## Step 6: Consider Edge Cases

- **Empty Array:** `strs = []`. The loop never runs, and it returns `[]`. Perfect.
- **Empty Strings:** `strs = [""]`. The sorted version of `""` is `""`. The dictionary naturally handles `{"": [""]}`.
- **Single Element:** `strs = ["a"]`. Works effortlessly.

## Step 7: Complexity Analysis

- **Time Complexity:** O(N×KlogK), where N is the number of strings and K is the maximum length of a string. You iterate through N strings, and for each string, you call `sorted()`, which takes O(KlogK) time.
- **Space Complexity:** O(N×K). You are storing every string inside the Hash Map's value lists. In the worst case, the total memory consumed is equivalent to the size of the original input array.

## Step 8: Review and Reflect

- **Python `defaultdict` Mastery:** Your use of `from collections import defaultdict` is excellent. It saves you from writing clunky initialization checks like `if key not in map: map[key] = []`.

# Code Explanation

## The Analogy: The LEGO Sorter

Imagine you are handed several bags of LEGOs. Each bag contains a different finished model (a "word"), like a house, a car, or a boat. You want to group the bags that were built from the exact same pile of raw bricks.
To do this quickly, you tear down every model and line up its bricks by color and size (`sorted(word)`). This sorted line of bricks is your "blueprint" (the Hash Map key).
Whenever you tear down a model and see it matches a blueprint you've seen before, you toss the bag into that blueprint's specific bin (`anagram_map[key].append(word)`).
At the end, you just grab all the bins (`anagram_map.values()`)!

## Step 1: The Grouping Map

Python

```python
anagram_map = defaultdict(list)
```

- **What it does:** Creates a Hash Map where, if a key doesn't exist yet, it automatically initializes with an empty list (`[]`). This allows you to append to it immediately without throwing a `KeyError`.

## Step 2: The Signature Generation

Python

```python
for word in strs:
    key = "".join(sorted(word))
```

- **What it does:** Iterates over the strings. `sorted(word)` returns a list of sorted characters (e.g., `['a', 'e', 't']`). `"".join()` stitches them back into a single string `"aet"`. This sorted string acts as the universal signature for all anagrams of that word.

## Step 3: The Categorization

Python

```python
    anagram_map[key].append(word)
return list(anagram_map.values())
```

- **What it does:** Adds the *original* (unsorted) word to the list associated with that specific sorted signature. Finally, it extracts all the grouped lists using `.values()` and casts them to a list for the final output.

# Analysis Summary (Deep Revision Framework)

- **The Core Idea:** Anagrams are identical when their characters are sorted. By generating a sorted version of each string, you can use it as a universal Hash Map key to group all original strings that share the exact same character makeup.
- **Data Structure Choice:** Hash Map (`collections.defaultdict(list)`).
- **Algorithm Pattern:** Categorization / Hashing.
- **Complexity:**
    - **Time:** O(N×KlogK)
    - **Space:** O(N×K)
- **Articulate the Solution:** "To group anagrams efficiently, I used a Hash Map to categorize them by a shared signature. I iterated through the array, sorting each string alphabetically. Because anagrams consist of the same characters, their sorted strings are identical. I used this sorted string as the dictionary key and appended the original string to the corresponding list. Finally, I returned the dictionary's values, resulting in an O(N×KlogK) time complexity."

## Spaced Repetition & Follow-ups

Here are a few related string/hashing problems to solve next:

1. **LeetCode 242. Valid Anagram:** The most foundational anagram problem. Can you solve it in O(N) time using frequency counting instead of sorting?
2. **LeetCode 438. Find All Anagrams in a String:** This combines anagram frequency counting with the **Fixed Sliding Window** technique you mastered earlier!
3. **LeetCode 249. Group Shifted Strings:** A step up in difficulty. Instead of grouping by exact characters, you must group by the *distance* between the characters (e.g., "abc" groups with "bcd" because every letter shifted by +1).

# Key Notes

## The O(N×K) Interview Optimization (Frequency Tuples)

Sorting strings takes O(KlogK) time. If the strings are very long, sorting becomes a massive bottleneck.

Because the problem guarantees strings consist only of **lowercase English letters**, you can skip sorting entirely! Instead, count the frequency of each character (a to z) and use that frequency count as the key.

*Crucial Python Detail:* Lists `[]` cannot be used as dictionary keys because they are mutable (unhashable). You must use a `tuple` `()` instead!

Python

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_map = defaultdict(list)

        for word in strs:
            # Create a 26-slot array for 'a' through 'z'
            count = [0] * 26

            for char in word:
                # ord(char) - ord('a') maps 'a' to 0, 'b' to 1, etc.
                count[ord(char) - ord('a')] += 1

            # Convert the list to a tuple so it can be hashed as a dict key
            anagram_map[tuple(count)].append(word)

        return list(anagram_map.values())
```