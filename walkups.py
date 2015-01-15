#!/usr/bin/python

import csv
import json
import requests
import pymssql
# bring in json data
jsondata = json.load(open("data.json"))
assignee = ""
previouspan = ""
# import sql server details from json
server = jsondata['sqlserver']
user = jsondata['username'] 
passw = jsondata['password']
db = jsondata['db']

# connect to the database
conn = pymssql.connect(server,user,passw,db)
# create a cursor to run queries with
c = conn.cursor(as_dict=True)
# collect initial data
users = c.execute("SELECT u.Email, u.FName, u.LName, p.PAN FROM BEARS_Users AS \
u JOIN BEARS_UserPAN AS p on u.UserID = p.UserID")
# import api and agent data from data.json
agents = jsondata['agents']
# open users file in read mode
# users = open("userid_pan.csv","r")
walkupyn = jsondata['walkupyn']
while 1: 
    def prompt(prompt):
        return raw_input(prompt).rstrip()

    
    # user input
    card = str(prompt("Swipe your card: "))
    card = card[0:20]
    if previouspan != card:
        previouspan = card
    else:
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
            print "You are not registered, please register at the printers"
            continue
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
