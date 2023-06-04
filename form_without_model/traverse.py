import json


def loadJSON():
    file = open(
        "C:/Users/katew/OneDrive/Desktop/chimp/working_with_forms/form_without_model/item.json"
    )
    item = json.load(file)
    file.close()
    return item


def traverse(obj):
    if type(obj) == dict:
        objType = "dict"
        return obj, objType
    elif type(obj) == list:
        objType = "list"
        return obj, objType
    else:
        objType = "string"
        return obj, objType


def newPath(obj, choice):
    index = int(choice.dict()["index_choice"]) - 1
    if type(obj) == dict:
        newPath = list(obj.values())[index]
        return newPath
    elif type(obj) == list:
        newPath = obj[index]
        return newPath
    else:
        return obj
