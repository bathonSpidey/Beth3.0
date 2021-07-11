from gtts import gTTS
import pyglet
import os
from time import sleep


tts = gTTS('hello, I am Beth, Your personal assistant', lang='en-us')
filename='temp.mp3'
tts.save(filename)
music = pyglet.media.load(filename, streaming=False)
music.play()

sleep(music.duration) #prevent from killing
os.remove(filename)