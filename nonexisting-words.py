import json

data = json.load(open("data.json"))

def translate(w):
    if w in data:
    return data(word)

word = input("Enter the word: ")

print(translate(word))