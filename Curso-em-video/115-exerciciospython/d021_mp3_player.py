'''import pygame
pygame.init()
pygame.mixer.music.load('eleanor.mp3')
pygame.mixer.music.play()'''

'''from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_mp3('eleanor.mp3')
play(song)'''

from playsound import playsound
playsound('C:\eleanor.mp3')