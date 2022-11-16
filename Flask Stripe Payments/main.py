import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

print('Public: ' + os.getenv('PUBLISHABLE_KEY'))
print('Secret: ' + os.getenv('SECRET_KEY'))
