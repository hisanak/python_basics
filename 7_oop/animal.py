# -*- coding: utf-8 -*
"""
this script is encoded with UTF-8 and contains non ASCII codes, so specify it for python2
"""

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def get_sound(self):
        return self.sound

animals = [
    Animal("cat", "meow"),
    Animal("dog", "bowwow"),
    Animal("horse", "neigh")
]

for animal in animals:
    """
    classを用いるともっとシンプルになることも
    Animalクラスかどうか、Animalクラスがget_soundを持っているかの検査はお好みで
    あまり真面目にやっても遅くなるだけです
    """
    assert isinstance(animal, Animal)

    print(animal.get_sound())

