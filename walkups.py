#!/usr/bin/python
import csv

# saw this used online, will come in handy 
def prompt(prompt):
	return raw_input(prompt).strip()

# open users file in read mode
users = open("../userid_pan.csv","r")

# user input
card = prompt("Swipe your card: ")
print "Your card number is " + card + "!"

# reads in the csv
reader = csv.reader(users, delimiter=',')
for row in reader:
	if card == row[3]:
		print "Your name is " + row[1] + " " + row[2]	
		break		
		
