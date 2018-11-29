import access_mysql_database
import access_mongodb_database

'''This script is an application where a user can enter a descriptor that they want to search for in a database. They can choose to search for the decriptor in the MySQL database or the MongoDB database. The application will print out all of the twitter handles that are associated with that descriptor (it is considered to be associated with a specific twitter handle if it was one of the top 5 descriptors in a session of running run_mini_project_1.py). The application uses the query_database functions in access_mongodb_database.py and access_mysql_database.py to determine if there were any twitter handles associated with that descriptor.'''

def main():
    while(True):
        print("Select an option below:")
        print("[1] Search for descriptor in MySQL database.")
        print("[2] Search for descriptor in MongoDB database.")
        print("[q] Quit.")
        option_selected=input()
        if option_selected=='1':
            print("Enter descriptor to search for:")
            search_descriptor=input()
            twitter_handles=access_mysql_database.query_database(search_descriptor)
            if len(twitter_handles) == 0:
                print("No twitter handles were associated with this descriptor.")
            else:
                print("Twitter handles in the database associated with this descriptor:")
                for handle in twitter_handles:
                    print(handle)
        elif option_selected=='2':
            print("Enter descriptor to search for:")
            search_descriptor=input()
            twitter_handles=access_mongodb_database.query_database(search_descriptor)
            if len(twitter_handles) == 0:
                print("No twitter handles were associated with this descriptor.")
            else:
                print("Twitter handles in the database associated with this descriptor:")
                for handle in twitter_handles:
                    print(handle)
        elif option_selected=='q' or option_selected=='Q':
            break
        else:
            print("That option was not recognized")
    exit()


if __name__ == '__main__':
    main()