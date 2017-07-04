import requests
from global_variable import *
def owners_info():
    url = '%s/users/self/?access_token=%s' % (BASE_URL,ACCESS_TOKEN)
    data = requests.get(url).json()
    print (" welcome you are " + data['data']['username'] +" and link to your profile pic is: "+ data['data']['profile_picture'])
