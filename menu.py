from delete_neg_comment import delete_a_comment
from owner_post import *
from like_a_post import *
from post_a_comment import *
from search_user import *
from user_media import *
from get_location_id import *
from get_comment_id import *
user = raw_input("Enter the username for which you want to perform following actions: ")
while len(user) == 0:
    user = raw_input("Enter the username for which you want to perform following actions: ")
def menu():
    print("1.To get owner's information")
    print("2.Search a user")
    print("3.To get user's id")
    print("4.T qo get user's media")
    print("5.To post a comment")
    print("6.Delete a negative comment")
    print("7.To like a post")
    print("8.To get images between certain geographical coordinates")
    print("9.To exit")
    def choose_option():
        user_choice = raw_input("select an option : ")
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
                get_location_post()
                menu()
            elif user_choice == 9:
                print ("Thank You for using InstaBot")
                exit(0)
            else:
                menu()
    choose_option()
menu()

