# 83. Majority Element

## Problem Description
Given an array `nums` of size n, find the majority element (appears more than n/2 times). The majority element always exists.

## Layman's Explanation
Find the number that appears more than half the time in the array.

**Example:** `nums = [3, 2, 3]`
- 3 appears 2 times (2 > 3/2 = 1.5) ✓
- 2 appears 1 time (1 ≤ 1.5) ✗

**Result:** 3

## Algorithm Approaches

### Approach 1: Brute Force Counting
Count occurrences of each element, return the one with count > n/2.
```python
for num in nums:
    if nums.count(num) > len(nums) // 2:
        return num
```
Time: O(n²), Space: O(1)

### Approach 2: Hash Map Cache
Cache each distinct element's `nums.count(num)` result in a dictionary.
Time: O(n²) worst case because each new value can trigger a full count, Space: O(n)

### Approach 3: Divide and Conquer
Split array in half, find majority in each half, the true majority is one of them.

```
[2,2,1,1,1,2,2]
      /        \
[2,2,1]    [1,1,2,2]
    2           ?
```
Recursively find majority in subarrays, then verify the winner.
Time: O(n log n), Space: O(log n)

### Approach 4: Sorting
Sort the array, the middle element is always the majority.
```
[2, 2, 1, 1, 1, 2, 2] → sorted → [1, 1, 1, 2, 2, 2, 2]
                                                        ↑
                                                     middle
```
Time: O(n log n), Space: O(1)

## Code Explanation

### Brute Force
```python
def majorityElement(self, nums: List[int]) -> int:
    for num in nums:
        if nums.count(num) > len(nums) // 2:
            return num
```

### Hash Map Cache
```python
def majorityElement(self, nums: List[int]) -> int:
    counts = collections.defaultdict(int)
    for num in nums:
        if counts[num] == 0:
            counts[num] = nums.count(num)

        if counts[num] > len(nums) // 2:
            return num
```

### Divide and Conquer
```python
def majorityElement(self, nums: List[int]) -> int:
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]

    half = len(nums) // 2
    a = self.majorityElement(nums[:half])
    b = self.majorityElement(nums[half:])

    return [b, a][nums.count(a) > half]
```

### Sorting
```python
def majorityElement(self, nums: List[int]) -> int:
    return sorted(nums)[len(nums) // 2]
```

## Complexity Analysis
| Approach | Time | Space |
|----------|------|-------|
| Brute Force | O(n²) | O(1) |
| Hash Map Cache | O(n²) worst case | O(n) |
| Divide & Conquer | O(n log n) | O(log n) |
| Sorting | O(n log n) | O(1) |

## Key Insights
1. **Brute force:** Directly checks the problem definition with `nums.count`
2. **Hash map cache:** Avoids repeated counts for values already seen
3. **Divide & Conquer:** True majority is majority in at least one half
4. **Sorting:** Majority must occupy middle position
5. **Guaranteed existence:** Problem guarantees majority exists (simplifies solution)
