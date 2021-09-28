# JSON Writer
Easy package to write JSON files

## About
`jsonwriter` is an easy JSON writer, when i say easy i mean super easy
##### Made by <a href="https://nawaf.cf">Nawaf Alqari<a> in 2021

## Installation 
### PIP
```bash
pip install jsonwriter
```

## Examples
### Initialize your file:
#### If you want to autosave every change you make
```python
from jsonwriter import file
file = file('names.json', autosave=True)
```

#### If you don't want to autosave them just set autosave to False
```python
from jsonwriter import file
file = file('names.json', autosave=False) # Whenever you want to save just add file.save() after it
file.set('name', 'Khayal')
file.save() # <---
                   
# By the way if you want to see your changes to the file before saving them you can use
file.content() # {'name': 'Khayal'}
```

##### names.json
```json
{
   "name": "Nawaf",
   "age": 10
}
```

```python
from jsonwriter import file

file = file('names.json', autosave=True)
                   
print(file.get('name')) # Nawaf
print(file.get('age')) # 10

# Recommended indent is 3, to make it more readable
file.set('age', 30, indent=0) # {"name": "Nawaf", "age": 30}
file.set('age', 30, indent=3)
                   

# {
#     "name": "Nawaf",
#     "age": 30
# }
                   
file.remove('name') # This will remove any key from the file

# {
#     "age": 30
# }

file.content() # This will return the file content or all the changes you made if you are not using autosave
                   
print(file.hasKey('name')) # True
print(file.hasValue('Nawaf')) # True

print(file.hasAll('name')) # True
print(file.hasAll('Nawaf')) # True

# This will return a list of all keys in your file
print(file.keys()) # ['name', 'age']

# This will return a list of all values in your file
print(file.values()) # ['Nawaf', 30]

file.clear() # This will remove every key and value in the file
# {}
                   
# This will work only if you are not using autosave
file.save() # This will save every changes you made
```
