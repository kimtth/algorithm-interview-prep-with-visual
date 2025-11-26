# Problem 59: Merge Intervals

## Visualization
[View Interactive Visualization](./59-merge-intervals.html)

## Problem Statement
Given an array of intervals where intervals[i] = [start, end], merge all overlapping intervals and return an array of non-overlapping intervals.

## Layman's Explanation
Imagine you have multiple meeting times on a calendar, and some overlap. You want to combine overlapping meetings into single blocks. First **sort by start time**, then go through each meeting: if it overlaps with the previous merged block (starts before the block ends), extend that block. Otherwise, start a new block.

## Step-by-Step Walkthrough
1. **Sort**: Order intervals by start time
2. **Initialize**: Add first interval to merged list
3. **For Each Interval**: 
   - If overlaps with last merged (start ≤ last.end), extend last.end
   - Otherwise, add as new interval
4. **Return**: The merged list

## Visual Example
```
Input: [[1,3], [2,6], [8,10], [15,18]]

After sorting: [[1,3], [2,6], [8,10], [15,18]]

Step 1: merged = [[1,3]]
Step 2: [2,6] overlaps [1,3] → merge to [[1,6]]
Step 3: [8,10] no overlap → [[1,6], [8,10]]
Step 4: [15,18] no overlap → [[1,6], [8,10], [15,18]]
```

## Code Snippet
```python
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    merged = []
    for i in sorted(intervals, key=lambda x: x[0]):
        if merged and i[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], i[1])
        else:
            merged += i,
    return merged
```

## Complexity Analysis
- **Time Complexity**: O(n log n) - dominated by sorting
- **Space Complexity**: O(n) - for storing merged intervals
