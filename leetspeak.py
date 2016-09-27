# A => 4
# E => 3
# G => 6
# I => 1
# O => 0
# S => 5
# T => 7

string = raw_input('What would you like to translate?\n:').upper()

leet = ''

for x in range(len(string)):
    if string[x] == "A":
        leet += "4"
    elif string[x] == "E":
        leet += "3"
    elif string[x] == "G":
        leet += "6"
    elif string[x] == "I":
        leet += "1"
    elif string[x] == "O":
        leet += "0"
    elif string[x] == "S":
        leet += "5"
    elif string[x] == "T":
        leet += "7"
    else:
        leet += string[x]
print leet
