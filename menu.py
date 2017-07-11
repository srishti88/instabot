from delete_neg_comment import delete_a_comment
from owner_post import *
from like_a_post import *
from post_a_comment import *
from search_user import *
from user_media import *
from natural_calamities import natural_calamities
from get_location_id import *
from get_comment_id import *
import sys
from termcolor import colored, cprint



user = raw_input(colored("Enter the username for which you want to perform following actions: ",'red'))
while len(user) == 0:
    user = raw_input(colored("Enter the username for which you want to perform following actions: ",'red'))
def menu():
    print (colored("1","blue")+ colored(".To get owner's information",'magenta'))
    print (colored("2","blue")+ colored(".Search a user",'magenta'))
    print (colored("3","blue")+ colored(".To get user's id",'magenta'))
    print (colored("4","blue")+ colored(".T qo get user's media",'magenta'))
    print (colored("5","blue")+ colored(".To post a comment",'magenta'))
    print (colored("6","blue")+ colored(".Delete a negative comment",'magenta'))
    print (colored("7","blue")+ colored(".To like a post",'magenta'))
    print (colored("8","blue")+ colored(".To get images between certain geographical coordinates",'magenta'))
    print (colored("9","white",'on_red')+ colored(".To exit",'white','on_red'))
    def choose_option():
        user_choice = raw_input(colored("select an option : ",'red'))
        if len(user_choice) > 0:
            user_choice = int (user_choice)
            if user_choice == 1:
                owners_info()
                menu()
            elif user_choice == 2:
                search_user(user)
                menu()
            elif user_choice == 3:
                search_user_info(search_user(user))
                menu()
            elif user_choice == 4:
                user_media(search_user(user))
                menu()
            elif user_choice == 5:
                post_a_comment(search_user(user))
                menu()
            elif user_choice == 6:
                delete_a_comment(user)
                menu()
            elif user_choice == 7:
                like_a_post(search_user(user))
                menu()
            elif user_choice == 8:
                natural_calamities()
                menu()
            elif user_choice == 9:
                print ("Thank You for using InstaBot")
                exit(0)
            else:
                menu()
    choose_option()
menu()

