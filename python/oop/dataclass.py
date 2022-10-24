from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

    def __post_init__(self):
        if self.age < 0:
            raise ValueError('Age cannot be negative')

    def __str__(self):
        return f'{self.name} is {self.age} years old'


@dataclass
class Vector:
    x: float
    y: float
    z: float = 0.0

    def __post_init__(self):
        if self.z == 0:
            self.z = self.x + self.y

    def __str__(self):
        return f'Vector({self.x}, {self.y}, {self.z})'


'''
By using dataclasses, we can create classes with less boilerplate code.
Basically, the dataclasses module provides a decorator and functions for automatically adding generated special methods such as __init__ and __repr__ to user-defined classes.
'''