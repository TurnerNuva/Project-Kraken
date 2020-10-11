import random

def send_data():

    # This is simulating the robot taking pictures and sending them to the cloud
    filename = 'images/trashocean' + str(random.randrange(3, 10, 1)) + '.jpg'

    print(filename)

    return filename 

def send_data_back(data):
    
    # This is simulating the robot recieiving the processed image data and acting upon it
    print("\nProcessed Data Recieved\n\nDisplaying Results:\n")
    print(data)