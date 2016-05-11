#!/usr/bin/python

# -xkcd https://imgs.xkcd.com/comics/sandwich.png
# -menu -wd (with descriptions) -gc (giant clubs) -sub (subs) -sl (slims)

#-gclub -sub -slim
#+cuc  +dmus +jmus +pep +vin +on +or +spr
#+avo +bac +rb +tuna +trk +chz +ham +tom +mayo

import sys
import os

#Giant Club Sandwiches:
a1 = '#7 SMOKED HAM CLUB'
a2 = '''1/4 pound of real wood smoked ham,
provolone cheese, lettuce, tomato & mayo!'''
b1 = '#8 BILLY CLUB'
b2 = '''Choice roast beef, smoked ham, provolone cheese,
Dijon mustard, lettuce, tomato & mayo.'''
c1 = '#9 ITALIAN NIGHT CLUB'
c2 = '''Genoa salami, Italian capicola, smoked ham,
and provolone cheese all topped with lettuce, tomato,
onion, mayo & our homemade Italian vinaigrette.'''
d1 = '#10 HUNTER\'S CLUB'
d2 = '''A full 1/4 pound of medium rare roast beef,
provolone, lettuce, tomato & mayo.'''
e1 = '#11 COUNTRY CLUB'''
e2 = '''Sliced turkey breast, real wood smoked ham,
provolone, and tons of lettuce, tomato & mayo!
(A very traditional, yet always exceptional classic!)'''
f1 = '#12 BEACH CLUB'
f2 = '''Fresh baked turkey breast, provolone cheese, avocado
spread, sliced cucumber, lettuce, tomato and mayo!'''
g1 = '#13 GOURMET VEGGIE CLUB'
g2 = '''Double provolone, real avocado spread, sliced
cucumber, lettuce, tomato & mayo. (Try it on my
7-grain whole wheat bread. This veggie sandwich
is really yummy! Sprouts* optional)'''
h1 = '#14 BOOTLEGGER CLUB'
h2 = '''Roast beef, turkey breast, lettuce, tomato & mayo.
An American classic!'''
i1 = '#15 CLUB TUNA'
i2 ='''The same as our #3 Totally Tuna except this one
has a lot more. Housemade tuna salad, provolone,
sliced cucumber, lettuce & tomato. (Sprouts* optional)'''
j1 = '#16 CLUB LULU'
j2 ='''Sliced turkey breast, bacon, lettuce, tomato
& mayo. (JJ's original turkey & bacon club)'''
k1 = '#17 ULTIMATE PORKER'
k2 = '''Real wood smoked ham and bacon with lettuce,
tomato & mayo! (This one rocks!)'''

#8" Subs
l1 = '#1 PEPE'
l2 = '''Real wood smoked ham and provolone cheese,
lettuce, tomato & mayo. (The original)'''
m1 = '#2 BIG JOHN'
m2 = '''Medium rare choice roast beef, mayo,
lettuce & tomato.'''
n1 = '#3 TOTALLY TUNA'
n2 = '''Fresh housemade tuna, mixed with celery, onions,
and our tasty sauce, sliced cucumber, lettuce & tomato.
(My tuna rocks! Sprouts* optional)'''
o1 = '#4 TURKEY TOM'
o2 = '''Fresh sliced turkey breast, lettuce, tomato & mayo.
The original (Sprouts* optional)'''
p1 = '#5 VITO'
p2 = '''The original Italian sub with genoa salami, provolone,
capicola, onion, lettuce, tomato, & a real tasty Italian
vinaigrette. (Hot peppers by request)'''
q1 = '#6 THE VEGGIE'
q2 = '''Layers of provolone cheese separated by real avocado
spread, sliced cucumber, lettuce, tomato & mayo. (Truly a
gourmet sub not for vegetarians only. Sprouts* optional)'''
r1 = 'J.J.B.L.T.'
r2 = '''Bacon, lettuce, tomato & mayo!
(My B.L.T. rocks)
'''

