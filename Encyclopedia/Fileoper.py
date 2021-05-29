from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def createFile(title, content):
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
    return len(filenames)            