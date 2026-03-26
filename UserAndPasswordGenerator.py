# Random User Generation
import random
import string
import dotenv
from pathlib import Path
import os
from dotenv import load_dotenv
def generate_random_alphanumeric(length):
    # Combine letters and digits from the string module constants
    characters = string.ascii_letters + string.digits
    # Use random.choices for Python 3.6+ (more efficient) or a generator expression
    random_string = ''.join(random.choices(characters, k=length))
    return random_string
length = 10 #Set passwords to 10 digits/characters
count = 1
times = int(input("How many accounts do you want to generate? "))
dotenv.load_dotenv()
for i in range(times):
    password = generate_random_alphanumeric(length)
    print(password)
    user = f'PASSWORD_FOR_{count}'
    env_path = dotenv.find_dotenv()
    username = os.getenv(user)
    #Checks for dupes
    while username is not None:
        count +=1
        user = f'PASSWORD_FOR_{count}'
        username = os.getenv(user)
    with open('.env', 'a') as envfile:
        envfile.write(f"{user}='{password}'\n")
with open('users.txt', 'w') as e:
        e.write(f'{count}')