import random
import os
import string
from datetime import datetime

class PasswordGenerator:
    def __init__(self):
        # Load the top English nouns for memorable password
        try:
            with open('top_english_nouns_lower_100000.txt', 'r') as file:
                self.words = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print("Error: The file 'top_english_nouns_lower_100000.txt' was not found.")
            self.words = []
        
    def generate_password(self, password_type, **kwargs):
        if password_type == "memorable":
            return self._generate_memorable_password(kwargs['n_words'], kwargs.get('case', 'lower'))
        elif password_type == "random":
            return self._generate_random_password(kwargs['length'], kwargs.get('include_punctuation', True), kwargs.get('disallowed_chars', ''))
        else:
            raise ValueError("Invalid password type. Choose 'memorable' or 'random'.")

    def _generate_memorable_password(self, n_words, case):
        chosen_words = [random.choice(self.words) for _ in range(n_words)]
        # Append a random digit to each word
        chosen_words = [word + str(random.randint(0, 9)) for word in chosen_words]
        # Apply the requested case
        if case == 'lower':
            chosen_words = [word.lower() for word in chosen_words]
        elif case == 'upper':
            chosen_words = [word.upper() for word in chosen_words]
        elif case == 'title':
            chosen_words = [word.capitalize() for word in chosen_words]
        # Join the words with a hyphen
        password = '-'.join(chosen_words)
        return password

    def _generate_random_password(self, length, include_punctuation=True, disallowed_chars=''):
        character_pool = string.ascii_letters + string.digits
        if include_punctuation:
            character_pool += string.punctuation
        # Remove any disallowed characters from the pool
        character_pool = ''.join([ch for ch in character_pool if ch not in disallowed_chars])
        # Generate the random password
        password = ''.join(random.choice(character_pool) for _ in range(length))
        return password

    def save_password(self, password_type, password):
        # Get the current date and time
        current_time = datetime.now().strftime("%A, %B %d, %Y %H:%M:%S")
        # Define the directory and file path
        directory = password_type.capitalize()  # 'Memorable' or 'Random'
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_path = os.path.join(directory, 'Generated_Passwords.txt')
        # Append the password and time to the file
        with open(file_path, 'a') as file:
            file.write(f"{password} - Generated on: {current_time}\n")

# Testing the generator by creating 1000 passwords
def generate_batch_passwords(n):
    generator = PasswordGenerator()
    for _ in range(n):
        password_type = random.choice(['memorable', 'random'])
        if password_type == 'memorable':
            password = generator.generate_password(password_type, n_words=4, case=random.choice(['lower', 'upper', 'title']))
        else:
            password = generator.generate_password(password_type, length=random.randint(8, 16), include_punctuation=True)
        generator.save_password(password_type, password)
    print(f"Generated {n} passwords successfully.")

# Generate 1000 passwords
generate_batch_passwords(1000)