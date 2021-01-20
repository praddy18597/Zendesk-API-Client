
import unittest
import json
import os
import sys
import zd
from os import path
class TestStringMethods(unittest.TestCase):

    def test_get_all_tickets(self):
        response=zd.get_all_tickets()
        self.assertEqual(len(response["tickets"]), 100)

    def test_get_single_tickets(self):
        """This function tests the get_single_ticket() method and verifies if it works
        """
        f=open("ticket.json")
        try:
            # print(os.getcwd())
            # print(path.exists("ticket.json"))            
            if(path.isfile('ticket.json')):
                # print("Inside if ")
                data=json.load(f)
                f.close()
                ticket=zd.get_single_ticket(1)
                self.assertEqual(ticket,data["ticket"])
            else:
                raise Exception("File Not Found")
        except Exception as e:
            print("Exception Ocurred")
            print(e)
        finally:
            f.close()

            


if __name__ == '__main__':
    unittest.main()