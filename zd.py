import requests as re
import json
from collections import defaultdict
from requests.models import HTTPBasicAuth
import configs
import math
cached_results={}
# Creating a Cache to store the results of the API CALLS
def get_all_tickets()->json:
    '''
    This function  returns all the tickets 
    '''
    try:
        # Trying to reach the API using username and password
        req=re.get(configs.API_LIST_ENDPOINT,  auth=HTTPBasicAuth(configs.USER,configs.PASSWORD))
        if req.status_code!=200:
            raise Exception((req.status_code))
        return req.json()
    except Exception as e:
        exception_handler(e)

def exception_handler(e):
    print("OOPS! Something went wrong while trying to reach the API")
    print(e)
    if(e.args[0]==401):
        print("Wrong Credentials!! Please check your email and password / API Token")
    if(e.args[0]==403):
        print("You are unauthorized to perform this operation! Please verify your permissions")
    if(e.args[0]==404):
            print("The ticket # you are looking for does not exists!! Please Try again")  

def get_single_ticket(i)->json:
    '''
    This Function retrieves 1 ticket at a time and returns its JSON
    '''
    try:
        if i in cached_results:
            print("Entry Found in Cache")
            return cached_results[i]
        else:
            req=re.get(configs.API_TICKET_ENDPOINT+str(i)+'.json?',  auth=HTTPBasicAuth(configs.USER,configs.PASSWORD))
            if req.status_code!=200:
                raise Exception((req.status_code))
            # print(req.json()['ticket']['subject'])
            response=req.json()
            ticket=response["ticket"]
            return ticket
    except Exception as e:
        exception_handler()


def display_ticket(i, ticket):
    '''This function is used for Displaying the tickets'''
    print("*"*75+"Ticket# "+str(i)+"*"*75)
    print(ticket["id"])
    print("Subject : "+ticket["subject"]+"/n")
    print("Description : "+ticket["description"]+"/n")
    print("Created at : "+":"+ticket["created_at"])
    print("Current Status : "+":"+ticket["status"])


if __name__ == "__main__":
    flag=True
    while(flag):
        """menu to display options to the user
        """
        print("*"*75+"ZENDESK Menu for Tickets"+"*"*75)
        print("Enter 1 to view all the tickets")
        print("Enter 2 to view individual tickets")
        print("Enter Any other to exit")
        choice=input()
        if(choice=="1"):
            print("*"*75+" Printing All tickets... Please Wait ... "+"*"*75)
            response=get_all_tickets()
            for ticket in response["tickets"]:
                i=ticket["id"]
                page=i/25
                if(i%25==1):
                    print("Showing Results "+str(math.floor(page*25))+"-"+str(math.ceil(page)*25))  
                if i in cached_results:
                    print("Found Entry in Cache")
                    display_ticket(i,cached_results[int(i)])               
                else:
                    cached_results[int(i)]=ticket
                    display_ticket(i, ticket)   
                if(i%25==0 and i!=0):
                    # To Paginate the JSON and show only 25 per page
                    print("")
                    input("Press Enter to move to page "+str(int(i/25)+1))                 
        elif (choice=="2"):
            print("Please enter the ticket number you want to retrieve(Between 1-100)")
            ticket=get_single_ticket(int(input()))
            try:
                display_ticket(ticket["id"],ticket)
            except Exception as e:
                print("")
        else:
                print("Wrong Choice. Please Enter 1 or 2 only")
        print("Do you want to Continue?")
        print("Enter y/Y to continue any other to exit")
        ch=input()
        if(ch.lower()=="y"):
           flag = True
        else:
            flag = False
            print("Exiting...")


    
