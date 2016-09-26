# This way works, but is too easy!

# string = raw_input("Give me a string to reverse please\n:")
# print string [::-1]

string = "Hello"
char_list = []

for i in range(len(string) - 1, - 1, - 1):
    char list.append(string[i])

#
output = ' '.join(char_list)
print output
