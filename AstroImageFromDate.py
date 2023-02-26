# File Name: AstroImageFromDate.py
# Created By: Jacob Weiler
# Created On: 2023-02-26
# Last Modified: 2023-02-26
# Description: This program gets an image from the NASA API based on a date inputted by user, alongside with information of the image. This is a test to see how good 
#              Github Copilot is at writing code and allowing me to do some pet projects


# Create a program that asks for a date and then it pulls an image from the NASA API and displays it on the screen. 
# The program should also save the image to a file. 
# The program should also display the title of the image and the date it was taken. 
# The program should also display the explanation of the image.

import requests
import json
import os
import datetime
import sys

# Get the date from the user
date = input("Enter a date in the format YYYY-MM-DD: ")

# Check if the date is valid
try:
    datetime.datetime.strptime(date, "%Y-%m-%d")
except ValueError:
    print("Invalid date. Exiting...")
    sys.exit()

# Get the API key from the environment variable
api_key = os.environ.get("NASA_API_KEY")

# Get the data from the API
url = "https://api.nasa.gov/planetary/apod?api_key=" + api_key + "&date=" + date
response = requests.get(url)
data = json.loads(response.text)

# Print the data
print("Title: " + data["title"])
print("Date: " + data["date"])
print("Explanation: " + data["explanation"])

# Download the image
image_url = data["url"]
image_response = requests.get(image_url)
image_data = image_response.content

# Save the image
image_file = open("image.jpg", "wb")
image_file.write(image_data)
image_file.close()

# Display the image
os.system("display image.jpg")

# Delete the image
os.remove("image.jpg")
