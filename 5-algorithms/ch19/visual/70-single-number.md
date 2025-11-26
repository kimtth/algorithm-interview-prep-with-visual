# 70. Single Number

## Problem Description
Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.

**Requirement:** Implement with O(1) extra space.

## Layman's Explanation
Imagine a dance party where everyone has a partner except one person. How do you find the lonely dancer?

**The XOR Magic:**
XOR (exclusive or) has a special property:
- `A ^ A = 0` (same numbers cancel out)
- `A ^ 0 = A` (XOR with 0 keeps the number)
- `A ^ B ^ A = B` (order doesn't matter, pairs cancel)

So if you XOR ALL numbers together:
- Every pair cancels out (becomes 0)
- Only the single number remains!

**Example:** `[4, 1, 2, 1, 2]`
```
4 ^ 1 ^ 2 ^ 1 ^ 2
= 4 ^ (1 ^ 1) ^ (2 ^ 2)  ← group pairs
= 4 ^ 0 ^ 0              ← pairs cancel
= 4                       ← single number!
```

## Algorithm Walkthrough
Given: `nums = [4, 1, 2, 1, 2]`

| Step | Current num | result (before) | Operation | result (after) |
|------|-------------|-----------------|-----------|----------------|
| 0    | -           | 0               | -         | 0              |
| 1    | 4           | 0               | 0 ^ 4     | 4              |
| 2    | 1           | 4               | 4 ^ 1     | 5              |
| 3    | 2           | 5               | 5 ^ 2     | 7              |
| 4    | 1           | 7               | 7 ^ 1     | 6              |
| 5    | 2           | 6               | 6 ^ 2     | 4 ✓            |

**Binary representation:**
```
4 = 100
1 = 001
2 = 010

100 ^ 001 = 101 (5)
101 ^ 010 = 111 (7)
111 ^ 001 = 110 (6)
110 ^ 010 = 100 (4) ✓
```

## Code Explanation
```python
def singleNumber(self, nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num  # XOR each number
    return result
```

One-liner using reduce:
```python
from functools import reduce
return reduce(lambda x, y: x ^ y, nums)
```

## Complexity Analysis
- **Time Complexity:** O(n) - Single pass through the array
- **Space Complexity:** O(1) - Only one variable

## Key Insights
1. **XOR Properties:**
   - Commutative: `A ^ B = B ^ A`
   - Associative: `(A ^ B) ^ C = A ^ (B ^ C)`
   - Self-inverse: `A ^ A = 0`
   - Identity: `A ^ 0 = A`
2. **Why it works:** All pairs cancel, leaving only the single number
3. **Constraint:** Every other element must appear exactly twice
4. **Extension:** For "every element appears 3 times except one", use bit counting
