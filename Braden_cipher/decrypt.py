#something

with open('Braden_cipher/card.txt', 'r') as file:
    encrypted = file.read().upper()

myGuess = "Dear Connor, I hope you have a ".upper()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


for letterCode, letterGuess in zip(encrypted, myGuess):
    print(letterCode, letterGuess)
    if letterCode in alphabet:
        print(alphabet.index(letterCode) - alphabet.index(letterGuess))
    else:
        print('not letter')