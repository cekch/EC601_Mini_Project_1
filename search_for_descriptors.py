import access_mysql_database

def main():
    while(True):
        print("Select an option below:")
        print("[1] Search for descriptor in mysql database.")
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
        elif option_selected=='q' or option_selected=='Q':
            break
        else:
            print("That option was not recognized")
    exit()


if __name__ == '__main__':
    main()