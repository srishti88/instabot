import requests
from user_media import *
from owners_info import *
from search_user import *
def like_a_post(user_name):
  media_id = user_media(user_name)
  payload = {"access_token": ACCESS_TOKEN}
  url = ("%s/media/%s/likes")%(BASE_URL,media_id)
  print 'POST  url : %s' % (url)

  response = requests.post(url, payload).json()
  if (response['meta']['code']) == 200:
          print("Post liked Successfully")

  else:
      print("Unable to like the POST or Status code other than 200 recieved")
like_a_post(search_user())
