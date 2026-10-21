from typing import TypedDict

class Person(TypedDict):

    name: str
    age:int

#new dictionay create
new_person: Person =  {'name':'nitish', 'age':45}

print(new_person)