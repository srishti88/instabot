import requests
from global_variable import *
from owners_info import *

def owners_post():
    url = ('%s/users/self/media/recent/?access_token=%s')%(BASE_URL,ACCESS_TOKEN)
    response = requests.get(url).json()
    if (response['meta']['code']) == 0:
        if len(response['data']) == 0:
            print("Do not have a post")
        else:
            print(response)['data']
    else:
        print("invalid")


