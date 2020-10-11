"""
Written by: Turner Flynn, Evan Fulkerson, & Jackson Sommer
Date started: October 11, 2020
Purpose: Project submission for UCF KnightHacks 2020
Project Title: USV (Unmanned Submersible Vehicle) Trash Detection & Collection Unit - Project Kraken
"""

from labeldetection import detect_labels
from multipleobject import localize_objects
from bot import send_data, send_data_back


print("\nCollecting data...\n")

# Get data here
# data_locations = ["images/trashocean7.jpg","images/trashocean10.jpg","images/trashocean9.jpg" ]
data_locations = [send_data(), send_data(), send_data()]

print("Starting Object Detection...\n\n")

for i in range(3):

    # Detect multiple objects here. Get locations of objects and if confidence score is 0.6 or higher send for further collection.
    print("Object Detection Pass", i+1)
    print("\n")
    
    objects = localize_objects(data_locations[i])

    # Detect labels in image and collect for data analysis
    detect_labels(data_locations[i])

    # After detecting data, return data to robot for it to decide if trash retrieval is necessary
    send_data_back(objects)

    i += 1
    print("======================================================================================================================\n")