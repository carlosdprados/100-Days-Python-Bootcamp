#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Day 5 Project: Password Generator
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
This program will create a randomized password for you, composed of a certain number of letters, numbers, and symbols.
You will get both an EAZY PASSWORD and a HARD PASSWORD. The difference is that the order of characters is randomised in the latter:
This means that different character types will be mixed together seamlessly (g#2jk8&P vs. having a more simplistic gjkP#&28).
You can choose how many characters of each kind you want, but you must have at least 1 of each type. Websites these days...
The program is protected against both misinputs and requesting a super high number of characters.
"""
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '=']

print("Welcome to the PyPassword Generator!\n")
nr_letters = -1
nr_numbers = -1
nr_symbols = -1
while nr_letters <= 0 or nr_symbols <= 0 or nr_numbers <= 0:
    print("~WARNING: Please avoid entering letters, symbols, a zero, or negative numbers as input!~\n")
    try:
        nr_letters= int(input("How many letters would you like in your password?\n"))
        nr_symbols = int(input("How many symbols would you like?\n"))
        nr_numbers = int(input("How many numbers would you like?\n"))
    except ValueError:
        continue
    if nr_letters > 50 or nr_symbols > 50 or nr_numbers > 50:
        print("Your password will contain a maximum of 50 characters per character type.\n")
        if nr_letters > 50:
            nr_letters = 50
        if nr_symbols > 50:
            nr_symbols = 50
        if nr_numbers > 50:
            nr_numbers = 50

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = gjkP#&28
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g#2jk8&P

#We start by creating a blank password string
password = ""

for n in range(0, nr_letters): #so this loop runs exactly the number of times that the user requested for letters to be implemented (from 0 to nr-1)
  random_temporal = random.randint(0, len(letters)-1) #to choose one random index between 0 and the last possible index of the 'letters' list
  password += letters[random_temporal] #concatenating the new character to be added to the password, chosen with the random index [random_temporal] inside the letters list
  #Could have also used random.choice(letters)

for n in range(0, nr_symbols): #same procedure
  random_temporal = random.randint(0, len(symbols)-1) #same procedure
  password += symbols[random_temporal] #same procedure
  #Could have also used random.choice(symbols)

for n in range(0, nr_numbers): #same procedure
  random_temporal = random.randint(0, len(numbers)-1) #same procedure
  password += numbers[random_temporal] #same procedure
  #Could have also used random.choice(numbers)

print(f"\nYour Eazy Password is {password}") #This is the EAZY Level Password


#For randomizing the order of the characters generated, we do the following:
password_temporal_list = random.sample(password, len(password)) #This transforms the string (password) into a list of individual characters (number of characters defined by second argument, len(password)) in a randomized order

master_password = ''.join(password_temporal_list) #This joins together every singular character in a list (which is called by its argument) into a single string; each character is concatenated separately to the initial str and then joined together.
#Because of this, we use a blank initial str ''. If we didn't, the initial str repeats itself as many times as characters it is concatenated to.

print(f"\nYour Hard Password is {master_password}") #This is the HARD Level Password
