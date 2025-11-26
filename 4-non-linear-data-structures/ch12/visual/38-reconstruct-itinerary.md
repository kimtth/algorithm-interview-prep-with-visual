# Q38: Reconstruct Itinerary

## Problem Description
Given a list of airline tickets as [from, to] pairs, reconstruct the itinerary starting from "JFK". If multiple valid itineraries exist, return the one with the smallest lexical order.

## Core Idea: Eulerian Path + DFS
**Approach:** Use DFS with Hierholzer''s algorithm. Visit edges in lexical order, backtrack when stuck, build path in reverse.

## How It Works (Layman''s Terms)

Imagine: **Planning a Trip Using All Tickets**
- Must use every ticket exactly once
- Start from JFK
- When multiple destinations available, pick alphabetically smallest
- If stuck, backtrack and try different route

Example: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
```
JFK → ATL (alphabetically first)
ATL → JFK
JFK → SFO (only option left from JFK)
SFO → ATL
ATL → SFO (last ticket)
```
Result: ["JFK","ATL","JFK","SFO","ATL","SFO"]

## Visualization

👉 [Interactive Visualization (HTML)](./38-reconstruct-itinerary.html)

## Core Code Logic

```python
def findItinerary(tickets: List[List[str]]) -> List[str]:
    graph = defaultdict(list)
    for src, dst in sorted(tickets, reverse=True):
        graph[src].append(dst)

    route = []
    def dfs(airport):
        while graph[airport]:
            dfs(graph[airport].pop())
        route.append(airport)

    dfs("JFK")
    return route[::-1]
```

## Complexity

- **Time:** O(E log E) - sorting edges
- **Space:** O(E) - storing edges and recursion

## Key Takeaways

1. **Eulerian path** - visit every edge exactly once
2. **Hierholzer''s algorithm** - build path in reverse
3. **Sort reverse + pop** - get lexically smallest efficiently
