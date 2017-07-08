import requests
from search_user import *
from user_id import *
from global_variable import *
def user_media(user_id):
    url = ("%s/users/%s/media/recent/?access_token=%s")%(BASE_URL,user_id,ACCESS_TOKEN)
    print url
    response = requests.get(url).json()
    # print(response)
    if response['meta']['code'] == 200:
        if len(response['data']) == 0:
            print("user does not have any recent post/user account is private")
        else:
            return(response['data'][0]['id'])
    else:
        print("unable to fetch results.")
