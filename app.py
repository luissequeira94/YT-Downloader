from pytube import YouTube
from PIL import ImageTk
import moviepy.editor as mp
import os, tempfile, time

cwd = os.getcwd()

def Download(link, path):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        a = youtubeObject.download(output_path=path)
    except:
        print("An error has occurred")
    return a

def convert(path):
    filename = os.path.basename(path)
    clip = mp.VideoFileClip(r'{}'.format(path), verbose=False)
    clip.audio.write_audiofile(r'{}mp3'.format(filename[:-3]), verbose=False, logger= None)

link = input("Enter the YouTube video URL: ")
temp = tempfile.gettempdir()
files = os.listdir(temp)
for file in files:
     if file.endswith(".mp4"):
         os.remove(os.path.join(temp, file))
a = Download(link, temp)
convert(a)