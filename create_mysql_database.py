import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Enter your password.")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE app_session_database")
mycursor.execute("USE app_session_database")
mycursor.execute("CREATE TABLE IF NOT EXISTS session_info (session_id INT AUTO_INCREMENT PRIMARY KEY, session_date DATE, twitter_handle TEXT, num_of_tweets_retrieved INT, num_of_tweets_with_images INT, most_common_descriptor_1 TEXT, most_common_descriptor_2 TEXT, most_common_descriptor_3 TEXT, most_common_descriptor_4 TEXT, most_common_descriptor_5 TEXT)")
mycursor.close()
mydb.close()
