import mysql.connector
'''This script creates a MySQL database with the name 
app_session_database. It creates a table within this 
database called session_info. This table holds the 
following information: session_id - this is a number 
starting from 1 that indicates the number session
session_date - the date of the session
twitter_handle - the twitter handle that the user 
entered to download images from, then a column for each 
of the top 5 descriptors of the images that were downloaded. 
If there were no common descriptors between the images 
downloaded, then these columns will be set to 0.'''

mydb = mysql.connector.connect(host="localhost", user="Enter your username.", passwd="Enter your password.")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE app_session_database")
mycursor.execute("USE app_session_database")
mycursor.execute("CREATE TABLE IF NOT EXISTS session_info (session_id INT AUTO_INCREMENT PRIMARY KEY, session_date DATE, twitter_handle TEXT, num_of_tweets_retrieved INT, num_of_tweets_with_images INT, most_common_descriptor_1 TEXT, most_common_descriptor_2 TEXT, most_common_descriptor_3 TEXT, most_common_descriptor_4 TEXT, most_common_descriptor_5 TEXT)")
mycursor.close()
mydb.close()
