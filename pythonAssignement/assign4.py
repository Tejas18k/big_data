#Python Program to Find ASCII Value of a character
'''
char = input("Enter a character: ")

# Manually get ASCII value
if 'a' <= char <= 'z':
    ascii_value = ord('a') + (ord(char) - ord('a'))
elif 'A' <= char <= 'Z':
    ascii_value = ord('A') + (ord(char) - ord('A'))
elif '0' <= char <= '9':
    ascii_value = ord('0') + (ord(char) - ord('0'))
else:
    ascii_value = ord(char)

print("The ASCII value of '{}' is {}".format(char, ascii_value))
'''

#

def get_ascii_value(char):
    return ord(char)

character = input("Enter a character: ")
ascii_value = get_ascii_value(character)
print("The ASCII value of '{}' is {}".format(character, ascii_value))

