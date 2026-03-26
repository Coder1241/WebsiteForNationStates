# Random User Generation
import random
import string
import dotenv
from pathlib import Path
import os
from dotenv import load_dotenv
def generate_random_alphanumeric(length, count):
    # Combine letters and digits from the string module constants
    characters = string.ascii_letters + string.digits
    # Use random.choices for Python 3.6+ (more efficient) or a generator expression
    random_string = ''.join(random.choices(characters, k=length))
    count += 1
    return random_string
length = 10 #Set passwords to 10 digits/characters
count = 0
for i in range(2):
    password = generate_random_alphanumeric(length, count)
    print(password)
    user = f'PASSWORD_FOR_{count}'
    env_path = dotenv.find_dotenv()
    dotenv.load_dotenv()
    username = os.getenv(user)
    #Checks for dupes
    if username is not None:
        count +=1
        user = f'PASSWORD_FOR_{count}'
    with open('users.txt', 'a') as userfile:
        userfile.write(user + '\n')
    with open('.env', 'a') as envfile:
        envfile.write(f"{user}='{password}'\n")
