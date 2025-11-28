# Question 2: Reverse String

## Layman's Explanation
The goal is to reverse a list of characters (like a word) in place. This means we modify the original list directly without creating a new one.

### How the Algorithm Works (Solution 2-1)
1.  **Pointers:** We place one finger (pointer) at the **start** of the list and another finger at the **end** of the list.
2.  **Swapping:** We swap the characters at these two positions. The character at the start goes to the end, and the character at the end goes to the start.
3.  **Moving Inwards:** We move the left finger one step to the right, and the right finger one step to the left.
4.  **Repeating:** We repeat the swapping and moving until our fingers meet in the middle or cross each other.
5.  **Result:** The entire list is now reversed.

## Visualization
I have created an interactive visualization to help you see this process in action.

[Open Visualization (2-reverse-string.html)](./2-reverse-string.html)

*(Open the HTML file in your browser to interact with the visualization)*
