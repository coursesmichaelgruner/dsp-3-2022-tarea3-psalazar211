from pickle import TRUE
import speech_recognition as sr
from playsound import playsound 
import os
import wave
import pyaudio
import time


def get_audio(filename, tiempo):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Di algo')
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = r.listen(source,timeout= tiempo/2,phrase_time_limit= tiempo/2)

            sampleRate = 44100.0 # hertz
            duration = 1.0 # seconds
            frequency = 440.0 # hertz
            obj = wave.open(filename,'wb')
            obj.setnchannels(1) # mono
            obj.setsampwidth(2)
            obj.setframerate(sampleRate)
            obj.writeframes(audio.get_wav_data())
            obj.close()
            ding_wav = wave.open(filename, 'rb')
            ding_data = ding_wav.readframes(ding_wav.getnframes())
            audio = pyaudio.PyAudio()
            stream_out = audio.open(
                format=audio.get_format_from_width(ding_wav.getsampwidth()),
                channels=ding_wav.getnchannels(),
                rate=ding_wav.getframerate(), input=False, output=True)
            stream_out.start_stream()
            stream_out.write(ding_data)
    #time.sleep(0.2)
            stream_out.stop_stream()
            stream_out.close()
            audio.terminate() 
        except: 
            print("Lo siento no te entendi")
       

tiempo = float(input("Escriba tiempo de atraso D:"))
while True:
    get_audio("audio.wav", tiempo)
