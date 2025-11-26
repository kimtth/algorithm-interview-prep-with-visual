# Q39: Course Schedule

## Problem Description
There are n courses labeled 0 to n-1. Given prerequisites as pairs [a, b] meaning you must take course b before course a, determine if you can finish all courses.

## Core Idea: Cycle Detection in Directed Graph
**Approach:** Model as a graph where edges represent dependencies. If a cycle exists, courses cannot be completed.

## How It Works (Layman''s Terms)

Imagine: **Class Registration Requirements**
- Some classes require prerequisites
- If A requires B, and B requires C, and C requires A → impossible!
- Need to detect such circular dependencies

Example: numCourses=2, prerequisites=[[1,0]]
- Course 1 requires course 0
- Take 0 first, then 1 → possible! ✓

Example: numCourses=2, prerequisites=[[1,0],[0,1]]
- Course 1 requires 0, Course 0 requires 1
- Circular dependency → impossible! ✗

## Visualization

👉 [Interactive Visualization (HTML)](./39-course-schedule.html)

## Core Code Logic

```python
def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    # 0: unvisited, 1: visiting, 2: visited
    state = [0] * numCourses

    def hasCycle(course):
        if state[course] == 1:  # Currently visiting → cycle!
            return True
        if state[course] == 2:  # Already completed
            return False

        state[course] = 1
        for next_course in graph[course]:
            if hasCycle(next_course):
                return True
        state[course] = 2
        return False

    for course in range(numCourses):
        if hasCycle(course):
            return False
    return True
```

## Complexity

- **Time:** O(V + E) - visit each node and edge once
- **Space:** O(V + E) - graph storage and recursion

## Key Takeaways

1. **Topological sort problem** - can also use Kahn''s algorithm (BFS)
2. **Three states** - unvisited, visiting (in current path), visited
3. **Cycle = visiting node again** - while still in the current DFS path
