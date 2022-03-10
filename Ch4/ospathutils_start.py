#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    # print(os.name)
    #
    # # Check for item existence and type
    # print("Item exists: " + str(path.exists("textfile.txt")))
    # print("Item is a File " + str(path.isfile("textfile.txt")))
    # print("Item is a Dir " + str(path.isdir("textfile.txt")))
    #
    # # Work with file paths
    # print("Item path: " + str(path.realpath("textfile.txt")))
    # print("Item path and name " + str(path.split(path.realpath("textfile.txt"))))

    # Get the modification time
    # t = time.ctime(path.getmtime("textfile.txt"))
    # print("Modified: " + str(t))
    # print("Modified: " + str(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))))
    # # Calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print("It's been ", str(td), "since last modification")
    print("Or " + str(td.total_seconds()), " seconds")


if __name__ == "__main__":
    main()
