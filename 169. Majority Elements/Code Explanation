# **Problem Explanation**

**169. Majority Element**

**Step 1: Understand the Problem**

- **Input:** An array of integers, `nums`.
- **Output:** A single integer.
- **Goal:** Find the "majority element."
- **Definition:** The majority element is the number that appears **more than n / 2 times**, where `n` is the size of the array.
- **Constraint:** The problem guarantees that a majority element always exists in the input array.

---

**Step 2: Work Through Examples**

- **Example 1: `nums = [3, 2, 3]`**
    - `n = 3`. The majority threshold is `> 3 / 2 = 1.5`.
    - The number `3` appears 2 times, which is greater than 1.5.
    - **Output:** `3`.
    
- **Example 2: `nums = [2, 2, 1, 1, 1, 2, 2]`**
    - `n = 7`. The majority threshold is `> 7 / 2 = 3.5`.
    - The number `2` appears 4 times, which is greater than 3.5.
    - **Output:** `2`.

---

**Step 3: Identify the Problem Type**

- Array Traversal
- Frequency Counting
- **Voting Algorithm** (for the optimal solution)

---

**Step 4: Think About Approaches**

- **Hash Map (O(n) space):** The most intuitive way is to loop through the array and use a hash map to count the frequency of each number. Then, loop through the map to find the number with a count greater than n/2.

- **Sorting (O(n log n) time):** If you sort the array, the majority element is guaranteed to be the element at the middle index (`n // 2`).

- **Boyer-Moore Voting Algorithm (The Implemented Solution):** This is the clever O(1) space solution. It works by canceling out pairs of different elements. Since the majority element appears more than n/2 times, it is guaranteed to be the last one standing.

---

**Step 5: Plan Before Coding**

- **Pseudocode (for the Boyer-Moore algorithm):**
    
    `function majorityElement(nums):
      // 1. Initialize a candidate for the majority element and a counter.
      candidate = null
      count = 0
    
      // 2. Loop through each number in the array.
      For each num in nums:
        // 3. If the count is zero, we need a new candidate.
        if count is 0:
          candidate = num
    
        // 4. If the current number matches the candidate, increment the count.
        if num is equal to candidate:
          increment count
        // 5. If it's a different number, decrement the count.
        else:
          decrement count
    
      // 6. After the loop, the candidate is the majority element.
      return candidate`
    

---

**Step 6: Consider Edge Cases**

- **Single-element array `[5]`:** The loop runs once. `count` becomes 0, `candidate` becomes 5. `count` becomes 1. The loop ends. It correctly returns 5.
- **Array where majority element appears last `[1, 2, 3, 3, 3]`:** The algorithm correctly identifies 3 as the final candidate.

---

**Step 7: Complexity Analysis**

- **Time Complexity: O(n)**. The solution iterates through the array exactly once.
- **Space Complexity: O(1)**. It only uses two extra variables (`majority` and `count`). The memory usage is constant, regardless of the input size.

---

**Step 8: Review and Reflect**

- **Why does this work?** The algorithm works like an election where votes for a candidate are canceled out by votes for any other candidate. Since the majority element has more votes than all other candidates *combined*, it is guaranteed to survive the cancellation process and remain the final candidate.
- **Can it be improved?** In terms of time and space complexity, this solution is optimal. It's a brilliant algorithm for this specific problem.

---

## **Code Explanation**

### The Analogy: The Election

Think of this problem like a political election. You have a list of votes (`nums`), and you want to find the candidate who won by a clear majority.

- **`majority`**: This variable holds our current leading candidate.
- **`count`**: This is the current "lead" or "margin" of our leading candidate.

---

### **Step 1: The Setup**

**Code:**

Python

`majority = None
count = 0`

- **What it does:** It sets up our tracking variables. We start with no leading candidate (`majority = None`) and their lead is zero (`count = 0`).

---

### **Step 2: The Loop**

**Code:**

Python

`for num in nums:`

- **What it does:** We look at every single vote (`num`) in the list, one by one.

---

### **Step 3: Finding a New Leader**

**Code:**

Python

`if count == 0:
    majority = num`

- **What it does:** This is the rule for finding a new leader. It asks: "Is the current leader's margin zero?"
- If the answer is **yes**, it means the previous leader has been completely canceled out. The current vote (`num`) is now used to pick a new leading candidate.

---

### **Step 4: The Voting Process**

**Code:**

Python

`if num == majority:
    count += 1
elif num != majority:
    count -= 1`

- **What it does:** This is how the votes are tallied.
- If the current vote (`num`) is **for** our leading candidate (`majority`), their lead increases by 1 (`count += 1`).
- If the current vote is for a **different** candidate, it cancels out one of the leader's votes, so their lead decreases by 1 (`count -= 1`).

---

### **Step 5: The Final Result**

**Code:**

Python

`return majority`

- **What it does:** After the loop has processed every single vote, the `majority` variable will hold the candidate who survived the cancellation process.

- **Why it works:** Because the true majority element appears more than half the time, it has more votes than all other candidates combined. This guarantees that its `count` will never be permanently canceled out to zero, and it will be the final candidate left standing.

---

## **Analysis Summary (Deep Revision Framework)**

- **The Core Idea:**
The one-sentence summary is: "The code finds the majority element by treating it as an election, where each vote for a candidate is canceled by a vote for an opponent, and the majority candidate is guaranteed to win."

- **Data Structure Choice:**
This algorithm brilliantly uses only two simple integer variables (`majority`, `count`). It does **not** need a complex data structure like a hash map. This is what makes it an **O(1) space** solution, which is its primary advantage. A hash map would be more intuitive but would use O(n) space.

- **Algorithm Pattern:**
This is a famous algorithm known as the **Boyer-Moore Voting Algorithm**. It is a specialized and highly efficient pattern for finding the majority element in a sequence.

- **Complexity:**
    - **Time Complexity: O(n)**. The code makes exactly one pass through the input array.
    - **Space Complexity: O(1)**. It only uses two extra variables. The memory usage is constant.

- **Articulate the Solution:**
    1. "My solution uses the Boyer-Moore Voting Algorithm, which is an O(1) space approach."
    2. "I'll initialize two variables: a `candidate` and a `count`, starting at `None` and `0`."
    3. "I'll iterate through the array once. If my `count` is ever zero, I'll pick the current number as my new `candidate`."
    4. "If the current number matches my `candidate`, I increment the count. If it doesn't, I decrement the count. This effectively cancels out votes between different elements."
    5. "Because the problem guarantees a majority element exists, it will have more votes than all other elements combined and will be the final `candidate` when the loop is done."

- **Spaced Repetition & Follow-ups:**
The main follow-up for this problem is **LeetCode 229. Majority Element II**, which asks for all elements that appear more than `n/3` times. The Boyer-Moore algorithm can be cleverly extended to solve this harder version as well