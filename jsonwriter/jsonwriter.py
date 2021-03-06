''' Made by Nawaf Alqari https://nawaf.cf in 2021 '''

from json import load, dump
from json.decoder import JSONDecodeError

class NotJsonFileError(Exception):
    pass

class file:
    def __init__(self, filepath:str, autosave:bool=True):
        '''
        Open file\nfile must be JSON
        '''
        self.__filepath = filepath
        self.__autosave = autosave
        try:
            with open(self.__filepath, 'r') as fileFile:
                self.__fileData = load(fileFile)
                if not self.__filepath.endswith('.json'):
                    raise NotJsonFileError('File must be json')
                self.content = self.__fileData
                self.keys = [key for key, value in self.__fileData.items()]
                self.values = [value for key, value in self.__fileData.items()]
        except JSONDecodeError:
            with open(self.__filepath, 'w') as fileFile:
                dump({}, fileFile)
            with open(self.__filepath, 'r') as fileFile:
                self.__fileData = load(fileFile)
                if not self.__filepath.endswith('.json'):
                    raise NotJsonFileError('File must be json')
                self.content = self.__fileData
                self.keys = [key for key, value in self.__fileData.items()]
                self.values = [value for key, value in self.__fileData.items()]
    # Setter function
    def save(self, indent:int=3):
        '''
        save your data to the file\n
        indent=3 (recommended)
        '''
        with open(self.__filepath, 'w') as fileFile:
            if indent == 0:
                return dump(self.__fileData, fileFile, indent=None)
            return dump(self.__fileData, fileFile, indent=indent)
    # Getter function
    def get(self, key):
        '''
        Return value of the specified key\n
        returns None if the key does not exist 
        '''
        if key in self.__fileData: return self.__fileData[key]
        else: None
    # Setter function
    def set(self, key, value, indent:int=3, encryption:bool=False) -> None:
        '''
        Set or update something in the file\n
        indent=3 (recommended)
        '''
        # self.__fileData[enc.encode(key)] = enc.encode(value)
        self.__fileData[key] = value
        if self.__autosave == True:
            with open(self.__filepath, 'w') as fileFile:
                if indent == 0:
                    return dump(self.__fileData, fileFile, indent=None)
                return dump(self.__fileData, fileFile, indent=indent)
    # Setter function
    def remove(self, key, indent=3) -> None:
        '''
        Remove a key in the file\n
        indent=3 (recommended)
        '''
        del self.__fileData[key]
        if self.__autosave == True:
            with open(self.__filepath, 'w') as fileFile:
                if indent == 0: return dump(self.__fileData, fileFile, indent=None)
                return dump(self.__fileData, fileFile, indent=indent)
    # Setter function
    def clear(self) -> None:
        '''
        WARNING!! This will remove everything in the json file
        '''
        for i in self.__fileData.copy():
            del self.__fileData[i]
        if self.__autosave == True:
            with open(self.__filepath, 'w') as fileFile:
                return dump(self.__fileData, fileFile)
    def hasKey(self, key) -> bool:
        if key in self.__fileData: return True
        return False
    def hasValue(self, value) -> bool:
        for ikey, ivalue in self.__fileData.items():
            if value == ivalue: return True
        return False
    def hasAll(self, keyOrValue) -> bool:
        for ikey, ivalue in self.__fileData.items():
            if keyOrValue == ikey or keyOrValue == ivalue: return True
        return False
