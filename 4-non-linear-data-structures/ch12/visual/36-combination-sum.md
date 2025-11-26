# Q36: Combination Sum

## Problem Description
Given an array of distinct integers and a target, return all unique combinations where the chosen numbers sum to target. The same number may be used **unlimited times**.

## Core Idea: Backtracking with Repetition
**Approach:** Try each candidate, allowing reuse of the same element. Track remaining target.

## How It Works (Layman''s Terms)

Imagine: **Making Change with Unlimited Coins**
- You have coin denominations (candidates)
- Find all ways to make exact change for target
- Can use same coin multiple times

Example: candidates=[2,3,6,7], target=7
```
2 → 2 → 2 → 2 (sum=8, too big, backtrack)
2 → 2 → 2 (need 1 more, no valid option)
2 → 2 → 3 = 7 ✓
2 → 3 → 3 (sum=8, too big)
3 → 3 (need 1 more, no valid option)
7 = 7 ✓
```
Result: [[2,2,3], [7]]

## Visualization

👉 [Interactive Visualization (HTML)](./36-combination-sum.html)

## Core Code Logic

```python
def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])  # i, not i+1 (reuse allowed)
            path.pop()

    backtrack(0, [], target)
    return result
```

## Complexity

- **Time:** O(n^(target/min)) - exponential in worst case
- **Space:** O(target/min) - recursion depth

## Key Takeaways

1. **Reuse allowed** - backtrack(i, ...) not backtrack(i+1, ...)
2. **Pruning** - stop when remaining < 0
3. **Start index** - prevents duplicate combinations like [2,3] and [3,2]
