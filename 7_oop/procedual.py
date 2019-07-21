# -*- coding: utf-8 -*
"""
this script is encoded with UTF-8 and contains non ASCII codes, so specify it for python2
"""

animals = [{"name": "cat"}, {"name": "dog"}, {"name": "horse"}]

for animal in animals:
    """
    各動物に合わせた処理を、各動物を表すデータの定義とは異なる場所に記述する。
    →離れれば離れるほどバグの温床になる
    →動物の種類が増えるとif文地獄になる
    """
    if not "name" in animal:
        print("???")
    elif animal["name"] == "cat":
        print("meow")
    elif animal["name"] == "dog":
        print("bowwow")
    elif animal["name"] == "horse":
        print("neigh")
    else:
        print("???")
