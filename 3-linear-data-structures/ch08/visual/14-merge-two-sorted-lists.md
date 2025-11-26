# Question 14: Merge Two Sorted Lists

## Layman's Explanation
We have two sorted linked lists (chains of numbers in order). We want to merge them into one single sorted linked list.

### How the Algorithm Works (Solution 14-1)
This uses **recursion** - the function calls itself to solve smaller parts of the problem.
1.  **Compare Heads:** Look at the first node of each list.
2.  **Pick Smaller:** The smaller one becomes the head of our merged list.
3.  **Recurse:** We then merge the rest of that list with the other list (the part we didn't pick from).
4.  **Base Case:** When one list is empty, we just attach the other list.

## Visualization
I have created an interactive visualization to help you see how two lists merge step by step.

[Open Visualization (14-merge-two-sorted-lists.html)](./14-merge-two-sorted-lists.html)

*(Open the HTML file in your browser to interact with the visualization)*
