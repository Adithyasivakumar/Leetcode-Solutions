### 14. Longest Common Prefix

### Step 1: Understand the Problem

**Input:** A list of strings `strs`.
**Output:** A single string that is the longest prefix common to all strings in the input list. If no common prefix exists, the output should be an empty string `""`.
**Constraints:** The list can contain between 1 and 200 strings. Each string can have a length between 0 and 200 characters and consists of only lowercase English letters.

---

### Step 2: Work Through Examples

**Example 1:**

- Input: `strs = ["flower","flow","flight"]`
- Output: `"fl"` (Explanation: 'f' and 'l' are common to the start of all three words. The third character 'o'/'i' is a mismatch.)

**Example 2:**

- Input: `strs = ["dog","racecar","car"]`
- Output: `""` (Explanation: The very first characters 'd', 'r', and 'c' do not match, so there is no common prefix.)

**Example 3:**

- Input: `strs = ["interrupt","internal","interview"]`
- Output: `"inter"` (Explanation: The prefix "inter" is common to all three words.)

---

### Step 3: Identify the Problem Type

- String manipulation
- Array / List iteration
- Character-by-character comparison

---

### Step 4: Think About Approaches

- **Horizontal Scanning:** Assume the first string is the prefix. Compare it to the second string and shorten the prefix if they don't match. Take that result and compare it to the third string, and so on. This is a valid approach but can be less efficient if the first string is very long.
- **Vertical Scanning (Optimal):** Compare characters column by column. Take the first character of the first string and see if it's the first character of every other string. If yes, move to the second character and repeat. This is the approach used in the provided code as it can fail fast on the first mismatch.

---

### Step 5: Plan Before Coding

**Pseudocode (for the Vertical Scanning approach):**

`function Longest_common_prefix(strs):
  If the list 'strs' is empty, return ""

  // Use the first string as the reference for length
  Loop i from 0 to length(strs[0]) - 1:
    char_to_check = strs[0][i]

    // Now, check this character against all other strings
    Loop j from 1 to length(strs) - 1:
      // A prefix ends if a string is too short OR a character mismatches
      If i is past the end of strs[j] OR strs[j][i] is not char_to_check:
        Return the prefix found so far (from index 0 up to i)

  // If the outer loop completes, the entire first string is the common prefix
  Return strs[0]`

---

### Step 6: Consider Edge Cases

- **Empty input list:** `[]` should become `""`. The code handles this with `if not strs:`.
- **List with a single string:** `["computer"]` should become `"computer"`. The code handles this, as the inner loop never runs and the function returns `strs[0]`.
- **A string in the list is empty:** `["apple", "", "apply"]` should become `""`. The code handles this when `i >= len(strs[j])` becomes true for the empty string at `i=0`.
- **No common prefix:** `["abc", "def", "ghi"]` should become `""`. The code finds a mismatch at the very first character (`i=0`) and returns `strs[0][:0]`, which is `""`.

---

### Step 7: Complexity Analysis

- **Time Complexity:** O(S), where S is the sum of all characters in all strings. This is often simplified to O(N * M), where N is the number of strings and M is the length of the longest common prefix. The algorithm's performance is bound by checking each character of the final common prefix across all N strings.
- **Space Complexity:** O(1). The algorithm uses a constant amount of extra memory regardless of the input size, as it modifies pointers and indices in-place.

---

### Step 8: Review and Reflect

- **Why does this work?** The vertical scanning method is robust because it confirms one character of the prefix across all strings before moving to the next. This allows it to stop immediately at the "weakest link"—either the shortest string or the first character mismatch.
- **Can it be improved?** For a one-time check, this approach is optimal. Any correct algorithm must, in the worst case, look at a character from every string, so an O(N * M) time complexity is the best possible. Other solutions like using a Trie data structure exist but are better suited for scenarios where you need to perform many prefix queries on the same dictionary of words.