#Slims
s1 = 'slim 1' 
s2 = 'Ham & cheese'
t1 = 'slim 2'
t2 = 'Roast beef'
u1 = 'slim 3'
u2 = 'Tuna salad'
v1 = 'slim 4'
v2 = 'Turkey breast'
w1 = 'slim 5'
w2 = 'Salami, capicola, cheese'
x1 = 'slim 6'
x2 = 'Double provolone'


giant_club_names = [a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k1]
giant_club_descriptions = [a2, b2, c2, d2, e2, f2, g2, h2, i2, j2, k2]

sub_names = [l1, m1, n1, o1, p1, q1, r1]
sub_descriptions = [l2, m2, n2, o2, p2, q2, r2]

slim_names = [s1, t1, u1, v1, w1, x1]
slim_descriptions = [s2, t2, u2, v2, w2, x2]

def displayGiantClubs():
	print '\n'
	for i in range(len(giant_club_names)):
		print giant_club_names[i]
		if with_desc:
			print giant_club_descriptions[i] + '\n'

def displaySlims():
	print '\n'
	for i in range(len(slim_names)):
		print slim_names[i]
		if with_desc:
			print slim_descriptions[i] + '\n'

def displaySubs():
	print '\n'
	for i in range(len(sub_names)):
		print sub_names[i]
		if with_desc:
			print sub_descriptions[i] + '\n'

def displayAll():
	displaySubs()
	displayGiantClubs()
	displaySlims()


sandwich = ''
sandwich_number = 0
sandwich_addons = []
selection = ''
with_desc = False
order_complete = False
no_args = False

if len(sys.argv) == 1:
	print "\nI will NOT make you a sandwich.\n"
	print "But here is the complete Jimmy John's menu"
	print "You can make your own!\n"
	raw_input("press 'Enter' to see the menu\n")
	no_args = True


if '-xkcd' in sys.argv:
	os.system("open -a Google\ Chrome " + 'https://imgs.xkcd.com/comics/sandwich.png')

if '-menu' in sys.argv or no_args == True:
	if '-wd' in sys.argv: with_desc = True
	if '-gclub' in sys.argv: 
		try: 
			int(sys.argv[sys.argv.index('-gclub') + 1])
			order_complete = True
		except: displayGiantClubs()
	elif '-sub' in sys.argv: 
		try: 
			int(sys.argv[sys.argv.index('-gclub') + 1])
			order_complete = True
		except: displaySubs()
	elif '-slim' in sys.argv: 
		try: 
			int(sys.argv[sys.argv.index('-gclub') + 1])
			order_complete = True
		except: displaySlims()
	else: displayAll()
	if order_complete == False: 
		selection = raw_input('select sandwich [ex. -gclub 7]:\n')


if ('-gclub' in sys.argv and '-menu' not in sys.argv) or ('-gclub' in selection):

	if '-gclub' in selection:
		sandwich_number = selection[selection.index('-gclub') + 7:]
		print sandwich_number

	else: sandwich_number = sys.argv[sys.argv.index('-gclub') + 1]

	try: sandwich_number = int(sandwich_number) 	
	except: displayGiantClubs()

	if (7 <= sandwich_number and sandwich_number <= 17):
		sandwich = giant_club_names[sandwich_number-7]
		#print sandwich, "sandwich"
		sandwich_description = giant_club_descriptions[sandwich_number-7]

elif ('-sub' in sys.argv and '-menu' not in sys.argv) or ('-sub' in selection):
	print "definitely a SUB"
	if '-sub' in selection:
		print sandwich_number
		sandwich_number = selection[selection.index('-sub') + 5]
	else: sandwich_number = sys.argv[sys.argv.index('-sub') + 1]

	try: sandwich_number = int(sandwich_number)
	except: displaySubs()

	if (1 <= sandwich_number and sandwich_number <= 7):
		sandwich = sub_names[sandwich_number-1]
		sandwich_description = sub_descriptions[sandwich_number-1]

