# Question 15: Reverse Linked List

## Layman's Explanation
We have a linked list pointing in one direction: `A -> B -> C -> D`. We want to reverse all the arrows so it becomes `D -> C -> B -> A`.

### How the Algorithm Works (Solution 15-1)
We use recursion to "unwind" the chain:
1.  **Go to the End:** Recurse down to the last node.
2.  **Flip Arrows:** As we return from each recursive call, we flip the `next` pointer of each node to point to the previous node.
3.  **New Head:** The last node becomes the new head of the reversed list.

## Visualization
I have created an interactive visualization to help you see how arrows flip one by one.

[View v1: recursive](./15-reverse-linked-list-v1-recursive.html) | [View v2: iterative](./15-reverse-linked-list-v2-iterative.html)

*(Open the HTML file in your browser to interact with the visualization)*
