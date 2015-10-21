#! python3

# Password Locker practice problem from Automate Boring Stuff - Chapter 6
# https://automatetheboringstuff.com/chapter6/

# pw.py - An insecure password locker program.
# you would need to install pyperclip for this. 'pip install pyperclip'

import sys, pyperclip

PASSWORDS = {'email':'someEmail','blog':'seomPassword','luggage':'12345'}

if len(sys.argv) <2:
	print('Usage: python pw.py [account] - copy account password')
	sys.exit()

account = sys.argv[1]

if(account in PASSWORDS):
	pyperclip.copy(PASSWORDS[account])
	print('password in clipboard')
else:
	print('no password found for account ' + account)