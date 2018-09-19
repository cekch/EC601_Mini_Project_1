import mini_project_1

'''This script uses the mini_project_1 api to first authorize a users use of the twitter api.
Then it downloads the images from a twitter feed, where the twitter handle and number of tweets
to look at is specified by the user in this script. The images that were downloaded then are converted
to a video. Label detection is then used to analyze the images.'''
def main():
	#mini_project_1.authorize_twitter(consumer_token, consumer_secret, access_key, access_secret)
    api=mini_project_1.authorize_twitter('Enter consumer token here', 'Enter consumer secret here', 'Enter access key here', 'Enter secret access key here')
    #mini_project_1.download_twitter_images(tweepy_api, twitter_handle, number_of_tweets)
    image_filenames=mini_project_1.download_twitter_images(api, 'BostonTweet', 20)
    mini_project_1.convert_images_to_video()
    #mini_project_1.analyze_video(filenames)
    mini_project_1.analyze_video(image_filenames)
	
if __name__ == '__main__':
    main()