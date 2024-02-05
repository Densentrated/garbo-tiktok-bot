#!/usr/bin/env python3

"""Code Entry Point"""
# thrid party
import os
import gtts
import pydub
import random
import praw
from moviepy.editor import AudioFileClip, VideoFileClip


# local
import constants
import private_constants

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

# Picks a video and background track at random
# Scrape the Web and find a random top post of the day, repeat process until post has correct amount of words
reddit_instance = praw.Reddit(
    client_id=private_constants.CLIENT_ID,
    client_secret=private_constants.CLIENT_SECRET,
    user_agent=private_constants.USER_AGENT,
)
subreddit_string = constants.SUBREDDIT_LIST[
    random.randint(0, (len(constants.SUBREDDIT_LIST) - 1))
]
subreddit = reddit_instance.subreddit(subreddit_string)
posts = [post for post in subreddit.hot(limit=2000)]

enough_words = False
while not enough_words:
    random_post = random.choice(posts)
    if (len(random_post.selftext) > 1250) and (len(random_post.selftext) < 2200):
        enough_words = True
    print("post wrong size")
print("post found")

with open("post.txt", "w") as f:
    f.write(random_post.title + "\n")
    f.write(random_post.selftext)
print("post written to file")

# Generate Captions for the Post
# turns post into audio
reddit_post = open("post.txt", "r").read()
# TODO change tts library to better voices
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
audio_clip = pydub.AudioSegment.from_file(
    constants.GENERATED_AUDIO_DIRECTORY + "/post.mp3"
)
audio_duration = int(audio_clip.duration_seconds + 1)
# grabs clip the video that is as long as the audio file
seed_video_duration = VideoFileClip(
    constants.BACKGROUND_VIDEO_DIRECTORY + "/Video0.mp4"
)
seed_video_duration = int(seed_video_duration.duration - 1)

final_post_start = random.randint(audio_duration, seed_video_duration)
final_post_end = final_post_start - audio_duration
final_post = VideoFileClip(
    constants.BACKGROUND_VIDEO_DIRECTORY + "/Video0.mp4"
).subclip(final_post_end, final_post_start)

# overlays the speech audio over the video

final_post_audio = AudioFileClip(constants.GENERATED_AUDIO_DIRECTORY + "/post.mp3")
final_post = final_post.set_audio(final_post_audio)
# overlays music over the video

# renders the video
final_post.write_videofile(
    constants.GENERATED_VIDEO_DIRECTORY + "/video.mp4",
    codec="libx264",
    audio_codec="mp3",
    bitrate="5000k",
)

exit()
