Purpose: This project generates memorable and random passwords based on user preferences. It can create passwords with words and numbers or fully randomized character strings. Generated passwords are saved automatically.
How to use it: 
- Load the list of words into the program
- Memorable Password: The code will select random words from the list and add a random digit to the word. Format words with lowercase, or uppercase and joins them together with hyphens
- Random Password: Picks random numbers, letters and symbols (if allowed) and can exclude characters if needed
- Stores passwords and includes timestamps for reference 
Input: A list of 100,000 top english words
Output: Memorable and random passwords based on the list of words
Libraries used: 
- random
- os
- string
- datetime
