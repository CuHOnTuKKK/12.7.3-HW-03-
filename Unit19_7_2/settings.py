import os
from dotenv import load_dotenv
import random
import string


load_dotenv()
valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')


no_valid_email = os.getenv('valid_email')
no_valid_password = os.getenv('valid_password')


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", rand_string)