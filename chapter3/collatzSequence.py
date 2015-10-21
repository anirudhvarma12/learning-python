# Collatz Sequence practice project from Automate Boring Stuff - Chapter 3
# https://automatetheboringstuff.com/chapter3/

def collatz(number):
	if number%2==0:
		print(number//2)
		return number//2
	else:
		output = 3*number+1
		print(output)
		return output

print("Enter a number")
try:
	inputNumber = int(input())
	result = inputNumber
	while result!=1:
		result = collatz(result)
except ValueError:
	print("Enter a valid number")



