# 80. Task Scheduler

## Problem Description
Given tasks (represented by letters) and a cooling time `n`, find the minimum time to complete all tasks. The same task must have at least `n` intervals between executions.

## Layman's Explanation
Imagine you're a CPU running tasks. After running a task, you must wait `n` cycles before running the **same** task again. You can run different tasks or stay idle during cooling.

**Example:** `tasks = ["A","A","A","B","B","B"]`, `n = 2`

```
A must wait 2 cycles before next A
B must wait 2 cycles before next B

Schedule: A → B → idle → A → B → idle → A → B
          1   2    3     4   5    6     7   8

Total time: 8
```

**Strategy:** Schedule the most frequent tasks first to minimize idle time!

## Algorithm Walkthrough
Given: `tasks = ["A","A","A","B","B","B"]`, `n = 2`

**Count tasks:** A=3, B=3

**Each cycle can run n+1 = 3 tasks before repeating**

| Cycle | Slot 1 | Slot 2 | Slot 3 |
|-------|--------|--------|--------|
| 1     | A(3→2) | B(3→2) | idle   |
| 2     | A(2→1) | B(2→1) | idle   |
| 3     | A(1→0) | B(1→0) | -      |

**Total:** 3 cycles × 3 slots = 8 (last cycle doesn't need trailing idle)

## Code Explanation
```python
def leastInterval(self, tasks: List[str], n: int) -> int:
    counter = collections.Counter(tasks)
    result = 0

    while True:
        sub_count = 0
        # Pick n+1 most common tasks
        for task, _ in counter.most_common(n + 1):
            sub_count += 1
            result += 1
            counter.subtract(task)
            # Remove zeros
            counter += collections.Counter()

        if not counter:
            break

        # Add idle time if we couldn't fill the cycle
        result += n - sub_count + 1

    return result
```

**Key insight:** Each "round" is `n+1` slots. Fill with most common tasks, rest is idle.

## Formula Approach
For the most frequent task with count `max_count`:

```
minimum_time = (max_count - 1) × (n + 1) + count_of_max_tasks
```

**Why?**
- `max_count - 1` full cycles with `n+1` slots each
- Last cycle only needs tasks with maximum frequency

**Example:** A=3, B=3, n=2
- `(3-1) × (2+1) + 2 = 2 × 3 + 2 = 8`

But if we have more tasks than idle slots, just return `len(tasks)`.

## Complexity Analysis
- **Time Complexity:** O(n × m) where m is distinct task count
- **Space Complexity:** O(1) - At most 26 letters

## Key Insights
1. **Greedy selection:** Always run the most frequent available task
2. **Cooling constraint:** Same task needs n gaps between runs
3. **Idle slots:** Fill remaining slots in each n+1 cycle with idle
4. **Dense case:** If tasks > idle slots, answer is just task count
5. **Frequency matters:** High-frequency tasks determine the schedule structure
