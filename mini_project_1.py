#Author: Caroline Ekchian, cekchian@bu.edu
import tweepy
import urllib.request
import subprocess
from google.cloud import vision
import io
import os

def authorize_twitter(consumer_token, consumer_secret, access_key, access_secret):
    '''Authorize use of the twitter API'''
    print("Authorizing use of Twitter API.")
    authorization_handler=tweepy.OAuthHandler(consumer_token, consumer_secret)
    authorization_handler.set_access_token(access_key, access_secret)
    api=tweepy.API(authorization_handler)
    return api

def download_twitter_images(tweepy_api, twitter_handle, number_of_tweets):
    print("Retreiving tweets from " + twitter_handle + "'s twitter feed.")
    '''Download the images from the twitter feed'''
    tweets=[]
    media_urls=set()
	
    #The maximum number of tweets the user_timeline can handle is 3200
    if number_of_tweets > 3200:
        number_of_tweets=3200

    '''Need to add tweet_mode=extended in order to get the full text of the tweet,
	otherwise, it will not always find the image.'''
    tweets=tweepy_api.user_timeline(screen_name=twitter_handle, count=number_of_tweets, tweet_mode='extended')
  
    num_of_tweets_retrieved=0
    num_of_tweets_with_images=0
    #Determine if there are any tweets with media
    for tweet in tweets:
        num_of_tweets_retrieved=num_of_tweets_retrieved+1
        media_tweet=tweet.entities.get('media')
        #If there are, determine if there is an image url
        if (media_tweet is not None):
            media_urls.add(media_tweet[0]['media_url'])

    #If there were any images, download them
    if len(media_urls) is 0:
        return 0
    else:
        print("Downloading images.")
        image_number=0
        image_filenames=[]
        for url in media_urls:
            filename_index=url.rfind('/')
            filename=url[filename_index+1:]
		    #change filenames to a format that can be used as an input into ffmpeg
            urllib.request.urlretrieve(url,'./image_'+str(image_number)+'.jpg')
            image_filenames.append('image_'+str(image_number)+'.jpg')
            image_number=image_number+1

        return [image_filenames,num_of_tweets_retrieved, image_number]
	
def convert_images_to_video():
    '''convert the sequence of images to video using ffmpeg'''
    print("Converting the sequence of images to video.")
    subprocess.call('ffmpeg -loglevel panic -framerate 1/5 -f image2 -i image_%1d.jpg -vf scale=640:360 -r 30 twitter_image_video.mp4')
	
def analyze_video(filenames):
    '''analyze the images that are in the video using the google vision API to detect
    the different labels in the images'''
    print("Analzying images.")
    client = vision.ImageAnnotatorClient()
    #loop through all images
    all_image_labels = []
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
            all_image_labels.append(label.description)
            print('\t'+label.description)
	
    return all_image_labels

def find_most_common_descriptors(all_image_labels):
    '''find the five most common descriptors among all of the labels for the images.'''
    most_common_descriptors_dict={}
    top_5_descriptors=[]
    most_common_descriptors=set([label for label in all_image_labels if all_image_labels.count(label) > 1])
    for descriptor in most_common_descriptors:
        most_common_descriptors_dict[descriptor] = all_image_labels.count(descriptor)
	
    most_common_descriptors_sorted = sorted(most_common_descriptors_dict.items(), key=lambda x:x[1])
    most_common_descriptors_sorted.reverse()
	
    for i in range(5):
    #if there aren't 5 common descriptors, then fill the rest of the list with "None"
        try:
            descriptor=most_common_descriptors_sorted[i][0]
            top_5_descriptors.append(descriptor)
        except:
            top_5_descriptors.append("None")
	
    return top_5_descriptors
