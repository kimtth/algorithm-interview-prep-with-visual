# Q41: Cheapest Flights Within K Stops

## Problem Description
Find the cheapest price from source to destination with at most k stops. Return -1 if no such route exists.

## Core Idea: Modified Dijkstra / BFS with Pruning
**Approach:** Use BFS level by level (each level = one stop) or modified Dijkstra tracking both cost and stops.

## How It Works (Layman''s Terms)

Imagine: **Budget Travel Planning**
- Find cheapest flight route
- Can have at most k layovers (stops)
- Sometimes a longer route with more stops is cheaper
- But we have a limit on stops!

Example: n=3, flights=[[0,1,100],[1,2,100],[0,2,500]], src=0, dst=2, k=1
```
Direct: 0 → 2 costs 500 (0 stops)
Via 1:  0 → 1 → 2 costs 200 (1 stop)
```
With k=1, we can use 1 stop, so answer = 200

## Visualization

👉 [Interactive Visualization (HTML)](./41-cheapest-flights.html)

## Core Code Logic

```python
def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, price in flights:
        graph[u].append((v, price))

    # (cost, stops, node)
    heap = [(0, 0, src)]
    # best[node] = minimum stops to reach with some cost
    best = {}

    while heap:
        cost, stops, node = heapq.heappop(heap)

        if node == dst:
            return cost

        if stops > k:
            continue

        if node in best and best[node] <= stops:
            continue
        best[node] = stops

        for neighbor, price in graph[node]:
            heapq.heappush(heap, (cost + price, stops + 1, neighbor))

    return -1
```

## Complexity

- **Time:** O(E × k × log(E × k)) - modified Dijkstra with stop tracking
- **Space:** O(E × k) - heap can have multiple entries per node

## Key Takeaways

1. **Two constraints** - minimize cost AND limit stops
2. **Can''t use standard Dijkstra** - cheaper path might have more stops
3. **Track stops per node** - same node can be visited with different stop counts
