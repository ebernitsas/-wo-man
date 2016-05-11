#!/usr/bin/python

#dump -n name -e email -r reason

# Import smtplib for the actual sending function
import smtplib
import sys
import os
import random

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.

def email():
	message = ''
	reason = ''
	you = ''
	myname = '' 
	name = ''
	added_sentence = ''
	original_letter = ''



	reasons = ['Inappropriate Behavior',
				'Negativity',
				'Lack of Integrity',
				'Inability to Perform',
				'Inability to fit office culture',
				'Failure to keep Commitments',
				'Improper Conduct',
				'Lack of Drive/Enthusiasm',
				'Other']

	#check flags

	if '-r' in sys.argv:
		reason = sys.argv[sys.argv.index('-r') + 1]
	if '-n' in sys.argv:
		name = sys.argv[sys.argv.index('-n') + 1]
	if '-mn' in sys.argv:
		myname = sys.argv[sys.argv.index('-mn') + 1]
	if '-e' in sys.argv:
		you = sys.argv[sys.argv.index('-e') + 1]

	#prompt for input if input was not provided
	if myname == '':
		myname = raw_input('your name: ')

	if name == '':
		name = raw_input('their name: ')
		
	if you == '':
		you = raw_input('their email: ')

	if reason == '':
		reason = raw_input('[(s) show reasons]\nreason: ')
		if reason == 's':
			count = 1
			for i in reasons:
				print str(count) + " " + i
				count+=1
			reason = raw_input('')

		if '9' in reason:
			original_letter = raw_input('Original Letter:\n')

		reason = reason.split() #now reason is a list of numbers


		if '9' in reason: reason.remove('9')

		added_sentence = " We can no longer employ you due to your "

		for i in reason:
			if len(reason) > 1 and i == reason[-2]:
				added_sentence += reasons[int(i)-1].lower() + " and "
			elif len(reason) > 0 and i == reason[-1]:
				added_sentence += reasons[int(i)-1].lower() + "."
			else: added_sentence += reasons[int(i)-1].lower() + ", "

	




	#get letters
	with open('/bin/fire_letters.txt') as fp:
		text = fp.read()


	insert = text.find('--p2')
	text = text[0:insert] + added_sentence + text[(insert)+4:]



	if reason != [] : 
		text = text + original_letter + added_sentence
	else: text = original_letter



	msg = name + ",\n \n" + text + "\n \n" + "Regards, " + myname

	print msg
	
	command = "mail -s \"Termination of Employment\" "+ you +" <<< \"" +msg + "\""

	os.system(command)

try: 
	email()
except:
	print "\n[Invalid Inputs]"

# email()









