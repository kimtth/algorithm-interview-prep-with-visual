# 79. Queue Reconstruction by Height

## Problem Description
People are described by a pair `[h, k]` where:
- `h` is the person's height
- `k` is the number of people **in front** who have height ≥ h

Reconstruct the queue.

## Layman's Explanation
Imagine people standing in line for a photo. Each person remembers:
- Their own height
- How many taller (or equal height) people were in front of them

The line got shuffled, and we need to reconstruct the original order!

**Example:** `people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]`

**Strategy:** Start with the tallest people first!
- Tallest people only see other tall people, so their `k` value directly tells us their position
- Insert shorter people later - they don't affect tall people's counts

## Algorithm Walkthrough
Given: `[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]`

**Step 1: Sort by height (descending), then by k (ascending)**
```
Sorted: [[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]
```

**Step 2: Insert each person at index k**

| Person | Insert at k | Queue State |
|--------|-------------|-------------|
| [7,0]  | index 0     | [[7,0]] |
| [7,1]  | index 1     | [[7,0], [7,1]] |
| [6,1]  | index 1     | [[7,0], [6,1], [7,1]] |
| [5,0]  | index 0     | [[5,0], [7,0], [6,1], [7,1]] |
| [5,2]  | index 2     | [[5,0], [7,0], [5,2], [6,1], [7,1]] |
| [4,4]  | index 4     | [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]] |

**Result:** `[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]`

## Why This Works
- **Tallest first:** When we place the tallest person, they don't need to consider shorter people (shorter people don't count toward their k)
- **Insert at k:** For the current tallest, k represents exactly how many people should be before them
- **Shorter people don't disturb taller:** When we insert a shorter person, the taller people already placed still maintain their correct k counts

## Code Explanation
```python
def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    heap = []
    # Push with negative height (for max-heap behavior)
    for person in people:
        heapq.heappush(heap, (-person[0], person[1]))
    
    result = []
    # Extract in order and insert at index k
    while heap:
        person = heapq.heappop(heap)
        result.insert(person[1], [-person[0], person[1]])
    
    return result
```

**Using heap for sorting:**
- `-person[0]`: negative for max-heap (tallest first)
- `person[1]`: breaks ties by k (lower k first)

## Complexity Analysis
- **Time Complexity:** O(n²) - n insertions, each can take O(n) in worst case
- **Space Complexity:** O(n) - for the result queue

## Key Insights
1. **Greedy order:** Process tallest to shortest
2. **Insert at k:** The k value directly gives the insertion position
3. **Invariant:** After inserting a person, all previously inserted (taller) people remain valid
4. **Tie-breaking:** Same height sorted by k ascending (smaller k first)
