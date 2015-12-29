from os import getcwd, path
from os.path import isfile
from dotenv import load_dotenv

dirName = getcwd()

for _ in range(5): 
    dotenv_path = path.join(dirName, '.env')
    if (isfile(dotenv_path)): 
        break
    dirName = path.join(dirName, '..')

load_dotenv(dotenv_path)
