#!/usr/bin/env python3

"""Code Entry Point"""
# thrid party
import os
import gtts
import pydub

# local
import constants

# Creates Directories
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


# turns post into audio
reddit_post = open("post.txt", "r").read()
post_audio = gtts.gTTS(reddit_post)
# saves the audio of the post to a file
post_audio.save(constants.GENERATED_AUDIO_DIRECTORY + "/post.mp3")
# speeds the audio of the post up by a bit
post_audio = pydub.AudioSegment.from_mp3(
    constants.GENERATED_AUDIO_DIRECTORY + "/post.mp3"
)
post_audio = post_audio.speedup(playback_speed=1.3)
# saves the sped up audio of the post to a file
post_audio.export(constants.GENERATED_AUDIO_DIRECTORY + "/post.mp3", format="mp3")

# grabs length of audio file

# grabs clip the video that is as long as the audio file

# merges the audio and video clip together

# saves the video clip to the final directory


print("Post Audio Generated")
exit()
