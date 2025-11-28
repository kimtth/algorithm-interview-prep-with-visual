# Question 13: Palindrome Linked List

## Layman's Explanation
A **linked list** is like a chain of boxes, where each box contains a value and a pointer to the next box. We want to check if the values in this chain read the same forwards and backwards (like a palindrome).

### How the Algorithm Works (Solution 13-1)
1.  **Convert to List:** We walk through the linked list and copy all values into a regular Python list (array).
2.  **Check Palindrome:** Now we have a simple list. We compare the first and last elements, remove them if they match, and repeat until the list is empty or we find a mismatch.

## Visualization
I have created an interactive visualization to help you see how the linked list is converted and checked.

[Open Visualization (13-palindrome-linked-list.html)](./13-palindrome-linked-list.html)

*(Open the HTML file in your browser to interact with the visualization)*
