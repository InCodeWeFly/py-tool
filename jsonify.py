from flask import Flask, jsonify
import json



print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

def getUsers():
    print("Using jsonify")
    users = {'id': 1, 'username': 'sweety'}
    #return jsonify({'users': users})
    return "ok!"



print(getUsers())















