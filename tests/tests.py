import __init__ as jsonWriter

db = jsonWriter.file('tests.json')

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