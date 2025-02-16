#Python Program to Check Whether a Character is Alphabet or Not


def check_alphabet(char):
    if char.isalpha():
        return True
    else:
        return False
        
alpha = input("Enter a character: ")
checker = check_alphabet(alpha)

if checker:
    print("{} is an alphabet".format(alpha))
   # print("the character is alphabet")
else:
    print("{} is not an alphabet".format(alpha))
     #print("the character is no alphabet alphabet")
