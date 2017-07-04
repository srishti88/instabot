import requests
from global_variable import *
from owners_info import *
from search_user import *
from user_id import *
def menu():

    print("1.user id")
    print("2.owners information")
    print("3.search user")
    menu_input = int(raw_input("enter your choice: "))
    if menu_input == 1:
        search_user_info(search_user())
    elif menu_input == 2:
        owners_info()
    elif menu_input == 3:
        search_user()
    else:
        exit()
menu()







