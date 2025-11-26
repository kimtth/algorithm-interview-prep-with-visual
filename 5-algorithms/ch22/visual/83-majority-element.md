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

### Approach 2: Hash Map
Use a dictionary to count occurrences.
Time: O(n), Space: O(n)

### Approach 3: Sorting
Sort the array, the middle element is always the majority.
```
[2, 2, 1, 1, 1, 2, 2] → sorted → [1, 1, 1, 2, 2, 2, 2]
                                          ↑
                                        middle
```
Time: O(n log n), Space: O(1)

### Approach 4: Boyer-Moore Voting Algorithm
The clever O(n) time, O(1) space solution!

**Intuition:** If we had one +1 vote for the majority and -1 for everyone else, majority wins.

```
nums = [2, 2, 1, 1, 1, 2, 2]

candidate = None, count = 0

2: count=0 → candidate=2, count=1
2: candidate=2 → count=2
1: candidate≠1 → count=1
1: candidate≠1 → count=0
1: count=0 → candidate=1, count=1
2: candidate≠2 → count=0
2: count=0 → candidate=2, count=1

Result: 2
```

### Approach 5: Divide and Conquer
Split array in half, find majority in each half, the true majority is one of them.

```
[2,2,1,1,1,2,2]
     /        \
[2,2,1]    [1,1,2,2]
   2           ?
```
Recursively find majority in subarrays, verify winner.

## Code Explanation

### Brute Force
```python
def majorityElement(self, nums: List[int]) -> int:
    for num in nums:
        if nums.count(num) > len(nums) // 2:
            return num
```

### Boyer-Moore
```python
def majorityElement(self, nums: List[int]) -> int:
    count = 0
    candidate = None
    
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    
    return candidate
```

## Complexity Analysis
| Approach | Time | Space |
|----------|------|-------|
| Brute Force | O(n²) | O(1) |
| Hash Map | O(n) | O(n) |
| Sorting | O(n log n) | O(1) |
| Boyer-Moore | O(n) | O(1) |
| Divide & Conquer | O(n log n) | O(log n) |

## Key Insights
1. **Boyer-Moore:** Treats array like an election; majority cancels out minority
2. **Sorting:** Majority must occupy middle position
3. **Divide & Conquer:** True majority is majority in at least one half
4. **Guaranteed existence:** Problem guarantees majority exists (simplifies solution)
