import requests
from global_variable import *
def search_user_info(user_id):
    url = ('%s/users/%s/?access_token=%s') % (BASE_URL,user_id,ACCESS_TOKEN)
    response = requests.get(url).json()
    print response['data']['username'],response['data']['id']


