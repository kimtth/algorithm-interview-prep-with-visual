# 64. K Closest Points to Origin

## Problem Description
Given an array of points where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin (0, 0).

The distance from a point (x, y) to origin is `√(x² + y²)`.

## Layman's Explanation
Imagine you're standing at the center of a field (the origin 0,0), and there are markers scattered around. You want to find the k markers that are closest to you.

**The Strategy:**
1. Calculate how far each marker is from you
2. Use a **heap (priority queue)** to efficiently track the k closest ones
3. Heaps are great for this because they can quickly give you the smallest/largest items

**Two Approaches:**
1. **Min-Heap:** Put ALL distances in, pop k times → O(n log n)
2. **Max-Heap of size k:** Keep only k closest at any time → O(n log k)

The solution uses a min-heap: push all points with their distances, then pop k times.

## Algorithm Walkthrough
Given: `points = [[1,3], [-2,2], [5,1], [2,-1]]`, `k = 2`

**Step 1: Calculate distances**
- Point [1,3]: distance² = 1² + 3² = 10
- Point [-2,2]: distance² = (-2)² + 2² = 8
- Point [5,1]: distance² = 5² + 1² = 26
- Point [2,-1]: distance² = 2² + (-1)² = 5

**Step 2: Build min-heap** (ordered by distance)
```
        5          ← smallest (closest)
       / \
      8   26
     /
    10
```

**Step 3: Pop k=2 times**
- Pop 1: distance=5 → point [2,-1]
- Pop 2: distance=8 → point [-2,2]

**Result:** `[[2,-1], [-2,2]]` ✓

## Code Explanation
```python
import heapq

def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    heap = []
    
    # Push all points with their squared distances
    for x, y in points:
        # Use squared distance to avoid sqrt (doesn't change ordering)
        dist = x*x + y*y
        heapq.heappush(heap, (dist, [x, y]))
    
    result = []
    # Pop k closest points
    for _ in range(k):
        result.append(heapq.heappop(heap)[1])
    
    return result
```

**Why squared distance?** 
- √a < √b if and only if a < b (for positive numbers)
- Avoiding sqrt saves computation and avoids floating-point issues

## Complexity Analysis
- **Time Complexity:** O(n log n) - Building heap is O(n), but popping k times is O(k log n), and pushing n times is O(n log n)
- **Space Complexity:** O(n) - Storing all points in the heap

**Alternative with Max-Heap of size k:**
- Time: O(n log k) - Only maintain k elements
- Space: O(k) - Only store k points

## Key Insights
1. **Heap for Top-K:** Heaps excel at finding k smallest/largest elements
2. **Squared Distance:** Skip the square root - it's monotonic and doesn't affect ordering
3. **Min-Heap vs Max-Heap:**
   - Min-heap: simple, pop k times
   - Max-heap of size k: more efficient for large n, small k
4. **Python heapq:** Is a min-heap by default; for max-heap, negate values
