# Question 1: Valid Palindrome

## Layman's Explanation
A **palindrome** is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

**Examples:**
- "racecar" -> "racecar" (It is a palindrome)
- "A man, a plan, a canal: Panama" -> "amanaplanacanalpanama" (It is a palindrome)
- "hello" -> "olleh" (Not a palindrome)

### How the Algorithm Works (Solution 1-1)
1.  **Cleaning:** First, we take the input text and remove anything that isn't a letter or a number. We also convert all uppercase letters to lowercase. This gives us a clean list of characters.
2.  **Comparing Ends:** We look at the very first character and the very last character of our clean list.
3.  **Matching:**
    -   If they are **different**, we know immediately it's not a palindrome. We stop and say "False".
    -   If they are the **same**, we remove both of them from the list (or just move our focus inwards).
4.  **Repeating:** We repeat step 2 and 3 with the remaining characters.
5.  **Conclusion:** If we successfully check all pairs without finding a mismatch, then it is a palindrome. We say "True".

## Visualization
I have created an interactive visualization to help you see this process in action.

[Open Visualization (1-valid-palindrome.html)](./1-valid-palindrome.html)

*(Open the HTML file in your browser to interact with the visualization)*
