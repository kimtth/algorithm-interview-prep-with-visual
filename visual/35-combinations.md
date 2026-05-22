# Q35: Combinations

## Problem Description
Given two integers n and k, return all possible combinations of k numbers chosen from range [1, n].

## Core Idea: Backtracking
**Approach:** Build combinations by choosing elements in order (to avoid duplicates), stopping when k elements are selected.

## How It Works (Layman''s Terms)

Imagine: **Selecting Team Members**
- Choose k people from n candidates
- Order doesn''t matter: {1,2} = {2,1}
- To avoid duplicates, always pick in increasing order

Example: n=4, k=2
```
Start with 1 → add 2 → [1,2] ✓
           → add 3 → [1,3] ✓
           → add 4 → [1,4] ✓
Start with 2 → add 3 → [2,3] ✓
           → add 4 → [2,4] ✓
Start with 3 → add 4 → [3,4] ✓
```

## Visualization

[View v1: dfs](./35-combinations-v1-dfs.html) | [View v2: itertools](./35-combinations-v2-itertools.html)

## Core Code Logic

```python
def combine(n: int, k: int) -> List[List[int]]:
    result = []

    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return

        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1, [])
    return result
```

## Complexity

- **Time:** O(C(n,k) × k) - C(n,k) combinations, O(k) to copy each
- **Space:** O(k) - recursion depth

## Key Takeaways

1. **Combination = order doesn''t matter** - {1,2} = {2,1}
2. **Start index prevents duplicates** - only pick larger numbers
3. **C(n,k) = n! / (k!(n-k)!)** - binomial coefficient
