import requests
from get_comment_id import return_neg_comment_id
from user_media import *
from owners_info import *
import sys
from termcolor import colored

def delete_a_comment(user):
    neg_id = return_neg_comment_id(user_media(search_user(user)))
    if len(neg_id):
        for id in neg_id:
            url = "%s/media/%s/comments/%s?access_token=%s" % (BASE_URL,user_media(owners_id()),id,ACCESS_TOKEN)
            print ("Attempting to delete negative comment from :")
            print  url
            response = requests.delete(url)
            print ("Negative Comments with id's deleted successfully.")
            print neg_id
    else:
        print (colored("HOORAY!!!! No negative comments Found",'red','on_green'))

