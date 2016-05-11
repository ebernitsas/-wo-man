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

	abuse = False
	cheating = False
	generic = False


	reasons = ['Emotional Abuse', 'Cheating', 'Physical Abuse', 
				'Economic Abuse', 'Sexual Abuse', 'Verbal Abuse',
				'Psychological Abuse', 'Dynamics for Immigrant Women',
				'Dynamics for Women with Disabilties', 'Academic Abuse',
				'Same-Sex Relationship Abuse', 'Send Generic Letter',
				'Write Letter']

	#check flags

	if '-r' in sys.argv:
		reason = sys.argv[sys.argv.index('-r') + 1]
	if '-n' in sys.argv:
		name = sys.argv[sys.argv.index('-n') + 1]
	if '-mn' in sys.argv:
		myname = sys.argv[sys.argv.index('-mn') + 1]
	if '-e' in sys.argv:
		you = sys.argv[sys.argv.index('-e') + 1]

	if '-sp' in sys.argv:
		os.system("open -a Google\ Chrome " + 
				"http://stoprelationshipabuse.org/pdfs/PowerControlwheelNOSHADING.pdf")
	if '-sr' in sys.argv:
		os.system("open -a Google\ Chrome " + 
				"http://stoprelationshipabuse.org/educated/types-of-abuse/")

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
		if '13' in reason:
			original_letter = raw_input('Original Letter:\n')
		elif '2' in reason and reason != '12':
			cheating = True
		elif '2' not in reason and reason != '12':
			abuse = True

		reason = reason.split() #now reason is a list of numbers
		added_sentence = " I will not stand around and endure your "
		if original_letter != '':
			reason.remove('13')
		if '12' in reason and original_letter == '':
			generic = True
			reason.remove('12')
		for i in reason:
			if len(reason) > 1 and i == reason[-2]:
				added_sentence += reasons[int(i)-1] + " and "
			elif len(reason) > 0 and i == reason[-1]:
				added_sentence += reasons[int(i)-1] + "."
			else: added_sentence += reasons[int(i)-1] + ", "



	#checking to see if custom reason was abuse or cheating
	else:
		if 'abuse' in reason.lower():
			abuse = True
		if 'cheat' in reason.lower():
			cheating = True

	#print added_sentence

	#get letters
	with open('/bin/letters.txt') as fp:
		text = fp.read()



	if cheating == True:
		# print "Case 1"

		start = text.find('Cheating')
		text = text[(start+8):]

		end = text.find('--end')
		text = text[:end]

		#print text

		insert = text.find('--p2')
		text = text[0:insert] + added_sentence + text[(insert)+4:]

	elif abuse == True:
		# print "Case 2"

		#use one of the abuse messages
		a = str(random.randint(0,1))

		start = text.find('Abuse' + '1')
		text = text[(start+6):]

		end = text.find('--end')
		text = text[:end]

		insert = text.find('--p2')
		text = text[0:insert] + added_sentence + text[(insert)+4:]

	elif generic == True:
		# print "Case 3"

		start = text.find('Generic')
		text = text[(start+7):]

		end = text.find('--end')
		text = text[:end]

	else:

		if reason != [] and reason != ['12']: 
			text = original_letter + added_sentence
		else: text = original_letter



	msg = "Dear " + name + ",\n \n" + text + "\n \n" + "Best, " + myname

	print msg
	command = "mail -s \"Please Read This\" "+ you +" <<< \"" +msg + "\""

	os.system(command)

try: 
	email()
except:
	print "\n[Invalid Inputs]"

# email()









