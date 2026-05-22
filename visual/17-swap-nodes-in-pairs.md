# Question 17: Swap Nodes in Pairs

## Layman's Explanation
We have a linked list and we want to swap every two adjacent nodes. For example:
-   `1 -> 2 -> 3 -> 4` becomes `2 -> 1 -> 4 -> 3`

### How the Algorithm Works (Solution 17-1)
This solution takes a shortcut: instead of swapping the actual node connections (which is complex), we simply **swap the values** inside the nodes.
1.  Take two nodes at a time.
2.  Swap their values.
3.  Move to the next pair.

## Visualization
I have created an interactive visualization to help you see the pairwise swapping.

[View v1: value swap](./17-swap-nodes-in-pairs-v1-value-swap.html) | [View v2: node swap](./17-swap-nodes-in-pairs-v2-node-swap.html) | [View v3: recursive](./17-swap-nodes-in-pairs-v3-recursive.html)

*(Open the HTML file in your browser to interact with the visualization)*
