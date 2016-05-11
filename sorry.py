#!/usr/bin/python

"""
sorry -100

"""
import sys
import imaplib
import email
import getpass

num_emails = 100

#Parse Arguments
string = ""
#print sys.argv
for i in sys.argv[1:]:
	string = string + i

if ('-' in string): num_emails = string[string.index('-')+1:]

num_emails = int(num_emails)


mail = imaplib.IMAP4_SSL('imap.gmail.com')
# imaplib module implements connection based on IMAPv4 protocol
# username = raw_input('user: ')
# password = raw_input('password: ')
logged_in = False
while (logged_in == False):
  username = raw_input('Gmail: ')
  password = getpass.getpass()
  

  try:
    mail.login(username, password)
    logged_in = True
  except:
    print "\nUsername/Password Incorrect, Try Again\n"
# >> ('OK', [username at gmail.com Vineet authenticated (Success)'])

mail.list() # Lists all labels in GMail
mail.select('[Gmail]/Sent Mail') # Connected to inbox.

typ, data = mail.search(None, 'ALL')
ids = data[0]
id_list = ids.split()
#get the most recent email id
latest_email_id = int( id_list[-1] )

#iterate through 15 messages in decending order starting with latest_email_id
#the '-1' dictates reverse looping order
count_sorry = 0
count_just = 0
count_actually = 0
count_i_think = 0


for i in range( latest_email_id, latest_email_id-num_emails, -1 ):
   typ, data = mail.fetch( i, '(RFC822)' )

   for response_part in data:
      if isinstance(response_part, tuple):

        find_reply = '\n>'
       
        msg = response_part[1]
        
        reply = msg.find(find_reply)

        msg = msg[0:reply]


        msg = msg.lower()
        count_sorry += msg.count('sorry')
        count_just += msg.count('just')
        count_actually += msg.count('actually')
        count_i_think += msg.count('i think')


print "sorry: " + str(count_sorry)
print "just: " + str(count_just)
print "actually: " + str(count_actually)
print "I think: " + str(count_i_think)

          
