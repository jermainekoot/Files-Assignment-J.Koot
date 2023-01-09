__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


import os
import glob
import zipfile 
from importlib.resources import contents

def clean_cache():
    cwd = os.getcwd()
    cwd = os.path.join(cwd, 'files')
    cache_name = 'cache'
    cache = os.path.join(cwd, cache_name)
        
    if not os.path.exists(cache):    
        os.mkdir(cache)
        return 'cache created'
    elif os.path.exists(cache):
        cache = os.path.join(cache, '*')
        cache = glob.glob(cache)
        for files in cache:
            os.remove(files)
        return 'existing cache was cleaned'

print(clean_cache())
    
def cache_zip(file_path, cache_path):
    zip = zipfile.ZipFile(file_path)
    zip.extractall(cache_path)
    return 'Unzipped file to cache'

data = os.path.join(os.getcwd(), 'files', 'data.zip')
cache_location = os.path.join(os.getcwd(), 'files', 'cache')

print(cache_zip(data, cache_location))

def cached_files():
    cache = os.path.join(os.getcwd(), 'files', 'cache')
    files = [os.path.join(cache, f) for f in os.listdir(cache) if 
    os.path.isfile(os.path.join(cache, f))]
    return files

def find_password(cached_files):
    for file in cached_files:

        f_contents = open(file, 'r')
        contents = f_contents.read()
        f_contents.close()
        if 'pass' in contents:
            password_location = contents.find('password')
            start = contents.find(' ', password_location) +1
            end = contents.find('\n', password_location) 
            return contents[start:end]


print(find_password(cached_files()))