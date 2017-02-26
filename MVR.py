from tkinter.filedialog import askopenfilename
from moviepy.editor import *


videoname = input("Enter name of video file:")
print("Locate image file:\n")
imageclip = ImageClip(askopenfilename())
print("Locate song file:\n")
audioclip = AudioFileClip(askopenfilename())
print(audioclip.duration)
imageclip = imageclip.set_audio(audioclip).set_duration(audioclip.duration)
print(imageclip.duration)
imageclip.write_videofile(videoname+".mp4", 60, "libx264")
