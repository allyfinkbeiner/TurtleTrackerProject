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

# Parse Data
# Copy and paste a line of data as the lineString variable value
lineString = "20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0"
  
# Use the split command to parse the items in lineString into a list object
lineData = lineString
  
# Assign variables to specfic items in the list
record_id = lineData[]   # ARGOS tracking record ID
obs_date = lineData[2]   # Observation date
ob_lc = lineData[]       # Observation Location Class
obs_lat = lineData[]     # Observation Latitude
obs_lon = lineData[]     # Observation Longitude
  
# Print information to the use
print (f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")