import requests
from global_variable import ACCESS_TOKEN,BASE_URL
def get_location_id():
  print "To get Longitude and latitude go to: https://maps.google.com"
  lat = str(raw_input("Please enter a Latitude: "))
  lng = str(raw_input("Please enter a Longitude: "))
  url = "%s/locations/search?lat=%s&lng=%s&access_token=%s"%(BASE_URL,lat,lng,ACCESS_TOKEN)
  # print url
  response = requests.get(url).json()
  return response
# get_location_id()
def get_location_post():
  text_to_search_in_caption = raw_input("Enter Captions Related to natural Calamity: ")
  locations = get_location_id()
  for location in locations['data']:
      if location['id'] == "0":
          pass
      else:
          url = "%s/locations/%s/media/recent?access_token=%s"%(BASE_URL,location['id'],ACCESS_TOKEN)
          # print url
          response = requests.get(url).json()
          if len(response['data']):
              for posts in response['data']:
                  if posts['caption'] == None:
                      pass
                  else:
                    if text_to_search_in_caption in posts['caption']['text']:
                        print "Post with id " + posts['id'] +" has \"" + text_to_search_in_caption + "\" in caption."
          else:
              # print ("No posts contain: %s") % text_to_search_in_caption
            pass
get_location_post()