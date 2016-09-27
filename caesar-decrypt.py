string = raw_input('What text would you like decrypted? ').lower()
shift = int(raw_input('How much was the shift on the cipher? '))
cipher = ''
for x in range(len(string)):
    y = ord(string[x]) - shift
    cipher += chr(y)
print cipher
