# Python Voice Assistant


A simple python voice assistant inspired by J.A.R.V.I.S. For tutorial on how to build it from scratch, visit https://thecodingpie.com


## Technologies Used
It uses SpeechRecognition and PyAudio modules to recognize speech through Microphone. Then for converting speech to text, it uses gTTS. pyttsx3 for generating computer voice.

## What it can do?
Currently it can reply to these commands:

- name
- today's date 
- current time
- how are you? 
- and finally if we say "quit" or "exit", it will terminate.

***Note: If you are using Ubuntu, then you may get some errors of the form "ALSA lib [...] Unknown PCM". To suppress those errors, see ![https://stackoverflow.com/questions/7088672/pyaudio-working-but-spits-out-error-messages-each-time](this Stackoverflow answer).***
