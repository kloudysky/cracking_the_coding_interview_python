from abc import ABC, abstractclassmethod
from datetime import datetime

class Entry(ABC):
    def __init__(self, name, parent) -> None:
        self.__name = name
        self.__parent = parent
        self.__createdAt = datetime.now()        
        self.__updatedAt = datetime.now()        
        self.__lastAccessedAt = datetime.now()    

    def deleteEntry(self):
        if self.__parent == None:
            return False
        self.__parent.deleteEntry(self)

    def getFullPath(self):
        return self.__parent.getFullPath() + "/" + f"{self.__name}"

    @abstractclassmethod
    def size(self):
        pass

    #getters and setters
    def getCreatedAt(self):
        return self.__createdAt

    def getUpdatedAt(self):
        return self.__updatedAt

    def getLastAccessedAt(self):
        return self.__lastAccessedAt
    
    def changeName(self, newName: str):
        self.__name = newName

    def getName(self):
        return self.__name

class File(Entry):
    def __init__(self, name, parent) -> None:
        super().__init__(name, parent)
        self.__content = ""

    def size(self):
        return len(self.__content)

    def setContent(self, content):
        self.__content = content

    def getContent(self):
        return self.__content

    def __str__(self):
        return f"{self.getName()}:"

class Directory(Entry):
    def __init__(self, name, parent) -> None:
        super().__init__(name, parent)
        self.__entries = []

    def size(self):
        size = 0
        for entry in self.__entries:
            size += entry.size()
        return size

    def addEntry(self, entry):
        return self.__entries.append(entry)

    def deleteEntry(self, entry):
        return self.__entries.remove(entry)

    def getEntries(self):
        return self.__entries

    def __str__(self):
        return f"{self.getName()}:"

    def __iter__(self):
        return iter(self.__entries)

root = Directory("root", None)
note = File("This is a file", root)
root.addEntry(note)
folder = Directory("folder", root)
root.addEntry(folder)
newFolder = Directory("new folder", folder)
folder.addEntry(newFolder)
print(folder)
for entry in root:
    print(entry)
