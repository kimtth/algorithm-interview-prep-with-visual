# 75. Sliding Window Maximum

## Problem Description
Given an array `nums` and sliding window size `k`, return the maximum value in each window as it slides from left to right.

## Layman's Explanation
Imagine looking through a window that only shows `k` consecutive elements at a time. The window slides one position right each step. For each position, we report the biggest number visible through the window.

**Example:** `nums = [1, 3, -1, -3, 5, 3, 6, 7]`, `k = 3`

```
Window positions:           Max:
[1  3  -1] -3  5  3  6  7    3
 1 [3  -1  -3] 5  3  6  7    3
 1  3 [-1  -3  5] 3  6  7    5
 1  3  -1 [-3  5  3] 6  7    5
 1  3  -1  -3 [5  3  6] 7    6
 1  3  -1  -3  5 [3  6  7]   7
```

**Result:** `[3, 3, 5, 5, 6, 7]`

## Algorithm Walkthrough

### Approach 1: Brute Force
For each window position, find the maximum by scanning all k elements.
- Simple but O(n×k) time

### Approach 2: Optimized with Deque
Use a deque (double-ended queue) to maintain useful elements:
1. **Remove smaller elements:** If a new element is larger, previous smaller elements can never be the max while this element is in the window
2. **Remove old elements:** Pop elements that have left the window
3. **Front is always max:** The deque front is always the maximum for current window

**Walkthrough with nums = [1, 3, -1, -3, 5], k = 3:**

| Step | Window | Deque (indices) | Deque (values) | Max |
|------|--------|-----------------|----------------|-----|
| 0    | [1]    | [0]             | [1]            | -   |
| 1    | [1,3]  | [1]             | [3]            | -   |
| 2    | [1,3,-1] | [1,2]         | [3,-1]         | 3   |
| 3    | [3,-1,-3]| [1,2,3]       | [3,-1,-3]      | 3   |
| 4    | [-1,-3,5]| [4]           | [5]            | 5   |

**Why keep smaller elements?**  
When -1 enters, 3 might leave soon. If 3 leaves, -1 could become the new max. So we keep -1 behind 3.

## Code Explanation

### Solution 1: Brute Force
```python
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    if not nums:
        return nums
    
    result = []
    for i in range(len(nums) - k + 1):
        result.append(max(nums[i:i + k]))  # O(k) for each window
    return result
```

### Solution 2: Deque Optimization
```python
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    results = []
    window = collections.deque()
    current_max = float('-inf')
    
    for i, v in enumerate(nums):
        window.append(v)
        if i < k - 1:
            continue
        
        # Update max if new value is larger
        if current_max == float('-inf'):
            current_max = max(window)
        elif v > current_max:
            current_max = v
        
        results.append(current_max)
        
        # Reset max if it slides out
        if current_max == window.popleft():
            current_max = float('-inf')
    
    return results
```

## Complexity Analysis
- **Brute Force:** O(n×k) time, O(1) space
- **Deque Approach:** O(n) time (each element added/removed once), O(k) space

## Key Insights
1. **Deque stores candidates:** Only potentially useful maximum candidates are kept
2. **Monotonic decreasing:** Deque values are in decreasing order; front is always max
3. **Index tracking:** Store indices to know when elements leave the window
4. **Lazy recalculation:** Only recalculate max when the current max leaves the window
