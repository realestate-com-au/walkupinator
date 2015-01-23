#!/usr/bin/python

import csv
import json
import requests
import pymssql
# bring in json data
jsondata = json.load(open("data.json"))
assignee = ""
previouspan = ""
userexists = True
# import sql server details from json
server = jsondata['sqlserver']
user = jsondata['username'] 
passw = jsondata['password']
db = jsondata['db']

# connect to the database
conn = pymssql.connect(server,user,passw,db)

# create a cursor to run queries with
c = conn.cursor(as_dict=True)


def prompt(prompt):
    return raw_input(prompt).rstrip()

def loaddata():
    c.execute("SELECT u.Email, u.FName, u.LName, p.PAN " + 
                    "FROM BEARS_Users " +  
                    "AS u JOIN BEARS_UserPAN AS p on u.UserID = p.UserID")
# import api and agent data from data.json
agents = jsondata['agents']
walkupyn = jsondata['walkupyn']

while 1: 
    loaddata()
    # Get the userdata from the database
    # user input
    card = str(prompt("Swipe your card: "))
    card = card[0:20]
    if card == "reload":
        print "Loaded users from database"
        loaddata()
        continue
    if previouspan != card:
        previouspan = card
    else:
        print "Cannot scan twice in a row"
        continue
    # checks if the card number is an assignee	
    if card in agents:
        print "Tickets will now be assigned to: " + agents[card]['name']
        assignee = agents[card]['id']
    else:
        # reads in the csv
        for row in c:
            if card == row['PAN']:
                username = row['FName'] + " " + row['LName']
                print "Your card number is " + card + "!"
                print "Your name is " + username
                break
        else:
            userexists = False
        if userexists == False:
            print "You are not registered, \nplease register at the printers"
            continue
        else:
            subject = "New Walkup request from: " + username
            body = "This is an auto-generated ticket from the Innovation Hub"

            # package data in a dictionary matching expected JSON
            data = { 
            'ticket':{
                'subject': subject, 
                'comment':{'body': body},
                'type': 'task',
                'requester' : row['Email'], 
                'assignee_id': assignee,
                'custom_fields': [{'id':walkupyn, 'value': 'yes'}]
                }
            }

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
