# Problem 55: Kth Largest Element in an Array

## Visualization
[View Interactive Visualization](./55-kth-largest.html)

## Problem Statement
Given an integer array nums and an integer k, return the kth largest element in the array. Note that it is the kth largest element in sorted order, not the kth distinct element.

## Layman's Explanation
Imagine a competition where you want to find who came in k-th place. Instead of sorting everyone (expensive!), use a **heap** - a special data structure that always keeps the smallest (or largest) element on top. With a **max-heap**, we can pop elements k-1 times to get to the k-th largest.

Alternatively, with a **min-heap** of size k, we push all elements and only keep the k largest. The top of this heap is the k-th largest!

## Step-by-Step Walkthrough (Max-Heap Approach)
1. **Build Max-Heap**: Insert all elements (negated for Python's min-heap)
2. **Pop k-1 Times**: Remove the largest k-1 elements
3. **Return Top**: The next pop gives the k-th largest

## Visual Example
```
nums = [3, 2, 1, 5, 6, 4], k = 2

Max-Heap (built):    [6, 5, 4, 2, 3, 1]
Pop 1st largest:     6  → [5, 3, 4, 2, 1]
Pop 2nd largest:     5  ← This is k-th largest!

Answer: 5
```

## Code Snippet (Max-Heap)
```python
def findKthLargest(self, nums: List[int], k: int) -> int:
    heap = list()
    for n in nums:
        heapq.heappush(heap, -n)  # Negate for max-heap

    for _ in range(1, k):
        heapq.heappop(heap)

    return -heapq.heappop(heap)
```

## Alternative: heapq.nlargest
```python
def findKthLargest(self, nums: List[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]
```

## Complexity Analysis
- **Time Complexity**: O(n log n) for heap approach, O(n + k log n) for nlargest
- **Space Complexity**: O(n) for storing the heap
