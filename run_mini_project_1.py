import mini_project_1
import access_mysql_database
import access_mongodb_database

'''This script uses the mini_project_1 api to first authorize a users use of the twitter api.
Then it downloads the images from a twitter feed, where the twitter handle and number of tweets
to look at is specified by the user in this script. The images that were downloaded then are converted to a video. Label detection is then used to analyze the images. Once the labels are analyzed, the user is given an option to save the information from their session of use for this application. They can either save it to the MongoDB database or the MySQL database. They can also choose to not save the session at all.'''
def main():
    #Note to user: enter all tokens and access keys
    consumer_token='Enter consumer token here.'
    consumer_secret='Enter consumer secret token here.'
    access_key='Enter access key here.'
    access_secret='Enter secret access key here.'
    api=mini_project_1.authorize_twitter(consumer_token, consumer_secret, access_key, access_secret)
    print("Enter twitter handle:")
    twitter_handle=input()
    number_of_tweets=20
    [image_filenames,num_of_tweets_retrieved, num_of_tweets_with_images]=mini_project_1.download_twitter_images(api, twitter_handle, number_of_tweets)
    #Check to see if there were any images associated with the specified twitter feed
    if image_filenames is 0:
        #If there weren't, exit
        print("There are no images associated with " + twitter_handle + "'s twitter feed.")
        exit(-1)
    else:
        #If there were, convert the images to video and analyze the images
        mini_project_1.convert_images_to_video()
        all_descriptors=mini_project_1.analyze_video(image_filenames)
        top_5_descriptors=mini_project_1.find_most_common_descriptors(all_descriptors)
       #Check to see if user would like to save information from this session
        while(True):
            print("Would you like to save this session to the MongoDB database or the MySQL database?")
            print("[1] MySQL")
            print("[2] MongoDB")
            print("[3] Do not save session.")
            database_selection=input()
            if database_selection == '1':
                access_mysql_database.add_row(top_5_descriptors, twitter_handle, num_of_tweets_retrieved, num_of_tweets_with_images)
                exit(0)
            elif database_selection == '2':
                access_mongodb_database.add_row(top_5_descriptors, twitter_handle, num_of_tweets_retrieved, num_of_tweets_with_images)
                exit(0)
            elif database_selection == '3':
                exit(0)
            else:
                print("Selection not recognized. Pleas try again")
	
if __name__ == '__main__':
    main()