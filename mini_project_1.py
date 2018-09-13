#Author: Caroline Ekchian, cekchian@bu.edu
#import twitter API library: going to be using tweepy
import tweepy
import urllib

def authorize_twitter():
    consumer_token='ckvs5fS5TUFSuZPzYYvFuqUrH'
    consumer_secret='9csfakIHTpO0BSSJAnQICu5SB8nDqhC73JQXe39NXhpOLcZPgN'
    access_key='355214663-PY1omoDd9MhhuM41GUpaJ2FOJNK2G5UVLtwauDdY'
    access_secret='37oD1C45NSDXBYad3qOMtxU76Ynn2VkI4B0KLb6VYYKJt'
    '''consumer_token="Put consumer API key here"
    consumer_secret="Put secret consumer API key here"
    access_key="Put access key here"
    access_secret="Put secret access key here"'''
    authorization_handler=tweepy.OAuthHandler(consumer_token, consumer_secret)
    authorization_handler.set_access_token(access_key, access_secret)
    api=tweepy.API(authorization_handler)
    return api

def download_twitter_images(tweepy_api):
    tweets=[]
    media_urls=set()
	
    '''Need to add tweet_mode=extended in order to get the full text of the tweet,
	otherwise, it will not always find the image.'''
    tweets=tweepy_api.user_timeline(screen_name='BostonTweet', count=10, tweet_mode='extended')
	
    #Determine if there are any tweets with media
    for tweet in tweets:
        media_tweet=tweet.entities.get('media')
        #If there are, determine if there is an image url
        if (media_tweet is not None):
            media_urls.add(media_tweet[0]['media_url'])

    #download all of the images 				
    for url in media_urls:
        filename_index=url.rfind('/')
        filename=url[filename_index+1:]
        urllib.urlretrieve(url,'./'+filename)
	
def convert_images_to_video():
    print('In function: convert_images_to_video')
    print('Third function called.')
    print('This function is not yet implemented.')
    print('It will use ffmpeg to convert the images that were downloaded to a video. \n')
	
def analyze_video():
    print('In function: analyze_video')
    print('Fourth function called.')
    print('This function is not yet implemeted')
    print('It will use the google vision api to describe the video of the images using text.')
	
	
def main():
    api=authorize_twitter()
    download_twitter_images(api)
    #convert_images_to_video()
    #analyze_video()
	
if __name__ == '__main__':
    main()