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
2. **Using Sets:** Convert both teams to "unique number sets" and find the overlap (fast!)
3. **Two Pointers:** Sort both lists and walk through them together (efficient for sorted data)

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

### Solution 2: Using Sets (more Pythonic)
```python
return list(set(nums1) & set(nums2))
```
- set(nums1) = {1, 2}
- set(nums2) = {2}
- Intersection = {2}

**Result:** `[2]` ✓

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

**One-liner using set intersection:**
```python
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1) & set(nums2))
```

## Complexity Analysis
**Brute Force:**
- **Time Complexity:** O(n × m) - Check every pair
- **Space Complexity:** O(min(n, m)) - Result set size

**Set Intersection:**
- **Time Complexity:** O(n + m) - Build two sets and intersect
- **Space Complexity:** O(n + m) - Two sets

## Key Insights
1. **Set for Uniqueness:** Using a set automatically handles duplicates
2. **Python Set Operations:** `&` operator computes intersection efficiently
3. **Trade-offs:** Brute force is simple but slow; set approach uses more space but is faster
4. **Two-Pointer Alternative:** If arrays are sorted, use two pointers for O(n + m) time, O(1) extra space
