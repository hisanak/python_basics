# -*- coding: utf-8 -*
"""
this script is encoded with UTF-8 and contains non ASCII codes, so specify it for python2
"""

animals = [{"name": "cat", "sound": "meow"}, {"name": "dog", "sound": "bowwow"}, {"name": "horse", "sound": "neigh"}]

for animal in animals:
    """
    各動物に合わせた処理とデータを組み合わせて定義した
    →書き方がシンプルになった
    →if文地獄にならない
    """
    if not "sound" in animal:
        print("???")
    else:
        print(animal["sound"])
