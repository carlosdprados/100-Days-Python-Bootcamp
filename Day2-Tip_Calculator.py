#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Day 2 Project: Tip Calculator
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is a simple Tip Calculator program.
#It gets the inputs pertaining to the bill, the selected tip percentage, and the number of people paying for the bill.
#It also checks for user misinputs, so you can only add numbers as inputs.

print("Welcome to the tip calculator!\n")

#Getting input data for bill, tip percentage, and number of people
while True:
    try:
        bill1 = float(input("What is the total bill? $"))
        tip = float(input("What is the percentage tip you would like to give? 10, 12, or 15? "))
        number_of_people = float(input("How many people are splitting the bill? "))
        break
    except ValueError:
        print("Please enter a valid number.\n")

#Incrementing the bill by the tip percentage amount
bill2 = bill1 * (1 + tip/100)

#Dividing the bill according to the number of people paying for it
bill3 = bill2 / number_of_people

#Formatting bill3 to show 2 decimal places EVEN if it's a zero
#This is because round(bill3, 2) won't show the last decimal place if it's not significant
#This method also rounds up, which is neat
bill4 = "{:.2f}".format(bill3)
print("Each person should pay $" + bill4)
