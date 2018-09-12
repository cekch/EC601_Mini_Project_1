#Author: Caroline Ekchian, cekchian@bu.edu
#import twitter API library: going to be using tweepy

def authorize_twitter():
    print('In function: authorize_twitter')
    print('First function called.')
    print('This function will authorize the usage of the tweepy. \n')

def download_twitter_images():
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
    authorize_twitter()
    download_twitter_images()
    convert_images_to_video()
    analyze_video()
	
if __name__ == '__main__':
    main()