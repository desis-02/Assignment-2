Purpose
The Password Generator allows users to generate either memorable or random passwords, tailored to their needs. The memorable passwords consist of a series of English words with appended random digits, while random passwords are generated from a customizable set of characters (letters, digits, and optionally symbols). Each generated password is logged to a file along with the timestamp of when it was created.

Features
- Memorable Password: Concatenates randomly selected English words with appended digits, joined by hyphens.
- Random Password: Generates a password from a customizable pool of characters, including upper/lower case letters, digits, and symbols.
- Passwords are saved to separate files, depending on their type (Memorable or Random), along with the date and time of creation.
- Automatically creates the necessary directories ("Memorable" or "Random") if they don't exist.

How to Use
1. Generating a Password: 
   Call the `generate_password` method with the type (`memorable` or `random`) and the relevant parameters:
   - For memorable passwords, provide the number of words (`n_words`) and an optional case option (`case`), which can be `'lower'`, `'upper'`, or `'title'`.
   - For random passwords, provide the length of the password (`length`), whether to include punctuation (`include_punctuation`), and any characters you want to disallow (`disallowed_chars`).

2. Saving the Password:
   Once the password is generated, it is automatically saved to a file in the respective directory along with the time of creation.

3. Batch Testing:
   To generate multiple passwords, use the `generate_batch_passwords` function. It will randomly alternate between generating memorable and random passwords.

Input/Output
Input
- Memorable Password: Requires `n_words` and optional `case` parameter.
- Random Password: Requires `length`, optional `include_punctuation`, and optional `disallowed_chars`.

Output
- Passwords are saved to `Generated_Passwords.txt` files in "Memorable" or "Random" directories.

Libraries Used
- `random`: For generating random numbers, characters, and word selections.
- `os`: For checking and creating directories.
- `string`: For handling character sets in random password generation.
- `datetime`: For logging the date and time of password creation.
