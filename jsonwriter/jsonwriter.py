''' Made by Nawaf Alqari https://nawaf.cf in 2021 '''

from json import load, dump

class NotJsonFileError(Exception):
    pass

class file:
    def __init__(self, filepath:str):
        '''
        Open file, file must be JSON
        '''
        self.__filepath = filepath
        with open(self.__filepath, 'r') as fileFile:
            self.__fileData = load(fileFile)
            if not self.__filepath.endswith('.json'):
                raise NotJsonFileError('File must be json')
            self.content = self.__fileData
    def get(self, key):
        '''
        Return value of the specified key\n
        returns None if the key does not exist 
        '''
        if key in self.__fileData: return self.__fileData[key]
        else: None
    def set(self, key, value, indent:int=3):
        '''
        Set or update something in the file\n
        indent=3 (recommended)
        '''
        self.__fileData[key] = value
        with open(self.__filepath, 'w') as fileFile:
            if indent == 0:
                return dump(self.__fileData, fileFile, indent=None)
            return dump(self.__fileData, fileFile, indent=indent)
    def hasKey(self, key) -> bool:
        if key in self.__fileData: return True
        return False
    def hasValue(self, value) -> bool:
        for ikey, ivalue in self.__fileData.items():
            if value == ivalue: return True
        return False
    def hasAll(self, keyOrValue):
        for ikey, ivalue in self.__fileData.items():
            if keyOrValue == ikey or keyOrValue == ivalue: return True
        return False