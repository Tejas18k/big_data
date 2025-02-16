# Python Program to Check Whether an Alphabet is Vowel or Consonant


def vowelornot(char1):
    if char1 == 'a' or char1 == 'e' or char1 == 'i' or char1=='o' or char1=='u':
   
        return "vowel"
        
    else:
        return "consonant"
    
char=input("enter the character :")
print(vowelornot(char))



#--------------------------------------------------------
'''
def check_vowel_or_consonant(char): #4th,inside fun defination
    vowels = 'aeiouAEIOU'        #5th
    if char in vowels:           #6th
        return "vowel"           #7th
    else:                        #8th
        return "consonant"       #9th

char = input("Enter an alphabet: ")     # 1st, execution start from here

# Make sure user enters a single alphabet
if len(char) == 1 and char.isalpha():    # 2nd, line of execution if condtion ok go to next 
    result = check_vowel_or_consonant(char) # 3rd, call check_vowel_or_consonant go to fn defination
    print("{} is a {}".format(char, result)) #10th print the result
else:
    print("Please enter a single alphabet.") #11 condition fails then this line will print at the end
    
'''make sure user enters a single alphabet
if len(char) == 1 and char.isalpha():    # 2nd, line of execution if condtion ok go to next 
    result = check_vowel_or_consonant(char) # 3rd, call check_vowel_or_consonant go to fn defination
    print("{} is a {}".format(char, result)) #10th print the result
else:
    print("Please enter a single alphabet.") #11 condition fails then this line will print at the end
    
'''
