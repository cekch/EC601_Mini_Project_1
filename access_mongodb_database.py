from pymongo import MongoClient
import datetime

'''This script has two functions for accessing the MongoDB database. 
The add_row() function adds a row to the database, if the
database does not exist, it will create it and if the collection 
does not exist, it will create that as well. The query_database() 
function will search through the database for a specific descriptor
and returns the twitter handles that had that descriptor as one of
its top 5 most common descriptors.'''

def add_file(most_common_descriptors, handle, num_of_tweets, num_of_tweets_with_images):
    myclient=MongoClient('localhost', 27017)
    mydb=myclient["app_session_database"]
    mycollection=mydb["session_info"]
    current_date = datetime.datetime.today().strftime('%Y-%m-%d')
    session_dict = {"session_date": current_date, "twitter_handle": handle,   
    "num_of_tweets_retrieved":num_of_tweets, "num_of_with_images": num_of_tweets_with_images,
    "most_common_descriptor_1": most_common_descriptors[0], "most_common_descriptor_2":
    most_common_descriptors[1], "most_common_descriptor_3": most_common_descriptors[2], 
	"most_common_descriptor_4":most_common_descriptors[3], "most_common_descriptor_5": 
    most_common_descriptors[4]}
    x=mycollection.insert_one(session_dict)
    myclient.close()
	
def query_database(search_descriptor):
    twitter_handles_with_descriptor=[]
    all_instances=[]
    myclient=MongoClient('localhost', 27017)
    mydb=myclient["app_session_database"]
    mycollection=mydb["session_info"]
    my_query = {"$or": [{"most_common_descriptors_1": search_descriptor}, {
    "most_common_descriptor_2": search_descriptor}, {"most_common_descriptor_3":  
    search_descriptor}, {"most_common_descriptor_4":search_descriptor}, {
    "most_common_descriptor_5":search_descriptor}]}
    #only return the twitter handle field, and nothing else
    all_instances_with_field=list(mycollection.find(my_query, {"twitter_handle":1, "_id":0}))
    for i in range(len(all_instances_with_field)):
        all_instances.append(all_instances_with_field[i]["twitter_handle"])

    myclient.close()

    for handle in all_instances:
        if twitter_handles_with_descriptor.count(handle)==0:
            twitter_handles_with_descriptor.append(handle)
	
    return twitter_handles_with_descriptor


    
