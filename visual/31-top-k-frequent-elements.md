# Q31: Top K Frequent Elements

## Problem Description
Given an integer array, return the **k most frequent** elements. Answer can be in any order.

## Core Idea: Heap or Bucket Sort
**Approach 1:** Use a min-heap of size k to track top k frequent elements.
**Approach 2:** Use bucket sort where index = frequency.

## How It Works (Layman''s Terms)

**Heap Approach:** Tournament for Top K
- Count votes for each candidate (frequency)
- Keep a "finalist pool" of size k
- If new candidate has more votes than the weakest finalist, swap them

**Bucket Approach:** Sorting by Popularity
- Create buckets numbered 1 to n (possible frequencies)
- Place each element in bucket matching its count
- Read from highest bucket until k elements collected

Example: nums = [1,1,1,2,2,3], k = 2
- Counts: {1:3, 2:2, 3:1}
- Bucket: [[], [3], [2], [1], [], [], []]
- Read from end: bucket[3]=[1], bucket[2]=[2] → result: [1, 2]

## Visualization

👉 [Interactive Visualization (HTML)](./31-top-k-frequent-elements.html)

## Core Code Logic

```python
# Pythonic solution using Counter
def topKFrequent(nums: List[int], k: int) -> List[int]:
    return [x for x, _ in Counter(nums).most_common(k)]

# Bucket sort solution
def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    bucket = [[] for _ in range(len(nums) + 1)]

    for num, freq in count.items():
        bucket[freq].append(num)

    result = []
    for i in range(len(bucket) - 1, 0, -1):
        for num in bucket[i]:
            result.append(num)
            if len(result) == k:
                return result
```

## Complexity

- **Heap:** O(n log k) time, O(n) space
- **Bucket Sort:** O(n) time, O(n) space

## Key Takeaways

1. **Counter.most_common()** - Python built-in for frequency problems
2. **Bucket sort** - O(n) when range is bounded
3. **Min-heap for top-k** - keeps only k elements in memory
