# 85. Fibonacci Number

## Problem Description
Given `n`, compute the nth Fibonacci number.

**Fibonacci sequence:** 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Formula: `F(n) = F(n-1) + F(n-2)` with `F(0) = 0`, `F(1) = 1`

## Layman's Explanation
Each Fibonacci number is the sum of the two preceding ones.

**Example:** `n = 6`
```
F(0) = 0
F(1) = 1
F(2) = F(1) + F(0) = 1 + 0 = 1
F(3) = F(2) + F(1) = 1 + 1 = 2
F(4) = F(3) + F(2) = 2 + 1 = 3
F(5) = F(4) + F(3) = 3 + 2 = 5
F(6) = F(5) + F(4) = 5 + 3 = 8
```

**Result:** `8`

## Approach 1: Simple Recursion (Slow)
```python
def fib(self, N: int) -> int:
    if N <= 1:
        return N
    return self.fib(N - 1) + self.fib(N - 2)
```

**Problem:** Recalculates the same values many times → O(2^n) time!

## Approach 2: Memoization (Fast)
```python
dp = collections.defaultdict(int)

def fib(self, N: int) -> int:
    if N <= 1:
        return N
    
    if self.dp[N]:
        return self.dp[N]  # Already computed!
    
    self.dp[N] = self.fib(N - 1) + self.fib(N - 2)
    return self.dp[N]
```

**Memoization:** Store computed results to avoid redundant calculations.

### Visualization of Memoization

Without memoization for F(5):
```
                    F(5)
                  /      \
               F(4)      F(3)  ← F(3) calculated twice!
              /    \    /    \
           F(3)   F(2) F(2)  F(1)
          /    \
       F(2)   F(1)
       ...
```

With memoization:
```
F(5) → calls F(4) and F(3)
F(4) → calls F(3) and F(2) (stores results)
F(3) → already cached! Return immediately
```

## Approach 3: Bottom-up (Iterative)
```python
def fib(self, n: int) -> int:
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]
```

## Complexity Analysis

| Approach | Time | Space |
|----------|------|-------|
| Recursion | O(2^n) | O(n) stack |
| Memoization | O(n) | O(n) |
| Iterative | O(n) | O(n) or O(1) |

## Key Insights
1. **Overlapping subproblems:** Same F(k) is needed multiple times
2. **Optimal substructure:** F(n) depends on F(n-1) and F(n-2)
3. **Dynamic Programming:** Store results to avoid recomputation
4. **Space optimization:** Only need last two values → O(1) space possible
