from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=tyXMy1nPIWc&list=PLnpdZyv-BjINbUjmTUsyziHz_4fa9hM5G&index=2')
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()