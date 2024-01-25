#!/usr/bin/env python3

"""Code Entry Point"""
# thrid party
import os
# import random

# local
import constants

# Does all the prerequisite work needed
empty_directories = False

for directory in constants.FULL_DIRECTORY_LIST:
    # Checks if Directories exits
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Creating Directory: " + directory)
    else:
        print(directory + " Found")

print()
# Checks if directories are empty

for directory in constants.SEED_DIRECTORY_LIST:
    if not os.listdir(directory):
        print(directory + " is empty")
        empty_directories = True

if empty_directories:
    print("Consult the README.md to fill directories")
    exit()

# Picks a video and background track at random
# Scrape the Web and find a random top post of the day
# Generate Audio for the Post
# Generate Captions for the Post

# Pick a background track
