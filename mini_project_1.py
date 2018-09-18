#Author: Caroline Ekchian, cekchian@bu.edu
import tweepy
import urllib
import subprocess
from google.cloud import vision
import base64
import io
import os

#google API key
def authorize_twitter():
    consumer_token="Put consumer API key here"
    consumer_secret="Put secret consumer API key here"
    access_key="Put access key here"
    access_secret="Put secret access key here"
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
    image_number=0
    image_filenames=[]	
    for url in media_urls:
        filename_index=url.rfind('/')
        filename=url[filename_index+1:]
		#change filenames to a format that can be used as an input into ffmpeg
        urllib.urlretrieve(url,'./image_'+str(image_number)+'.jpg')
        image_filenames.append('image_'+str(image_number)+'.jpg')
        image_number=image_number+1

    return image_filenames
	
def convert_images_to_video():
    subprocess.call("ffmpeg -framerate 1/5 -f image2 -i image_%1d.jpg -vf scale=640:-1 -vcodec libx264 -r 30 twitter_image_video.mp4")
	
def analyze_video(filenames):
    client = vision.ImageAnnotatorClient()
    #loop through all images
    for file in filenames:
        #load each image
        with io.open('./'+file, 'rb') as twitter_image_file:
            image_content = twitter_image_file.read()

        twitter_image = vision.types.Image(content=image_content)

        #extract labels from twitter images
        response = client.label_detection(image=twitter_image)
        image_labels = response.label_annotations
		
		#print the labels detected in each image
        print('Labels in ' + file+ ':')
        for label in image_labels:
            print('\t'+label.description)
def main():
    api=authorize_twitter()
    image_filenames=download_twitter_images(api)
    convert_images_to_video()
    analyze_video(image_filenames)
	
if __name__ == '__main__':
    main()