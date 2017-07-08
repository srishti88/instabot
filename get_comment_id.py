import requests
from global_variable import *
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
comment_id = []
def return_neg_comment_id(media_id):
    print media_id
    url = ('%s/media/%s/comments?access_token=%s') % (BASE_URL,media_id,ACCESS_TOKEN)
    # print url
    response = requests.get(url).json()

    for comment in response['data']:
        analyze = TextBlob(comment['text'], analyzer=NaiveBayesAnalyzer())
        if analyze.sentiment.p_pos < analyze.sentiment.p_neg:
            print comment['text']
            print "Is a negative comment"
            comment_id.append(comment['id'])

        else:
            print comment['text']
            print "Is a positive comment"
    return comment_id


