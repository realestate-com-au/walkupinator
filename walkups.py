#!/usr/bin/python

import csv
import json
import requests
assignee = ""
admins = {
'***REMOVED***': {'name' : '***REMOVED***', 'id' : ***REMOVED***},
'***REMOVED***': {'name': '***REMOVED***', 'id': ***REMOVED***},
'***REMOVED***': {'name': '***REMOVED***', 'id': ***REMOVED***},
'***REMOVED***': {'name': '***REMOVED***', 'id': ***REMOVED***},
'***REMOVED***': {'name': '***REMOVED***','id': ***REMOVED***},
'***REMOVED***': {'name': '***REMOVED***', 'id': ***REMOVED***},
'***REMOVED***': {'name': '***REMOVED***', 'id': ***REMOVED***},
'***REMOVED***': {'name': '***REMOVED***', 'id': ***REMOVED***},
'***REMOVED***': {'name': '***REMOVED***', 'id': ***REMOVED***}}

while True: 
	# saw this used online, will come in handy 
	def prompt(prompt):
		return raw_input(prompt).rstrip()

	# open users file in read mode
	users = open("userid_pan.csv","r")

	# user input
	card = str(prompt("Swipe your card: "))
	card = card[0:20]
	print "Your card number is " + card + "!"
	
	if card in admins:
		print "Tickets will now be assigned to: " + admins[card]['name']
		assignee = admins[card]['id']
		continue
	else:
		# reads in the csv
		reader = csv.reader(users, delimiter=',')
		for row in reader:
			if card == row[3]:
				username = row[1] + " " + row[2]
				print "Your name is " + username
				break
		else:
			continue
		subject = "New Walkup request from: " + username
		body = "This is an auto-generated ticket from the Innovation Hub"
	
		# package data in a dictionary matching expected JSON
		data = {'ticket': {'subject': subject, 'comment': {'body': body}, 'requester' : row[0], 'assignee_id': assignee}}
	
		# encode as JSON
		payload = json.dumps(data)
	
		# request parameters
		token = '***REMOVED***'
		url = 'https://***REMOVED***.zendesk.com/api/v2/tickets.json'
		user = "***REMOVED***"
		headers = {'content-type': 'application/json'}
	
		# Do the http POST request
	
		response = requests.post(url, data=payload, auth=("***REMOVED***/token",token), headers=headers)
