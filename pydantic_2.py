from typing import List

from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int

person = Person(name='John', age=20)
js = person.model_dump_json(indent=2)
print(js)

with open('person.json', 'w') as f:
    f.write(js)


