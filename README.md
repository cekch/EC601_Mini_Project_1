# EC601_Mini_Project_1

This repository contains two python modules:
    1. mini_project_1.py
	2. run_mini_project_1.py
	
mini_project_1.py
====

mini_project_1.py contains four functions:
    1. **authorize_twitter(consumer_token, consumer_secret, access_key, access_secret)**
	    The user will have to enter their twitter api information into this functions so that it can authorize the users information and allow them to use the twitter api. This function returns the twitter api interface.
	2. **download_twitter_images(tweepy_api, twitter_handle, number_of_tweets)**
	    In this function, the user will enter the twitter handle that they want to download the images from and the number of tweets that they want to look at. Then, this function uses the twitter api to download the tweets from the user specified twitter handle and extract the images from those tweets. These images are downloaded to the current directory. This function returns a list of image filenames.
	3. **convert_images_to_video()**
	    This function does not take any inputs. It uses ffmpeg to convert the sequence of images to a video.
	4. **analyze_video(filenames)**
	    This takes in a list of the image filenames so that the google api can use those images to run label detection on them using the google api. This function prints out each label that the google vision api detects to the command line.