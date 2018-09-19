import mini_project_1

'''This script uses the mini_project_1 api to first authorize a users use of the twitter api.
Then it downloads the images from a twitter feed, where the twitter handle and number of tweets
to look at is specified by the user in this script. The images that were downloaded then are converted
to a video. Label detection is then used to analyze the images.'''
def main():
    consumer_token='Enter consumer token here.'
	consumer_secret='Enter consumer secret token here.'
    access_key='Enter access key here.'
    access_secret='Enter secret access key here.'
    api=mini_project_1.authorize_twitter(consumer_token, consumer_secret, access_key, access_secret)
    twitter_handle='BostonTweet'
    number_of_tweets=20
    image_filenames=mini_project_1.download_twitter_images(api, twitter_handle, number_of_tweets)
    if image_filenames is 0:
        print("There are no images associated with " + twitter_handle + "'s twitter feed.")
        exit(-1)
    else:
        mini_project_1.convert_images_to_video()
        mini_project_1.analyze_video(image_filenames)
        exit(0)
	
if __name__ == '__main__':
    main()