from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import random

def improveFilename(name):
    name = name[0:-3]
    return name

def createFile(title, content):
    path = f"Files/{title}.md"

    if default_storage.exists(path):
        return False
    default_storage.save(path, ContentFile(content))  
    return True

def saveFile(title, content):
    path = f"Files/{title}.md"

    if default_storage.exists(path):
        default_storage.delete(path)
    default_storage.save(path, ContentFile(content))  

def getFile(title):
    path = f"Files/{title}.md"
    if default_storage.exists(path):
        return default_storage.open(path).read().decode("utf-8")
    else:
        return None

def totalFiles():
    direc, filenames = default_storage.listdir("Files")
    impfilenames = sorted(map(improveFilename,filenames))
    return impfilenames            

def randomFile():
    filenames = totalFiles()
    return random.choice(filenames)
