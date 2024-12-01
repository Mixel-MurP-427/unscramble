# This repo is for my message encryption and decryption programs.
There are currently 4 different subfolders, each with a different message encryption type.

### Wingfeather
All this code was created for the sole purpose of unscrambling the letters "KLNCUOHTDEITEHOCW". I found the letters from a certain page (34) in a certain book (Wingfeather Tales by Andrew Peterson and other authors). After who knows how many weeks of effort, I finally unscrambled the letters into "unlock with the code".

### Eli_Cipher
This is some code I wrote to help me crack my friend's substitution cipher. constants.py contains the substitution key, translate.py actually does the substitution, and reorder.py takes specific strings and reorganizes the letters, because apparently my friend thought it wasn't enough to just use substitution for his code.

## The next two types of encryption I wrote to get revenge on my friend. I sent him some messages in the mail using these types.

### Pi_Cipher
This message encoding system is simple: just add the consecutive digits of Pi to the letters in your message. To encrypt "Hello World!", H+3=**K**, e+1=**f**, etc. until you get "Kfpmt Fqxqg!"

### Sharp_Cipher
This encryption system is a bit more complicated. "Round" letters are letters whose uppercase form contains a curve. They are represented in the key as "0". Round characters act like a shift key, changing the sharp letters into something else. In a coded message, "K" by itself means "a", but when preceded by any round letter it is "D". Whitespace characters in a coded message mean nothing, and a double "0" cancels out.

## Concerning the singleFile_versions branch:
This branch was created for the convenience of non-coders. Everything you need to encrypt or decrypt a message is contained in a single file, as opposed to having a constants file, input file, output file, etc.
