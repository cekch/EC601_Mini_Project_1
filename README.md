# EC601_Mini_Project_1

This application uses the Twitter API and the Google API to look at a certain number of tweets from a Twitter feed and download the images contained in these tweets. The images that are downloaded are converted into a video and are analzyed using the label detection functionality of the Google vision API. The application determines what the most common descriptors are among the labels of the images that were downloaded from a specific twitter handle. The user of run_mini_project_1.py has the option to save the information from their session (this information includes: the session date, the twitter handle, the number of tweets retrieved, the number of tweets with images retrieved and the top 5 most common descriptors of the images that were downloaded) to either a MySQL database or a MongoDB database. The user can then query these databases to search for common descriptors between different twitter handles by using the search_for_descriptors.py application. Before running this application, look at the rest of the README.md document to make sure that you have entered all of the neccessary information and that your environment is set up correctly. 

This application was built and tested with Python 3.7 and Windows 10. If you do not already have MongoDB or MySQL installed on your computer, please follow the following tutorials:  
[MySQL Tutorial](https://www.youtube.com/watch?v=WuBcTJnIuzo)  
[MongoDB Tutorial](https://www.youtube.com/watch?v=FwMwO8pXfq0)

This repository contains six python modules:  
    1. mini_project_1.py  
    2. run_mini_project_1.py  
    3. access_mongodb_database.py  
    4. access_mysql_database.py  
    5. create_mysql_database.py  
    6. search_for_descriptors.py  
    
Running the Application
----
First, make sure that you have read through the entire README to make sure that you have installed all of the neccessary resources. Then clone the repository and make sure you checkout the branch Mini_Project_3. Next, before running all any of the scripts, make sure that you have entered your password and username for all of the MySQL database connections. The occurrences of the mysql.connector.connect() functions occur in create_mysql_database.py and access_mysql_database.py(). Additionally, make sure that you have entered your consumer token, secret token, access key and secret access key into run_mini_project_1.py.

Next, run create_mysql_database.py

> python create_mysql_database.py

Then, run_mini_project_1.py

> python run_mini_project_1.py

First, you will be prompted to enter a twitter handle from which you want to download images.
If this is not your first time running run_mini_project_1.py, then you will see a message that says that twitter_image_video.mp4 already exists, and you will be asked if you want to replace it. Type in 'y' to indicate that you do.
You will then be prompted to save the information from your session of running this application to either the MySQL database or the MongoDB database. You can also choose to not save the information at all.

Next, if you would like to query the database to search for a specific descriptor to determine if either databases contain any twitter handles that are associated with that descriptor. To do this, run search_for_discriptors.py.

> python search_for_descriptors.py

You will be prompted to select which database you would like to query. You have the option to query the MySQL database or the MongoDB database. You can also choose to quit the application. However, if you decide to query one of the databases you will be prompted to enter a descriptor that you would like to search for. If the database that you are querying contains a twitter handle that is associated with this descriptor, then all of the twitter handles that are associated with this descriptor will be printed out to the command line. If no, twitter handles were found in the database that are associated with this descriptor, a message saying "No twitter handles were associated with this descriptor." will be printed to the command line.
 
mini_project_1.py
----
imports tweepy, urllib, subprocess, google cloud vision, io, and os  
mini_project_1.py contains four functions:
1. **authorize_twitter(consumer_token, consumer_secret, access_key, access_secret)**  
The user will have to enter their Twitter API information into this function so that it can autorize the users information and allow them to use the Twitter API. This function returns the twitter API interface.
2. **download_twitter_images(tweepy_api, twitter_handle, number_of_tweets)**  
In this function, the user will enter the twitter handle that they want to download the images from and the number of tweets that they want to look at. Then, this function uses the twitter api to download the tweets from the user specified twitter handle and extract the images from those tweets. These images are downloaded to the current directory. This function returns a list of image filenames, the number of tweets that were retrieved and the number of tweets that had images in them.
3. **convert_images_to_video()**  
This function does not take any inputs. It uses ffmpeg to convert the sequence of images to a video.
4. **analyze_video(filenames)**  
This takes in a list of the image filenames so that the google api can use those images to run label detection on them using the google api. This function prints out each label that the google vision api detects to the command line. This function returns a list of all of the image labels that were found to describe the images.
5. **find_most_common_descriptors(all_image_labels)**  
This function takes in all the image labels that were found for all of the images that were downloaded from a specific twitter handle and returns a list of the top 5 most common descriptors among that list. If there aren't any common descriptors among that list or there are less than 5 common descriptors, it will return 'None' in that space in the list that this function returns.

run_mini_project_1.py
---
This file imports mini_project_1  
This file imports access_mysql_database  
This file imports access_mongodb_database  
run_mini_project_1.py contains one function:  
1. **main()**  
Main first runs authorize_twitter(consumer_token, consumer_secret, access_key, access_secret) to authorize the user's Twitter API information. The user will need to enter the values for these variables in this file. The user is prompted to enter a twitter handle through the command line. The number of tweets to retrieve is set to 20 by default. Next, download_twitter_images(tweepy_api, twitter_handle, number_of_tweets) is called. Then, there is a check to see if there were any images in the tweets that were read. If there were no images, it exits main(). If there were images, convert_images_to_video() is called next, then analyze_video(filenames) is called, where filenames represents a list of the image files that are going to be analyzed. Then, based on the analysis of the images, a list of labels to describe all of the images is produced. The user is then prompted to see if they want to save the session information to a database, they can either choose to save the session information to a MySQL database or a MongoDB database or to not save the session information at all.

access_mongodb_database.py
---
This file imports MongoClient from pymongo  
This file imports datetime  
access_mongo_db.py contains two functions:  
1.**add_file(most_common_descriptors, handle, num_of_tweets, num_of_tweets_with_images)**  
First, a connection to the Mongo client is made. Then this function adds a file to the MongoDB database called app_session_database. If this database does not already exist, it is created. The file is added to a collection called session_info. If this collection does not already exist, it is created. Then a file is added to the collection, using the information for the session. This information contains the session date, the twitter handle, the number of tweets retrieved during the session, the number of tweets retrieved that contain images, and the top 5 most common descriptors for the all of the images that were downloaded for the specific session. The connection to the Mongo client is then closed.
2.**query_database(search_descriptor)**  
First, a connection to the Mongo client is made. Then the collection session_info in the app_sesssion_database database is queried to determine if any twitter handles that are in the database are associated with the search descriptor. This function returns a list of all of the twitter handles that are associated with the search_descriptor. The connection to the Mongo client is then closed.

access_mysql_database.py
---
This file imports mysql.connector  
This file imports datetime  
access_mongo_db.py contains two functions:  
1.**add_row(most_common_descriptors, handle, num_of_tweets, num_of_tweets_with_images)**  
First, a connection to the MySQL server is made. The user will need to enter their username and password into this function for the function call to mysql.connector.connect(). Then this function adds a file to the MySQL database called app_session_database. The file is added to a table called session_info. Then a row is added to the table, using the information for the session. This information contains the session date, the twitter handle, the number of tweets retrieved during the session, the number of tweets retrieved that contain images, and the top 5 most common descriptors for all of the images that were downloaded for the specific session. The connection to the MySQL server is then closed.
2.**query_database(search_descriptor)**  
First, a connection to the MySQL server is made. The user will need to enter their username and password into this function for the function call to mysql.connector.connect(). Then the table session_info in the app_session_database database is queried to determine if any twitter handles that are in the database are associated with the search descriptor. This function returns a list of all of the twitter handles that are associated with the search_descriptor. The connection to the MySQL server is then closed.

create_mysql_database.py  
---
This file imports mysql.connector  
This script creates a MySQL database called app_session_database. In order to do that, first a connection to the MySQL server is made. The user will need to enter their username and password into this function for the function call to mysql.connector.connect(). Then the database is created. Next, a table called session_info is created, after first checking to make sure that the table does not already exist. This table that is created contains 10 columns. The first column is the session_id, which is an auto incremented integer. The second column contains the date of the session. The third column contains the twitter handle. The fourth column contains the number of tweets that were retrieved during that specific session. The fifth column contains the number of tweets that were retrieved that contained images. And the remaining five columns contain the top 5 most common descriptors for all of the images that were retrieved during that session.

search_for_descriptors.py
---
This file imports access_mysql_database  
This file imports mongodb_database  
This file contains one function:  
1.**main()**  
This function first prompts the user to select an option of the database that they want to query. They can either select the MySQL database, the MongoDB database, or they can choose to quit the application. Next, the user is prompted to enter a descriptor that they want to search for in the database that they selected. Once the user enters the descriptor that they would like to search for, the query_database() function for the database that they selected to query will be called to determine if the database contains any twitter handles that have images where one of the top 5 descriptors match with the descriptor that they entered. If there are twitter handles that where one of the top 5 descriptors match, the twitter handle(s) will printed to the console. The user can keep entering descriptors to search for until they choose to exit the application.

Notes
---
1. The image files that are downloaded will be downloaded to the current directory where the program is being run from.
2. You will have to add your credentials to run this, in order to use the Google API. You can do this by typing the following command into your command prompt:
> export GOOGLE_APPLICATION_CREDENTIALS=YourFilePath/Your_Credenitals.json
3. This application was developed on Windows 10 using Python 3.7
4. The video that is created in this application was compatible during testing with both Windows Media Player and VLC
5. For reference, there is a file called ExamplesOfRunningScripts that contains screenshots of scripts being run and the resulting databases that are created when the scripts are run.
