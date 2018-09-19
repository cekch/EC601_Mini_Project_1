# EC601_Mini_Project_1

This application uses the Twitter API and the Google API to look at a certain number of tweets from a Twitter feed and download the images contained in these tweets. The images that are downloaded are converted into a video and are analzyed using the label detection functionality of the Google vision API. Before running this application, look at the rest of the README.md document to make sure that you have entered all of the neccessary information and that your environment is set up correctly. In order to run this application, use the following command in your command prompt:
> python run_mini_project_1.py

This repository contains two python modules:
    1. mini_project_1.py
    2. run_mini_project_1.py
	
mini_project_1.py
----
imports tweepy, urllib, subprocess, google cloud vision, io, and os
mini_project_1.py contains four functions:
1. **authorize_twitter(consumer_token, consumer_secret, access_key, access_secret)**
..* The user will have to enter their Twitter API information into this function so that it can autorize the users information and allow them to use the Twitter API. This function returns the twitter API interface.
2. **download_twitter_images(tweepy_api, twitter_handle, number_of_tweets)**
..* In this function, the user will enter the twitter handle that they want to download the images from and the number of tweets that they want to look at. Then, this function uses the twitter api to download the tweets from the user specified twitter handle and extract the images from those tweets. These images are downloaded to the current directory. This function returns a list of image filenames.
3. **convert_images_to_video()**
..* This function does not take any inputs. It uses ffmpeg to convert the sequence of images to a video.
4. **analyze_video(filenames)**
..* This takes in a list of the image filenames so that the google api can use those images to run label detection on them using the google api. This function prints out each label that the google vision api detects to the command line.

run_mini_project_1.py
---
This file imports mini_project_1
run_mini_project_1.py contains one function:
1. **main()**
..* Main first runs authorize_twitter(consumer_token, consumer_secret, access_key, access_secret) to authorize the user's Twitter API information. The user will need to enter the values for these variables in this file. Next, download_twitter_images(tweepy_api, twitter_handle, number_of_tweets) is called. By default, the twitter_handle is set to 'BostonTweet' and the number_of_tweets is set to 20. These values can be changed in this file. Then, there is a check to see if there were any images in the tweets that were read. If there were no images, it exits main(). If there were images, convert_images_to_video() is called next, then analyze_video(filenames) is called, where filenames represents a list of the image files that are going to be analyzed. 

Notes
---
1. The image files that are downloaded will be downloaded to the current directory where the program is being run from.
2. You will have to add your credentials to run this, in order to use the Google API. You can do this by typing the following command into your command prompt:
> export GOOGLE_APPLICATION_CREDENTIALS=YourFilePath/Your_Credenitals.json
3. This application was developed on Windows 10 using Python 2.7.15
4. The video that is created in this application was compatible during testing with both Windows Media Player and VLC
