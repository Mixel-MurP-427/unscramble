import json
with open("./Sharp_cipher/frequency.json", "r") as file_obj:
    word_sizes = json.load(file_obj)

print(len(word_sizes))

condensed = {}

#assemble:
for i in range(20):
    condensed[i] = 0

for num in word_sizes:
    condensed[num] += 1

print(condensed)