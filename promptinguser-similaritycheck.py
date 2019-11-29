import json

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data(w)
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter the word: ")

print(translate(word))

# get_close_matches("themandalorian", data.keys(), cutoff=0.5)