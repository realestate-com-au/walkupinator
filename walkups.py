#!/usr/bin/python

import csv
import json
import requests
assignee = ""
# import api and agent data from data.json
jsondata = json.load(open("data.json"))
agents = jsondata['agents']
# open users file in read mode
users = open("userid_pan.csv","r")

while 1: 
    users.seek(0,0) 
    def prompt(prompt):
        return raw_input(prompt).rstrip()

    
    # user input
    card = str(prompt("Swipe your card: "))
    card = card[0:20]
    
    # checks if the card number is an assignee	
    if card in agents:
        print "Tickets will now be assigned to: " + agents[card]['name']
        assignee = agents[card]['id']
    else:
        # reads in the csv
        reader = csv.reader(users, delimiter=',')
        for row in reader:
            if card == row[3]:
                username = row[1] + " " + row[2]
                print "Your card number is " + card + "!"
                print "Your name is " + username
                break
        else:
            print "You are not registered, please register at the printers"
            continue
        subject = "New Walkup request from: " + username
        body = "This is an auto-generated ticket from the Innovation Hub"

        # package data in a dictionary matching expected JSON
        data = {'ticket': {'subject': subject, 'comment': {'body': body}, 'requester' : row[0], 'assignee_id': assignee}}

        # encode as JSON
        payload = json.dumps(data)

        # request parameters
        token = jsondata['api-token']
        url = jsondata['api-url']
        user = jsondata['api-email']
        headers = {'content-type': 'application/json'}

        # Do the http POST request

        response = requests.post(url, data=payload, auth=(jsondata['api-email']
            + "/token",token), headers=headers)
