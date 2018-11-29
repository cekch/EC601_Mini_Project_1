import mysql.connector
import datetime

'''
This script has two functions for accessing the MySQL database. The add_row() function adds a row to the database. The query_database() function will search through the database for a specific descriptor and returns the twitter handles that had that descriptor as one of its top 5 most common descriptors.
'''

def add_row(most_common_descriptors, handle, num_of_tweets, num_of_tweets_with_images):
    mydb = mysql.connector.connect(host="localhost", user="Enter your username.", passwd="Enter your password.")
    mycursor = mydb.cursor()
    mycursor.execute("USE app_session_database")
    current_date = datetime.datetime.today().strftime('%Y-%m-%d')
    mycursor.execute("INSERT INTO session_info (session_id, session_date, twitter_handle, num_of_tweets_retrieved, num_of_tweets_with_images, most_common_descriptor_1, most_common_descriptor_2, most_common_descriptor_3, most_common_descriptor_4, most_common_descriptor_5) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (current_date, handle, num_of_tweets, num_of_tweets_with_images, most_common_descriptors[0], most_common_descriptors[1], most_common_descriptors[2], most_common_descriptors[3], most_common_descriptors[4]))
    mydb.commit()
    mycursor.close()
    mydb.close()

def query_database(search_descriptor):
    all_instances=[]
    twitter_handles_with_descriptor=[]
    mydb = mysql.connector.connect(host="localhost", user="Enter your username.", passwd="Enter your password.")
    mycursor = mydb.cursor()
    mycursor.execute("USE app_session_database")
    mycursor.execute("SELECT twitter_handle FROM session_info WHERE (most_common_descriptor_1=%s) OR (most_common_descriptor_2=%s) OR (most_common_descriptor_3=%s) OR (most_common_descriptor_4=%s) OR (most_common_descriptor_5=%s)", (search_descriptor, search_descriptor, search_descriptor, search_descriptor, search_descriptor))
    for twitter_handle in mycursor:
        all_instances.append(twitter_handle[0])  
    mycursor.close()
    mydb.close()

    for handle in all_instances:
        if twitter_handles_with_descriptor.count(handle) == 0:
            twitter_handles_with_descriptor.append(handle)
	
    return twitter_handles_with_descriptor
	


