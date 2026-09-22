# Problem Explanation

## 50. Pow(x, n)

### Step 1: Understand the Problem

- **Input:** A floating-point number `x` and an integer `n`.
- **Output:** A floating-point number representing $x^n$.
- **Goal:** Implement a power function that calculates $x$ raised to the power of $n$.
- **Note:** The solution must handle negative exponents (where $x^{-n} = 1/x^n$) and be efficient enough to handle large values of `n` without timing out.

### Step 2: Work Through Examples

- **Example 1:** `x = 2.00000`, `n = 10`
    - We need to calculate $2^{10}$.
    - **Output:** `1024.00000`.
- **Example 2:** `x = 2.10000`, `n = 3`
    - Calculation: $2.1 \times 2.1 \times 2.1$.
    - **Output:** `9.26100`.
- **Example 3:** `x = 2.00000`, `n = -2`
    - Negative exponent means reciprocal: $1 / 2^2 = 1 / 4$.
    - **Output:** `0.25000`.

### Step 3: Identify the Problem Type

- Recursion
- Divide and Conquer
- Mathematical Optimization (Binary Exponentiation)

### Step 4: Think About Approaches

1. **Brute-Force (O(n)):** Loop from 1 to `n` and multiply `x` by itself each time.
    - *Drawback:* If `n` is large (e.g., $2^{31}-1$), this will cause a Time Limit Exceeded (TLE).
2. **Binary Exponentiation (O(log n)):** The implemented solution. Instead of multiplying `x` one by one, we calculate $x^{n/2}$ and square it. This cuts the number of operations in half at every step, making it logarithmically fast.

### Step 5: Plan Before Coding

**Pseudocode:**

Plaintext

`function myPow(x, n):
  // 1. Handle negative exponents by calculating power for abs(n)
  //    and taking the reciprocal later.
  N = abs(n)
  
  // 2. Define recursive helper function
  function power(x, N):
      if N == 0: return 1
      if x == 0: return 0
      
      // Divide step
      res = power(x, N // 2)
      
      // Conquer step (Square the result)
      res = res * res
      
      // If N is odd, multiply by x one more time
      if N is odd: return x * res
      else: return res

  result = power(x, N)
  
  // 3. Return result (or reciprocal if n was negative)
  if n >= 0: return result
  else: return 1 / result`

### Step 6: Consider Edge Cases

- `n = 0`: The code correctly returns 1 (mathematical definition).
- `x = 0`: The code returns 0.
- `n < 0`: The logic handles this by calculating the positive power first and returning `1 / result`.

### Step 7: Complexity Analysis

- **Time Complexity:** $O(\log n)$. Since we divide `n` by 2 in every step, the number of operations is proportional to the number of bits in `n`.
- **Space Complexity:** $O(\log n)$. The recursion stack will go as deep as the number of divisions needed.

### Step 8: Review and Reflect

- **Why does this work?** It exploits the mathematical property that $x^n = x^{n/2} \times x^{n/2}$. By calculating $x^{n/2}$ once and storing it, we avoid redundant calculations.
- **Can it be improved?** The recursive approach uses stack space. An **iterative** approach using a `while` loop and bitwise operations can achieve the same time complexity with $O(1)$ space.

---

# Code Explanation

### The Analogy: The "Folding Paper" Shortcut

Think of calculating $x^n$ like creating a stack of paper `n` sheets thick.

- **Linear Way:** Stack one sheet at a time. (Takes `n` steps).
- **Recursive Way:**
    1. Start with 1 sheet.
    2. **Fold it in half** (Double the thickness). Now you have 2 layers.
    3. **Fold it again**. Now 4 layers.
    4. **Fold it again**. Now 8 layers.
    - You reach huge numbers very quickly. This code is essentially "folding" the number to reach the target power.

### Step 1: The Setup & Handling Negatives

**Code:**

Python

`res = power(x, abs(n))

if n >= 0:
    return res
else:
    return 1 / res`

- **What it does:** It simplifies the core logic. Instead of worrying about negative math inside the recursion, we calculate the power as if `n` were positive. If the original `n` was negative, we just flip the result (take the reciprocal) at the very end.

### Step 2: The Recursive Division

**Code:**

Python

`if n == 0: return 1
res = power(x, n // 2)`

- **What it does:** This is the **Divide** step.
- To solve for `n=10`, the function calls itself for `n=5`.
- To solve for `n=5`, it calls for `n=2`.
- It keeps drilling down until `n=0`, where it returns 1.

### Step 3: Squaring and Adjusting

**Code:**

Python

`res = res * res

if n % 2 != 0:
    return x * res
else:
    return res`

- **What it does:** This is the **Conquer** step.
- **Squaring:** We take the result of the half-problem (`res`) and multiply it by itself. This effectively doubles the exponent (e.g., $x^5 \times x^5 = x^{10}$).
- **Odd Adjustment:** If the current `n` was odd (like 5), integer division (`5 // 2 = 2`) truncated the remainder. Squaring $x^2$ gives $x^4$. We are missing one $x$, so we multiply `res` by `x` to correct it.

---

# Analysis Summary (Deep Revision Framework)

### The Core Idea:

The one-sentence summary is: **"We use Binary Exponentiation to compute the power in logarithmic time by recursively calculating half the power ($x^{n/2}$), squaring the result, and performing an extra multiplication if the exponent is odd."**

### Data Structure Choice:

The solution uses the **System Call Stack** (Recursion). No explicit data structures like arrays or hashmaps are needed, but the stack holds the state of the computation at each level of division.

### Algorithm Pattern:

This is a classic **Divide and Conquer** algorithm. Specifically, it is **Exponentiation by Squaring**. It breaks the problem into subproblems of half the size, solves one, and reuses the solution.

### Complexity:

- **Time Complexity:** $O(\log n)$. The input `n` is halved at every step.
- **Space Complexity:** $O(\log n)$. The recursion depth is proportional to the logarithm of `n`.

### Articulate the Solution:

"I solved this problem using the Divide and Conquer approach known as Binary Exponentiation."

"First, I handled the edge case of negative exponents by using the absolute value of n and taking the reciprocal of the final result."

"I defined a recursive function that calculates the power for n // 2. I store this result and square it to double the exponent."

"If n is odd, I multiply the result by x one more time to account for the remainder. This approach reduces the complexity from linear $O(n)$ to logarithmic $O(\log n)$."

### Spaced Repetition & Follow-ups:

- **Iterative Approach:** Can you rewrite this using a `while` loop to save stack space? (Using bitwise operators).
- **Modular Exponentiation:** How would you change this if you needed to return the result modulo $10^9 + 7$? (Apply `% mod` at every multiplication).