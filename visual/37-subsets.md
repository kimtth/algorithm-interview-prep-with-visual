# Q37: Subsets

## Problem Description
Given an integer array of unique elements, return all possible subsets (the power set). Must not contain duplicate subsets.

## Core Idea: Backtracking (Include/Exclude)
**Approach:** For each element, make a binary choice: include it or exclude it.

## How It Works (Layman''s Terms)

Imagine: **Packing a Bag**
- For each item, decide: pack it or leave it
- Each combination of decisions = one subset
- 2^n total possibilities

Example: [1, 2, 3]
```
Include 1? Yes → Include 2? Yes → Include 3? Yes → [1,2,3]
                                            No  → [1,2]
                           No  → Include 3? Yes → [1,3]
                                            No  → [1]
          No  → Include 2? Yes → Include 3? Yes → [2,3]
                                            No  → [2]
                           No  → Include 3? Yes → [3]
                                            No  → []
```

## Visualization

👉 [Interactive Visualization (HTML)](./37-subsets.html)

## Core Code Logic

```python
def subsets(nums: List[int]) -> List[List[int]]:
    result = []

    def backtrack(start, path):
        result.append(path[:])  # Add current subset

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result
```

## Complexity

- **Time:** O(n × 2^n) - 2^n subsets, O(n) to copy each
- **Space:** O(n) - recursion depth

## Key Takeaways

1. **Power set** - all possible subsets including empty and full
2. **2^n subsets** - each element has 2 choices (in or out)
3. **Add at every node** - not just at leaves
