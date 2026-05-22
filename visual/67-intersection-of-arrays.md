# 67. Intersection of Two Arrays

## Problem Description
Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result must be unique.

## Layman's Explanation
Imagine two groups of people with numbered jerseys:
- **Team 1:** Players wearing #1, #2, #2, #1
- **Team 2:** Players wearing #2, #2

**Question:** Which jersey numbers appear in BOTH teams?

**Answer:** Just #2! (Even though multiple players wear #2, we only list it once)

**Three Ways to Solve:**

1. **Brute Force:** Check every player in Team 1 against every player in Team 2 (slow!)
2. **Binary Search:** Sort Team 2, then use `bisect_left` to search each Team 1 number
3. **Two Pointers:** Sort both lists and walk through them together

[View v1: brute force](./67-intersection-v1-brute-force.html) | [View v2: binary search](./67-intersection-v2-binary-search.html) | [View v3: two pointers](./67-intersection-v3-two-pointers-set.html)

## Algorithm Walkthrough
Given: `nums1 = [1, 2, 2, 1]`, `nums2 = [2, 2]`

### Solution 1: Brute Force (used in code)
```
For each n1 in nums1:
    For each n2 in nums2:
        If n1 == n2: add to result set
```
- Check 1 against [2, 2] → no match
- Check 2 against [2, 2] → match! Add 2
- Check 2 against [2, 2] → match! (2 already in set)
- Check 1 against [2, 2] → no match

**Result:** `{2}` ✓

### Solution 2: Binary Search (`67-2.py`)
```python
result = set()
nums2.sort()
for n1 in nums1:
    i2 = bisect.bisect_left(nums2, n1)
    if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
        result.add(n1)
return result
```
- Sort `nums2` once
- For each `n1`, find the first possible matching index with `bisect_left`
- Add `n1` only when that index is in range and equal to `n1`

**Result:** `[2]` ✓

### Solution 3: Two Pointers (`67-3.py`)
```python
nums1.sort()
nums2.sort()
i = j = 0
while i < len(nums1) and j < len(nums2):
    if nums1[i] > nums2[j]:
        j += 1
    elif nums1[i] < nums2[j]:
        i += 1
    else:
        result.add(nums1[i])
        i += 1
        j += 1
return result
```

## Code Explanation
```python
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    result: Set = set()  # Use set to avoid duplicates
    
    for n1 in nums1:
        for n2 in nums2:
            if n1 == n2:
                result.add(n1)  # add() handles duplicates
    
    return result  # Can also return list(result)
```

**Binary-search solution:**
```python
import bisect

def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    result: Set = set()
    nums2.sort()
    for n1 in nums1:
        i2 = bisect.bisect_left(nums2, n1)
        if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
            result.add(n1)

    return result
```

## Complexity Analysis
**Brute Force:**
- **Time Complexity:** O(n × m) - Check every pair
- **Space Complexity:** O(min(n, m)) - Result set size

**Binary Search:**
- **Time Complexity:** O(m log m + n log m) - Sort `nums2`, then search each value in `nums1`
- **Space Complexity:** O(min(n, m)) - Result set

**Two Pointers:**
- **Time Complexity:** O(n log n + m log m) - Sort both arrays, then scan once
- **Space Complexity:** O(min(n, m)) - Result set

## Key Insights
1. **Set for Uniqueness:** Using a set automatically handles duplicates
2. **Binary Search:** Sorting one array lets us test membership with `bisect_left`
3. **Two-Pointer Alternative:** Sorting both arrays lets us scan both lists together
4. **Uniqueness:** All three implemented solutions use a set for the final unique result
