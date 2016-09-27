string = raw_input('What text would you like encrypted? ').lower()
shift = int(raw_input('How much should the shift on the cipher be? '))
def encrypt(string, shift):
    cipher = ''
    for x in range(len(string)):
        y = ord(string[x]) + shift
        cipher += chr(y)
    print cipher
def decrypt(string, shift):
    cipher = ''
    for x in range(len(string)):
        y = ord(string[x]) - shift
        cipher += chr(y)
    print cipher
