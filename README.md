# Zendesk-API-Client

## Installation and usage instructions

So firstly, to do this project we need to install some software tools in CMD which are as follows:
1.	In first step we need to install python by using the below link:
https://realpython.com/installing-python/
2.	Once you done with installation, we need to install pip to download other dependencies’ using the link below:
https://phoenixnap.com/kb/install-pip-windows
3.	In this step we need to install request package for authentication and requests of the Tickets using simple command in CMD:
 pip install requests
4.	Before we are executing code to request tickets, we need to create Zendesk account where you will get API keys, API domain and password using the following link:
https://www.zendesk.com/register/#step-1
5.	Now fill this detail in config.py file for e.g.:

```python
API_LIST_ENDPOINT="https://abc.zendesk.com/api/v2/tickets.json"
API_TICKET_ENDPOINT="https://abc.zendesk.com/api/v2/tickets/"
USER="xyz@gmail.com" #Add actual user here
PASSWORD="xyz@18"
```
6.	So, now we import some essential libraries such as requests, json and defaultdict for the sending the tickets.
7.	Now we are ready to connect with Zendesk API by following line of code:
```python
# Trying to reach the API using username and password
req=re.get(configs.API_LIST_ENDPOINT,  auth=HTTPBasicAuth(configs.USER,configs.PASSWORD))
```
8. In next step we are going to display all the tickets which are as follows:
```python
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
```
9.	The output of the tickets from 1-100 which are as follows:
![picture alt](Zendesk%20images/Ticket%201.png "Ticket 1")

![picture alt](/Zendesk%20images/Ticket%20100.png "Ticket 100")

10. Now we are going to display individual ticket details the code is as follows:
```python
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
```

11. The output of the individual tickets which are as follows:

![picture alt](/Zendesk%20images/Individual%20Ticket.png "Individual Ticket")

12. Now we display them in a list the code is as follows:
```python
def display_ticket(i, ticket):
    '''This function is used for Displaying the tickets'''
    print("*"*75+"Ticket# "+str(i)+"*"*75)
    print(ticket["id"])
    print("Subject : "+ticket["subject"]+"/n")
    print("Description : "+ticket["description"]+"/n")
    print("Created at : "+":"+ticket["created_at"])
    print("Current Status : "+":"+ticket["status"])
```

13. The output is same as we display all tickets earlier, so I do not attach same screenshot again.

14.	So, we are showing 25 tickets in one page after 25 tickets it ask for another page to display next 25 tickets and it is goes on until 100 tickets.

![picture alt](/Zendesk%20images/Ticket%2025.png "Ticket 25")

*Thank You*


