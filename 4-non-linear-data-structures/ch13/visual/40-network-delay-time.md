# Q40: Network Delay Time

## Problem Description
Given a network of n nodes and weighted directed edges representing signal travel times, find how long it takes for a signal sent from node k to reach all nodes. Return -1 if impossible.

## Core Idea: Dijkstra''s Algorithm
**Approach:** Find shortest paths from source to all nodes using a priority queue. Answer is the maximum of all shortest distances.

## How It Works (Layman''s Terms)

Imagine: **Broadcasting a Message**
- Signal spreads from source node
- Each edge has a travel time (weight)
- Signal reaches each node via the fastest path
- Total time = when the last node receives the signal

Example: times=[[2,1,1],[2,3,1],[3,4,1]], n=4, k=2
```
Node 2 (source): distance = 0
Node 2 → Node 1: distance = 1
Node 2 → Node 3: distance = 1
Node 3 → Node 4: distance = 2
```
Maximum distance = 2

## Visualization

👉 [Interactive Visualization (HTML)](./40-network-delay-time.html)

## Core Code Logic

```python
def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    dist = {}
    heap = [(0, k)]  # (distance, node)

    while heap:
        d, node = heapq.heappop(heap)
        if node in dist:
            continue
        dist[node] = d

        for neighbor, weight in graph[node]:
            if neighbor not in dist:
                heapq.heappush(heap, (d + weight, neighbor))

    return max(dist.values()) if len(dist) == n else -1
```

## Complexity

- **Time:** O(E log V) - each edge processed once, heap operations
- **Space:** O(V + E) - graph and heap storage

## Key Takeaways

1. **Dijkstra''s algorithm** - shortest paths from single source
2. **Priority queue** - always process closest unvisited node
3. **Check reachability** - all n nodes must be reachable
