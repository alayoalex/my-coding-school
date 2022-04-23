from pytube import YouTube
from tqdm import tqdm

# misc
import os
import shutil
import math
import datetime

def show_progress_bar(stream: Stream, chunk: bytes, bytes_remaining: int):


video = YouTube('https://www.youtube.com/watch?v=tyXMy1nPIWc&list=PLnpdZyv-BjINbUjmTUsyziHz_4fa9hM5G&index=2')
#print(video.streams.all())
video.register_on_progress_callback(show_progress_bar)
video.streams.get_by_itag(18).download(filename='Building a Portfolio Website with React - Setting up the Project - Part 2')
print('Complete')