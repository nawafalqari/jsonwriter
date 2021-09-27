# Easy JSON Writer
Easy package to write JSON files

## About
`jsonwriter` is an easy JSON writer, when i say easy i mean super easy
##### Made by <a href="https://nawaf.cf">Nawaf Alqari<a> in 2021

## Installation 
### PIP
```bash
npm install brain.js
```

## Examples
##### names.json
```json
{
   "name": "Nawaf",
   "age": 10
}
```

```python
from jsonwriter import file

db = file('names.json')

print(db.get('name')) # Nawaf
print(db.get('age')) # 10

db.set('age', 30, indent=None) # {"name": "Nawaf", "age": 30}
db.set('age', 30, indent=3)
'''
{
    "name": "Nawaf",
    "age": 30
}
'''

print(db.hasKey('name')) # True
print(db.hasValue('Nawaf')) # True

print(db.hasAll('name')) # True
print(db.hasAll('Nawaf')) # True

print(db.keys) # ['name', 'age']
print(db.values) # ['Nawaf', 30]
```
