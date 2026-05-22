# Q34: Permutations

## Problem Description
Given an array of distinct integers, return all possible permutations in any order.

## Core Idea: Backtracking
**Approach:** Build permutations by choosing each unused element at each position, then recurse.

## How It Works (Layman''s Terms)

Imagine: **Arranging People in a Line**
- Pick any person for position 1
- Pick any remaining person for position 2
- Continue until all positions filled
- Backtrack to try different arrangements

Example: [1, 2, 3]
```
Position 1: choose 1 → Position 2: choose 2 → Position 3: choose 3 → [1,2,3]
                                            → backtrack
                       → Position 2: choose 3 → Position 3: choose 2 → [1,3,2]
→ backtrack all the way
Position 1: choose 2 → ...
```

## Visualization

[View v1: dfs](./34-permutations-v1-dfs.html) | [View v2: itertools](./34-permutations-v2-itertools.html)

## Core Code Logic

```python
def permute(nums: List[int]) -> List[List[int]]:
    result = []

    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return

        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i+1:])
            path.pop()

    backtrack([], nums)
    return result
```

## Complexity

- **Time:** O(n! × n) - n! permutations, O(n) to copy each
- **Space:** O(n) - recursion depth

## Key Takeaways

1. **Permutation = ordering matters** - [1,2] ≠ [2,1]
2. **Track used elements** - via remaining list or visited set
3. **n! results** - grows very fast!