elif ('-slim' in sys.argv and '-menu' not in sys.argv) or ('-slim' in selection):
	if '-slim' in selection:
		print sandwich_number
		sandwich_number = selection[selection.index('-slim') + 6]
	else: sandwich_number = sys.argv[sys.argv.index('-slim') + 1]
	
	try: 
		sandwich_number = int(sandwich_number)
	except: displaySlims()

	if (1 <= sandwich_number and sandwich_number <= 6):
		sandwich = slim_names[sandwich_number-1]
		sandwich_description = slim_descriptions[sandwich_number-1]

#addons
#+cuc  +dmus +jmus +pep +vin +on +or +spr
#+avo +bac +rb +tuna +trk +chz +ham +tom +mayo
if '+cuc' in sys.argv: sandwich_addons.append('add cucumbers')
elif '-cuc' in sys.argv: sandwich_addons.append('no cucumbers')

if '+dmus' in sys.argv: sandwich_addons.append('add dijon mustard')
elif '-dmus' in sys.argv: sandwich_addons.append('no dijon mustard')

if '+jmus' in sys.argv: sandwich_addons.append('add jimmy mustard')
elif '-jmus' in sys.argv: sandwich_addons.append('no jimmy mustard')

if '+pep' in sys.argv: sandwich_addons.append('add peppers')
elif '-pep' in sys.argv: sandwich_addons.append('no peppers')

if '+vin' in sys.argv: sandwich_addons.append('add italian vinaigrette')
elif '-vin' in sys.argv: sandwich_addons.append('no italian vinaigrette')

if '+on' in sys.argv: sandwich_addons.append('add onions')
elif '-on' in sys.argv: sandwich_addons.append('no onions')

if '+or' in sys.argv: sandwich_addons.append('add oregano')
elif '-or' in sys.argv: sandwich_addons.append('no oregano')

if '+spr' in sys.argv: sandwich_addons.append('add sprouts')
elif '-spr' in sys.argv: sandwich_addons.append('no sprouts')

if '+avo' in sys.argv: sandwich_addons.append('add avocado')
elif '-avo' in sys.argv: sandwich_addons.append('no avocado')

if '+bac' in sys.argv: sandwich_addons.append('add bacon')
elif '-bac' in sys.argv: sandwich_addons.append('no bacon')

if '+rb' in sys.argv: sandwich_addons.append('add roast beef')
elif '-rb' in sys.argv: sandwich_addons.append('no roast beef')

if '+tuna' in sys.argv: sandwich_addons.append('add tuna')
elif '-tuna' in sys.argv: sandwich_addons.append('no tuna')

if '+trk' in sys.argv: sandwich_addons.append('add turkey')
elif '-trk' in sys.argv: sandwich_addons.append('no turkey')

if '+chz' in sys.argv: sandwich_addons.append('add provolone')
elif '-chz' in sys.argv: sandwich_addons.append('no provolone')

if '+ham' in sys.argv: sandwich_addons.append('add ham')
elif '-ham' in sys.argv: sandwich_addons.append('no ham')

if '+tom' in sys.argv: sandwich_addons.append('add tomato')
elif '-tom' in sys.argv: sandwich_addons.append('no tomato')

if '+mayo' in sys.argv: sandwich_addons.append('add mayo')
elif '-mayo' in sys.argv: sandwich_addons.append('no mayo')

options = ['+cuc',  '+dmus' ,'+jmus', '+pep', '+vin', '+on', '+or' ,'+spr',
'+avo', '+bac', '+rb', '+tuna', '+trk', '+chz', '+ham', '+tom', '+mayo',
'-cuc',  '-dmus' ,'-jmus', '-pep', '-vin', '-on', '-or' ,'-spr',
'-avo', '-bac', '-rb', '-tuna', '-trk', '-chz', '-ham', '-tom', '-mayo', '-menu']




print "-------------------"	
print "ORDER UP!"
print sandwich
for i in sandwich_addons:
	print "- " + i

sandwich_ascii ='''
               .----------'    '-.
             /  .      '     .   \\
            /        '    .      /|
           /      .             \ /
          /  ' .       .     .  || |
         /.___________    '    / //
         |._          '------'| /|
         '.............______.-' /  
         |-.                  | /
         `"""""""""""""-.....-'
'''

print sandwich_ascii
	













