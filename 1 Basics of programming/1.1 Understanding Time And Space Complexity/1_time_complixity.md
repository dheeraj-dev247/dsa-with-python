# Time Complexity and Space Complexity in DSA | Explained with Examples

Time complexity and space complexity both measure an algorithm’s efficiency.

- **Time complexity** shows how the running time increases with input size.
- **Space complexity** tracks memory usage.

Both are essential for optimizing algorithms — especially when dealing with large datasets or limited resources.

In this article, we will explore these two concepts of algorithm analysis along with their **examples, cases, best practices, and more**.

---

## 📘 Contents

- [What is Time Complexity?](#what-is-time-complexity)
- [Rules for Calculating Time Complexity](#rules-for-calculating-time-complexity)
- [Avoiding Constant Terms](#avoid-including-the-constant-terms)
- [What is Space Complexity?](#what-is-space-complexity)
- [Competitive Programming Tips](#points-to-remember-for-competitive-programming)
- [Conclusion](#conclusion)

---

## What is Time Complexity?

When solving a problem, there may be multiple approaches to achieve the same result.  
**Time complexity** helps us evaluate and compare these approaches — determining which one is more efficient.

> It’s not about the time a machine takes, but about how the code scales with input size.

Time complexity measures **how the time required to execute code changes** as the input size grows. It is independent of the machine used to execute the code and focuses solely on the algorithm’s behavior.

---

### Representing the Time Complexity of Any Code

**Example:**

```python
i = 1
while i <= 5:
    print("Code and Debug")
    i += 1
```

---

### Step-by-Step Analysis

In terms of **Big O notation**, time complexity reflects the number of steps relative to input size.

1. Initialization: `i = 1`
2. Comparison: `i <= 5`
3. Execution: `print("Code and Debug")`
4. Increment: `i += 1`

This loop runs **5 times**, each involving 3 steps → `5 × 3 = 15`.

👉 Hence, **O(15)**, but constants are ignored, so **O(N)**.

---

### Generalizing for N

If 5 is replaced with `N`:

```
Steps = 3N  →  O(N)
```

---

### Why Machine Time Is Not Reliable

Actual execution time varies across machines:

- A low-end Windows PC vs a high-end MacBook will yield different results.
- Hardware (processor, memory, etc.) affects performance.

Hence, **we use algorithmic analysis (Big O)** for fair comparison.

---

### Why Manual Counting Isn’t Feasible

Manual counting works for small snippets but fails for:

- Loops running millions of times
- Nested or complex operations

Thus, we use systematic rules to calculate time complexity.

---

## Rules for Calculating Time Complexity

To simplify the process, follow these rules:

1. **Worst-case scenario** — always analyze the worst case.
2. **Ignore constant factors** — constants don’t affect scalability.
3. **Focus on growth rate** — ignore lower-order terms.

---

### Example

```python
marks = int(input("Enter your marks = "))

if marks >= 90:
    print("A")
elif marks >= 80 and marks < 90:
    print("B")
elif marks >= 70 and marks < 80:
    print("C")
elif marks >= 60 and marks < 70:
    print("D")
elif marks >= 50 and marks < 60:
    print("E")
else:
    print("Fail")
```

---

### Step-by-Step Explanation

- **Initialization:** Takes input for `marks`
- **Condition Checks:** Compared against thresholds
- **Output:** Prints the corresponding grade

---

#### 1. Best Case

If `marks = 95`, the first condition is True:

- Input → Check `marks >= 90` → Print `A`
  ✅ **3 steps (minimum)**

---

#### 2. Worst Case

If `marks = 45`, all conditions checked before `else` executes:

- Input → 5 condition checks → Print “Fail”
  ❌ **7 steps (maximum)**
  👉 **O(k)** where k = number of conditions (6 in this case)

---

#### 3. Average Case

If `marks = 75`, conditions checked until grade “C”:

- Input → Check ≥90 → ≥80 → ≥70 → Print “C”
  ≈ **5 steps**

---

### Why Focus on the Worst Case?

- Ensures **robustness**
- Predicts **scalability**
- Serves as a **standard benchmark**

---

## Avoid Including the Constant Terms

Consider:

```
T(N) = 5N¹⁰ + 8N³ + 2
```

For large N:

- 5N¹⁰ dominates
- 8N³ and 2 are negligible

Hence, we write **O(N¹⁰)**.

✅ **Big O focuses on growth rate, not actual counts.**

---

## What is Space Complexity?

**Space complexity** measures the amount of memory used by a program during execution — including:

- **Input space:** Memory to store input data
- **Auxiliary space:** Extra memory for variables, structures, etc.

Represented in **Big O notation** (not MB/GB).

---

### Example

```python
a = int(input())  # Input space
b = int(input())  # Input space
c = a + b         # Auxiliary space
print(c)
```

Here:

- Input space → `a`, `b`
- Auxiliary space → `c`

Total: **O(3)** → Simplifies to **O(1)** (constant space)

---

### Using Arrays

If an array of size `N` is used → **O(N)** space complexity.

---

### Good Coding Practice: Avoid Input Manipulation

Instead of:

```python
b = a + b
```

Prefer using a new variable:

```python
c = a + b
```

Reasons:

- Maintains **input integrity**
- Avoids **unintended side effects**
- Follows **company standards**

> Only modify input if explicitly instructed to do so.

---

## Points to Remember for Competitive Programming

Online judges (like LeetCode, GfG, etc.) execute ~10⁸ operations per second.

| Time Limit | Allowed Operations |
| ---------- | ------------------ |
| 2 seconds  | ≤ 2 × 10⁸          |
| 5 seconds  | ≤ 5 × 10⁸          |

✅ Keep time complexity ≈ **O(10⁸)** operations to stay safe.

---

## 🧭 Conclusion

By understanding and optimizing both **time** and **space complexity**, you can:

- Write **efficient & scalable code**
- Perform well in **coding interviews**
- Handle **real-world systems effectively**

> Always maintain input integrity, optimize for growth rate, and stay mindful of execution limits.

---

_Master these fundamentals — and you’re well on your way to building world-class algorithms._
