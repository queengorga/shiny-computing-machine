import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif (get_close_matches(w, data.keys())) > 0:
        return "Did you mean %s instead?" % get_close_matches(w, data.keys()) [0]
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter the word: ")

print(translate(word))

# get_close_matches("themandalorian", data.keys(), cutoff=0.5)