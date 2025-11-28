# 87. Climbing Stairs

## Problem Description
You are climbing a staircase. It takes `n` steps to reach the top. Each time you can climb 1 or 2 steps. How many distinct ways can you climb to the top?

## Layman's Explanation
Count all the different combinations of 1s and 2s that add up to n.

**Example:** `n = 4` (4 stairs)
```
1+1+1+1 = 4  ✓
1+1+2 = 4    ✓
1+2+1 = 4    ✓
2+1+1 = 4    ✓
2+2 = 4      ✓
```

**Result:** `5` ways

## Key Insight: This is Fibonacci!

To reach step `n`, you can either:
1. Come from step `n-1` (take 1 step)
2. Come from step `n-2` (take 2 steps)

So: `ways(n) = ways(n-1) + ways(n-2)`

This is the Fibonacci sequence!

### Walkthrough

| n | Ways | Explanation |
|---|------|-------------|
| 1 | 1 | Just `[1]` |
| 2 | 2 | `[1,1]` or `[2]` |
| 3 | 3 | From n=2 (1 step) + From n=1 (2 steps) = 2+1 |
| 4 | 5 | From n=3 (1 step) + From n=2 (2 steps) = 3+2 |
| 5 | 8 | From n=4 (1 step) + From n=3 (2 steps) = 5+3 |

## Approach 1: Simple Recursion (Slow)
```python
def climbStairs(self, n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    return self.climbStairs(n - 1) + self.climbStairs(n - 2)
```

**Problem:** O(2^n) time - too slow for large n!

## Approach 2: Memoization (Fast)
```python
dp = collections.defaultdict(int)

def climbStairs(self, n: int) -> int:
    if n <= 2:
        return n
    
    if self.dp[n]:
        return self.dp[n]
    
    self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
    return self.dp[n]
```

## Approach 3: Iterative (Optimal)
```python
def climbStairs(self, n: int) -> int:
    if n <= 2:
        return n
    
    prev2, prev1 = 1, 2
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1
```

**O(n) time, O(1) space!**

## Complexity Analysis

| Approach | Time | Space |
|----------|------|-------|
| Recursion | O(2^n) | O(n) stack |
| Memoization | O(n) | O(n) |
| Iterative | O(n) | O(1) |

## Key Insights
1. **Recurrence relation:** `f(n) = f(n-1) + f(n-2)`
2. **Base cases:** `f(1) = 1`, `f(2) = 2`
3. **Fibonacci pattern:** This is Fibonacci shifted by 1 position
4. **Generalization:** Can extend to k different step sizes
5. **Real-world:** Counting paths, combinations, partitions
