# Walkups

Minimum Python Version: 2.7.3

Requirements: 

*Zendesk API Key
    
* Zendesk API user email

* Agent Id's for the assignees

* Card numbers for assignees

* CSV of user details. Similar format to:  email,firstname,lastname,card PAN

* RFID card reader

Modules that need to be installed: 
* requests

Config: 
* Run pip -r requirements.txt
    
* Input the above information into the respective spots in the data.json file.

Usage:
* Run the script
    
* Scan a card. 
    
* If the card is a user it will send a request to zendesk, if the card  is an agent the script will assign all tickets going forward to that  agent.





The MIT License (MIT)

Copyright (c) 2015 Jarid Spokes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
