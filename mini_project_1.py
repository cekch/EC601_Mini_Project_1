#Author: Caroline Ekchian, cekchian@bu.edu
#import twitter API library: going to be using tweepy
import tweepy

def authorize_twitter():
    consumer_token="Put consumer API key here"
    consumer_secret="Put secret consumer API key here"
    access_key="Put access key here"
    access_secret="Put secret access key here"
    authorization_handler = tweepy.OAuthHandler(consumer_token, consumer_secret)
    authorization_handler.set_access_token(access_key, access_secret)
    api= tweepy.API(authorization_handler)
    return api

def download_twitter_images(api):
    print('In function: download_twitter_images')
    print('Second function called.')
    print('This function is not yet implemented.')
    print('It will download the images from a twitter feed. \n')
	
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
    #download_twitter_images(api)
    #convert_images_to_video()
    #analyze_video()
	
if __name__ == '__main__':
    main()