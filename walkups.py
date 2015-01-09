#!/usr/bin/python

import csv
import json
import requests

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
		username = row[1] + " " + row[2]
		print "Your name is " + username
		break		

subject = "New Walkup request from: " + username
body = "Please update this ticket"

# package data in a dictionary matching expected JSON
data = {'ticket': {'subject': subject, 'comment': {'body': body}, 'requester' : row[0], 'assignee_id': "***REMOVED***"}}

# encode as JSON
payload = json.dumps(data)

# request parameters
token = '***REMOVED***'
url = 'https://***REMOVED***.zendesk.com/api/v2/tickets.json'
user = "***REMOVED***"
headers = {'content-type': 'application/json'}

# Do the http POST request

response = requests.post(url, data=payload, auth=("***REMOVED***/token",token), headers=headers)
