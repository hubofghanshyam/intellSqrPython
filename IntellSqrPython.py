from tkinter import *
from tkinter.messagebox import showinfo
from gtts import gTTS
import speech_recognition as sr
import os

mainwindow= Tk()
mainwindow.title( 'DataF1air Text-To-Speech and Speech-To-Text Converter')
mainwindow. geometry( ' 500x500 ' )
mainwindow. resizable (0, 0)
mainwindow. configure (bg= 'yellow ' )

def say(textl):
  language ='en'
  speech = gTTS(text = textl, lang = language, slow = False)
  speech. save ("text. mp3")
  os. text.mp3")

def recordvoice():
  while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
      audio=r. listen( source)
      try :
        textl = r. recognize_google ( audio, - IN " )
      except :
        pass
      return textl