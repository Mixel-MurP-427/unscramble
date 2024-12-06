#import constants
#old code above, replaced below:

str_sharps = 'AEFHIKLMNTVWXYZ'
str_rounds = 'BCDGJOPQRSU'
sharps = tuple(str_sharps)
rounds = tuple(str_rounds)
everything = tuple('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

encrypted = ('K', 'W', '0E', '0K', 'Y', '0N', 'X', 'V', '0Y', '0L', '0V', 'I', 'H', 'M', 'E', '0F', '0Z', 'F', '0I', '0X', '0H', '0W', '0A', '0M', 'L', '0T', 'N', 'A', 'T', 'Z')
decrypted = tuple('abcdefghijklmnopqrstuvwxyz.,! ')

#assemble word sizes
word_sizes_condensed = {1: 417, 2: 1005, 3: 1440, 4: 1051, 5: 723, 6: 555, 7: 454, 8: 247, 9: 142, 10: 80, 11: 35, 12: 20, 13: 17}
word_sizes = []
for size, amount in word_sizes_condensed.items():
    print(size, amount)
    word_sizes += [size]*amount



import random

message = input('Enter a message to encrypt:\n--> ')
print(message)

output = ''

#encrypt
for letter in message:
    code_letter = encrypted[decrypted.index(letter)]
    if len(code_letter) == 2:
        code_letter = random.choice(rounds) + code_letter[1]
#        code_letter = '0' + code_letter[1]
    output += code_letter



#insert bonus double rounds for "fun"
for i in range(len(output), -1, -1):
    if random.randint(1, 5) == 1:
        #assert output[:i] + output[i:] == output
        output = output[:i] + random.choice(rounds) + random.choice(rounds) + output[i:] #inserts 2 random round chars



#insert bonus spaces for more 'fun'
counter = len(output)
while True:
    myInt = random.choice(word_sizes)
    counter -= myInt
    if counter < 0: break
    output = output[:counter] + ' ' + output[counter:]
    #print(myInt,counter)



print('Here is the encrypted message:')
print(output)