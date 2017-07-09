import requests
from user_media import *
from owners_info import *
from search_user import *
def post_a_comment(user_name):
  media_id = user_media(user_name)
  comment_text = raw_input("Your comment: ")
  payload = {"access_token": ACCESS_TOKEN, "text" : comment_text}
  url = ("%s/media/%s/comments")%(BASE_URL,media_id)
  print 'POST  url : %s' % (url)

  response = requests.post(url, payload).json()
  if (response['meta']['code']) == 200:
      if len(response['data']):
          print(response['data'])
      else:
          print("Unable to Post a Comment")

  else:
      print("Status code other than 200 recieved")
# post_a_comment(search_user())
