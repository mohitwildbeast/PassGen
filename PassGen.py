#A simple Password Generator program made in Python. 

from random import * #Import everyting from Python's random module

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!@#$%^&*()-_=+?"

#Number of passwords to be generated
numOfPass = int(input("Enter number of Passwords to be generated: "))

#Input the password Length
passLength = int(input("Enter Password Length: "))

#Choose the type of Password to be generated
passType = int(input("""Choose Password Type:
				1. Only Lowercase Alphabets
				2. Lowercase and UpperCase Alphabets
				3. Alphabets and Numbers
				4. Only Numbers
				5. Alphabets and Numbers and Symbols (Recommended)
				6. Numbers and Symbols 
				7. Only Symbols: """))

passSet = "" #Stores the required Password Character Set depending on User's input
if (passType == 1):
	passSet = lowercase
elif(passType == 2):
	passSet = lowercase + uppercase
elif(passType == 3):
	passSet = lowercase + uppercase + numbers
elif(passType == 4):
	passSet = numbers
elif(passType == 5):
	passSet = lowercase +uppercase + numbers + symbols
elif(passType == 6):
	passSet = numbers + symbols
elif(passType == 7):
	passSet = symbols
else:
	print("Wrong Choice. Please input correct choice!")
	exit(1)

finalPasswords = [] #List for storing all generated passwords

for i in range(numOfPass):
	tempPass = ""
	for j in range(passLength):	
		tempPass += choice(passSet)
	finalPasswords.append(tempPass)

print("The generated Passwords are:")

for passwords in finalPasswords:
	print(passwords)

print("\nBest Recommended Password for you:")
print(choice(finalPasswords))