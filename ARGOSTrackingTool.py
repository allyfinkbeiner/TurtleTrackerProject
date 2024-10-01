#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Ally Finkbeiner (ally.finkbeiner@duke.edu)
# Date:   Fall 2024
#--------------------------------------------------------------

#Create a variable pointing to the data file
file_name = './data/raw/Sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a list
lineString = file_object.readline()

#Iterate through all lines in the data
while lineString:
    #Check if line is a data line
    if lineString[0] in ("#","u"):
        lineString = file_object.readline()
        continue

    #Split the string into a list of data items
    lineData = lineString.split()

    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]

    #Print the location of sara
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")

     # Move to the next line
    lineString = file_object.readline()
  
# Close the file
file_object.close()