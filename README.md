# garbo-tiktok-bot

A Python Script that creates those robot text reddit videos that you keep seeing.

# Roadmap

- [x] Check for Prerequisites
- [x] Create TTS Audio of a reddit post
- [x] Attach TTS Audio to Video
- [x] Make a Video with TTS audio from a reddit post
- [ ] General Code Cleanup
- [ ] Add background music to the video
- [ ] Add captions to the video front in center
- [ ] Create a tool to format the videos correct first

#Setup

- First You need to install the following dependencies
  - `MoviePy => 1.0.3`
  - `requests => 2.31.0`
  - `gTTS => 2.5.1`
  - `audioread => 3.0.1`
  - `pydub => 0.21.1`
- Next, Create a file called "private_constants.py", and a reddit API app
- fill the info out in the following format
  - `CLIENT_ID = "Your ID`
  - `CLIENT_SECRET = "Your Client Secret"`
  - `USER_AGENT = "Your User Agent`
