import constants
import random

message = input('Enter a message to encrypt:\n--> ')

output = ''

#encrypt
for letter in message:
    code_letter = constants.encrypted[constants.decrypted.index(letter)]
    if len(code_letter) == 2:
        code_letter = random.choice(constants.rounds) + code_letter[1]
#        code_letter = '0' + code_letter[1]
    output += code_letter



#insert bonus double rounds for "fun"
for i in range(len(output), -1, -1):
    if random.randint(1, 5) == 1:
        #assert output[:i] + output[i:] == output
        output = output[:i] + random.choice(constants.rounds) + random.choice(constants.rounds) + output[i:] #inserts 2 random round chars



#insert bonus spaces for more 'fun'
counter = len(output)
while True:
    myInt = random.choice(constants.word_sizes)
    counter -= myInt
    if counter < 0: break
    output = output[:counter] + ' ' + output[counter:]
    #print(myInt,counter)



print('Here is the encrypted message:')
print(output)