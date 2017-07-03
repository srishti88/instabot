import requests
ACCESS_TOKEN = '5679361638.395d4d9.d4e5e05e63904a4099cf293855490f95'
BASE_URL = 'https://api.instagram.com/v1'
def owners_info():
    url = '%s/users/self/?access_token=%s' % (BASE_URL,ACCESS_TOKEN)
    data = requests.get(url).json()
    print (" welcome you are " + data['data']['username'] +" and link to your profile pic is: "+ data['data']['profile_picture'])
def search_user():
    user_to_be_searched = raw_input("Enter a name to search: ")
    while len(user_to_be_searched) == 0:
        user_to_be_searched = raw_input("Enter a name to search: ")
    url = ('%s/users/search?q=%s&access_token=%s') % (BASE_URL,user_to_be_searched,ACCESS_TOKEN)
    response = requests.get(url).json()
    # print response
    if response['meta']['code'] == 200:
        if len(response['data']) > 0:
            # print response['data'][0]['id']
            return response['data'][0]['id']
        else:
            print ("User not Found")
            search_user()
    else:
        print ("Unable to Fetch Data")
        exit(0)

def search_user_info(user_id):
    url = ('%s/users/%s/?access_token=%s') % (BASE_URL,user_id,ACCESS_TOKEN)
    response = requests.get(url).json()
    print response['data']['username'],response['data']['id']
search_user_info(search_user())


