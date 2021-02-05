import os
import playsound
import speech_recognition as sr
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch
import pyttsx3

wikipedia.set_lang('vi')
language = 'vi'


# path = ChromeDriverManager().install()
# đây là hàm chuyển văn bản thành giọng nói
def speak(text):
    print("Trợ Lý ảo:  ", text)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume - 0.0)  # tu 0.0 -> 1.0
    engine.setProperty('rate', rate - 50)
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


# đây là hàm chuyển giọng nói thành văn bản
def get_audio():
    ear_robot = sr.Recognizer()
    with sr.Microphone() as source:
        print("Trợ Lý Ảo: Đang Nghe ... \t\t  0.0 ")
        audio = ear_robot.listen(source, phrase_time_limit=5)
        try:
            text = ear_robot.recognize_google(audio, language="vi-VN")
            print("Tôi:  ", text)
            return text
        except:
            print("Lỗi rồi --__-- ")
            return 0


def get_audio_2():
    ear_robot = sr.Recognizer()
    with sr.Microphone() as source:
        # ear_robot.pause_threshold = 2
        print("Đang nghe ===========================")
        audio = ear_robot.listen(source, phrase_time_limit=4)
    try:
        text = ear_robot.recognize_google(audio, language="vi-VN")
    except:
        print("Nhận dạng giọng nói thất bại. Vui lòng nói lại <>")
        # text = input("Mời nhập: ")
        text = get_audio_2()
    return text.lower()


def stop():
    speak("Hẹn gặp lại bạn sau!")


# lấy văn bẩn mà người dùng nói
def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak(f"Tôi nghe không rõ. Bạn có thể nói lại được không nè ? {name}")
    time.sleep(3)
    stop()
    return 0


def hello(name):
    day_time = int(strftime('%H'))

    if 0 <= day_time < 11:
        speak(f'Chào buổi sáng bạn {name}. Chúc bạn một ngày tốt lành.')
    elif 11 <= day_time < 13:
        speak(f'Chào buổi trưa bạn {name}. Bạn đã được nghỉ trưa chưa vậy ?')
    elif 13 <= day_time < 18:
        speak(f'Chào buổi chiều bạn {name}. Bạn đã có dự định gì cho chiều nay chưa nè ? ')
    elif 18 <= day_time <= 23:
        speak(f'Chào buổi tối bạn {name}. Bạn ăn tối chưa ?')


def get_time(text):
    now = datetime.datetime.now()
    if 'giờ' in text:
        speak(f'Bây giờ là {now.hour}:{now.minute}:{now.second} ')
    elif "ngày" in text:
        speak(f'hôm nay là ngày {now.day} tháng {now.month} năm {now.year}')
    else:
        speak(f'Lý Hành chưa hiểu ý bạn. bạn có thể nói lại không ạ ?')


def help_me():
    speak("""
    Lý Hành có các chức năng sau:
    1. Chào hỏi
    2. ...
    """)

def open_google():
    speak("Mở trình duyệt web")
    while True:
        text = get_audio_2().lower()
        if "ok google".lower() in text:
            print(f"Trợ Lý Ảo : {text}")
            break
        if text != "":
            print(f"Trợ Lý Ảo : {text}")
            continue
        else:
            print(f"Trợ Lý Ảo : {text}")
            break

def main_brain():
    speak("Xin chào bạn. Bạn tên là gì ? Có thể nói tên bạn cho mình biết không ?")
    global name
    name = get_text()
    if name:
        speak(f'Chào bạn {name}')
        speak(f'Bạn cần Lý Hành giúp gì không ạ ?')
        while True:
            text = get_text()
            if not text:
                break
            elif ('tạm biệt' in text) or ('hẹn gặp lại' in text):
                stop()
                break
            elif ('chào trợ lý ảo' in text) or ('chào' in text):
                hello(name)
            elif 'có thể làm gì' in text:
                help_me()
            elif "hiện tại" in text:
                get_time(text)
            elif "mở" in text:
                open_google()
            else:
                speak('Chức năng chưa có. Bạn vui lòng chọn lại chức năng đã có trong menu nha ?')


main_brain()
