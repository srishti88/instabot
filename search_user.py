import requests
from global_variable import *
def search_user(user):
    # user_to_be_searched = raw_input("Enter a name to search: ")
    url = ('%s/users/search?q=%s&access_token=%s') % (BASE_URL,user,ACCESS_TOKEN)
    response = requests.get(url).json()
    # print response
    if response['meta']['code'] == 200:
        if len(response['data']) > 0:
            print ("User found with id: %s")%(response['data'][0]['id'])
            return response['data'][0]['id']
        else:
            print ("User not Found")
            search_user()
    else:
        print ("Unable to Fetch Data")
        exit(0)
