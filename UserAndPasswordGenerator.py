# Random User Generation
import random
import string
import dotenv
from pathlib import Path
count = 0
def generate_random_alphanumeric(length, count):
    # Combine letters and digits from the string module constants
    characters = string.ascii_letters + string.digits
    # Use random.choices for Python 3.6+ (more efficient) or a generator expression
    random_string = ''.join(random.choices(characters, k=length))
    count += 1
    return random_string
length = 10 #Set passwords to 10 digits/characters
password = generate_random_alphanumeric(length, count)
print(password)

user = f'PASSWORD_FOR_{count}'
env_path = dotenv.find_dotenv()
dotenv.load_dotenv()
dotenv.set_key(env_path, user, password)