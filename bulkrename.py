import os
#define main function
def main():
    #set variable of i to zero
    i = 0
    #define our directory
    path = "~/DeveloperStuff/Dev"
    # for filename in our path's directory
    for filename in os.listdir(path):
        #destination variable for what we want to rename the files to (ie format)
        my_destination = "image" + str(i) + ".jpg"
        #the source of the newly named files
        my_source = path + filename
        #saved the new file 
        my_destination = path + my_destination
        #os renames the files officially
        os.rename(my_source, my_destination)
        i += 1

if __name__ == '__main__':
    main()