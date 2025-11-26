# 66. Search in Rotated Sorted Array

## Problem Description
You are given a rotated sorted array (originally sorted, then rotated at some pivot). Search for a target value. Return its index if found, or -1 if not.

Example: `[0,1,2,4,5,6,7]` rotated at pivot 4 becomes `[4,5,6,7,0,1,2]`

## Layman's Explanation
Imagine a circular necklace of beads numbered 1-10. If you cut it and lay it flat, you might get:
`[7, 8, 9, 10, 1, 2, 3, 4, 5, 6]`

The numbers are "mostly" sorted, but there's a "break point" (between 10 and 1).

**The Strategy:**
1. **Find the pivot** (the smallest element) - this is where the rotation happened
2. **Use modified binary search** - adjust indices by the pivot offset

It's like having a map that's rotated - once you know the rotation angle, you can read it correctly!

## Algorithm Walkthrough
Given: `nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 0`

**Phase 1: Find the Pivot (minimum element)**
```
Array: [4, 5, 6, 7, 0, 1, 2]
        L        M        R
        0        3        6
```
- mid = 3, nums[3] = 7 > nums[6] = 2
- Minimum is in RIGHT half → left = mid + 1 = 4

```
Array: [4, 5, 6, 7, 0, 1, 2]
                    L  M  R
                    4  5  6
```
- mid = 5, nums[5] = 1 < nums[6] = 2
- Minimum is in LEFT half → right = mid = 5

```
Array: [4, 5, 6, 7, 0, 1, 2]
                    LMR
                    4
```
- left = right = 4 → **Pivot found at index 4!**

**Phase 2: Binary Search with Pivot Offset**
- Use virtual indices: `mid_pivot = (mid + pivot) % len(nums)`
- Search as if array is `[0, 1, 2, 4, 5, 6, 7]` (unwrapped)

```
Virtual:  [0, 1, 2, 4, 5, 6, 7]
           0  1  2  3  4  5  6
Actual:   [4, 5, 6, 7, 0, 1, 2]
           4  5  6  0  1  2  3  (indices after pivot mapping)
```

- left=0, right=6, mid=3 → mid_pivot = (3+4)%7 = 0
- nums[0] = 4 > 0 → search left (right = mid-1 = 2)
- left=0, right=2, mid=1 → mid_pivot = (1+4)%7 = 5
- nums[5] = 1 > 0 → search left (right = mid-1 = 0)
- left=0, right=0, mid=0 → mid_pivot = (0+4)%7 = 4
- nums[4] = 0 == target → **FOUND at index 4!**

## Code Explanation
```python
def search(self, nums: List[int], target: int) -> int:
    if not nums:
        return -1
    
    # Phase 1: Find pivot (minimum element)
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[right]:
            left = mid + 1  # Minimum in right half
        else:
            right = mid  # Minimum in left half (including mid)
    
    pivot = left
    
    # Phase 2: Binary search with pivot offset
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_pivot = (mid + pivot) % len(nums)  # Map to actual index
        
        if nums[mid_pivot] < target:
            left = mid + 1
        elif nums[mid_pivot] > target:
            right = mid - 1
        else:
            return mid_pivot
    
    return -1
```

## Complexity Analysis
- **Time Complexity:** O(log n) - Two binary searches: O(log n) + O(log n)
- **Space Complexity:** O(1) - Only pointer variables

## Key Insights
1. **Two-Phase Approach:** First find pivot, then search with offset
2. **Pivot Finding:** The minimum element reveals the rotation point
3. **Index Mapping:** `(mid + pivot) % n` converts virtual to actual index
4. **Why it works:** After rotation, array is two sorted halves - pivot tells us how to "unwrap" it
