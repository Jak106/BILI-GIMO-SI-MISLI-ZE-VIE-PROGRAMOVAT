alphabet = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0
}

with open("frequency_table.txt") as f:
    text = f.read()

text = text.lower()

print(text)

for letter in text:
    try:
        alphabet[letter] += 1
    except:
        continue

for key in alphabet:
    print(f'{key.upper()} - {alphabet[key]}')

print("THESE LETTERS DID NOT APPEAR IN THE TEXT AT ALL ")
for key in alphabet:
    if alphabet[key] == 0:
        print(f'{key.upper()};')