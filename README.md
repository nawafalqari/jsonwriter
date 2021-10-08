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
##### <small>If you set autosave to `True` every change you make will be automatically saved</small>
```python
from jsonwriter import file
file = file('filename.json', autosave=True)

file.set('key', 'value') # This will be saved automatically 
```

##### <small>If you don't use autosave you have to add `file.save()` whenever you want to save your changes</small>

```python
from jsonwriter import file
file = file('filename.json', autosave=False)

file.set('key', 'value')
file.set('key2', 'value2')
file.save() # Now, it will be saved
```

### <small>Functions</small>

Let's say this is our file content:
```json
{
   "name": "Nawaf",
   "age": 10
}
```

get(key)
```python
file.get('name') # Will return Nawaf
file.get('age') # Will return 10
```
set(key, value)
```python
file.set('Skills', ['Sleeping', 'Coding'], indent=3)
# indentation will make it more readable
# 3 is recommended/default value

# set() Can also update values
file.set('age', 100)
```
File will get updated to
```json
{
   "name": "Nawaf",
   "age": 100,
   "Skills": [
      "Sleeping",
      "Coding"
   ]
}
```
If we set the indentation to `0` this is what we will get
```json
{"name": "Nawaf", "age": 100, "Skills": ["Sleeping", "Coding"]}
```
remove(key)
```python
file.remove('name') # This will just remove "name": "Nawaf"
```
clear()
```python
file.clear() # Warning! This will remove everything from your file
```
hasKey(key)
```python
file.hasKey('age') # return True
```
hasValue(value)
```python
file.hasValue(10) # return True
```
hasAll(key or value)
```python
file.hasAll('age') # return True
file.hasAll(10) # return True
```
### <small>Attributes</small>
```python
from jsonwriter import file
file = file('filename.json', autosave=True)

print(file.content)
# This will show your file content
# Note: if you are not using autosave this will show all the changes, even if they are not saved

print(file.keys)
# This will show all the keys

print(file.values)
# This will show all the values

```
