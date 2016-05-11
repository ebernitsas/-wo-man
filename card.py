#!/usr/bin/python
import sys
import os


d_woman = {"latino/hispanic":.54, "american indian":.59, "african american":.64,
	"pacific islander": .65, "white":.78, "asian american":.90}

d_man =  {"latino/hispanic":.61, "american indian":.69, "african american":.71,
	"pacific islander": .70, "white":1, "asian american":1.13}

if ("-get" in sys.argv):
	os.system("open -a Google\ Chrome " + "https://shop.hillaryclinton.com/products/the-woman-card")

if ("-man" in sys.argv):
	if ("-lat" in sys.argv):
		print("\nlatino/hispanic man: " +  str(d_man["latino/hispanic"]) + " cents on the dollar\n")
	if ("-ind" in sys.argv):
		print("\namerican indian man: " +  str(d_man["american indian"]) + " cents on the dollar\n")
	if ("-bla" in sys.argv):
		print("\nafrican american man: " +  str(d_man["african american"]) + " cents on the dollar\n")
	if ("-pac" in sys.argv):
		print("\npacific islander man: " + str(d_man["pacific islander"]) + " cents on the dollar\n")
	if ("-wh" in sys.argv):
		print("\nwhite man: " + str(d_man["white"]) + " on the dollar\n")
	if ("-asi" in sys.argv):
		print("\nasian american man: " + str(d_man["asian american"]) + " cents on the dollar\n")

elif ("-woman" in sys.argv):
	if ("-lat" in sys.argv):
		print("\nlatino/hispanic woman: " + str(d_woman["latino/hispanic"]) + " cents on the dollar\n")
	if ("-ind" in sys.argv):
		print("\namerican indian woman: " + str(d_woman["american indian"]) + " cents on the dollar\n")
	if ("-bla" in sys.argv):
		print("\nafrican american woman: " + str(d_woman["african american"]) + " cents on the dollar\n")
	if ("-pac" in sys.argv):
		print("\npacific islander woman: " + str(d_woman["pacific islander"]) + " cents on the dollar\n")
	if ("-wh" in sys.argv):
		print("\nwhite woman: " + str(d_woman["white"]) + " cents on the dollar\n")
	if ("-asi" in sys.argv):
		print("\nasian american woman: " + str(d_woman["asian american"]) + " cents on the dollar\n")


if ('-perks' in sys.argv):
	print("\n-Lower wages!")
	print("-More expensive healthcare!")
	print("-No paid family leave!")
	print("-Limited access to your own reproductive rights!\n")
	print("For more information:")
	print("https://www.hillaryclinton.com/feed/what-official-hillary-america-woman-card-gets-you/")
		
	
























#works cited: http://www.infoplease.com/ipa/A0882775.html