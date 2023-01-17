#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Day 1 Project: Band Name Generator
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This program creates a cool band name for you. It will use both the name of the city you grew up in, and the name of your pet, to concatenate them and produce a unique new name for your band :)

#Title
print("\nThis is the Cool Band Name Generator\n\n")

#Asking the user for city name; all spaces are eliminated using the string.replace() function, so the band name doesn't have weird spaces in between  
city = input("What's name of the city you grew up in?\n").replace(" ","")

#String length is computed to later combine the halves of input names into only one word (the band name)
city_length = len(city)

#We need to divide the length by 2, so we need to check if the length is odd or even. When odd, we add 1 to the value
#trick: & 1 checks the last bit of the variable. If it is 1 (as in 0011 = 3), then it's odd; when 0 (0010 = 2), it's even
if city_length & 1:
  city_length = city_length + 1
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Same procedure for inputting and processing pet name
#str.lower() function is used to lowercase every letter inside this string, so the band name doesn't get a weird capital letter in the middle
pet = input("What's your pet's name?\n").lower().replace(" ","")
pet_length = len(pet)
if pet_length & 1:
  pet_length = pet_length + 1

#Concatenating the left half of the city name and the right half of the pet name.
print("\nYour cool band name shall be " + city[:city_length//2] + pet[pet_length//2:])
