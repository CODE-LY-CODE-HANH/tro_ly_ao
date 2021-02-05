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

wikipedia.set_lang('vi')
language = 'vi'
path = ChromeDriverManager().install()


def speak(text):
    print("Bot: {}".format(text))
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", False)
    os.remove("sound.mp3")


def get_audio():
    print("\nBot: \tĐang nghe \t --__-- \n")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end='')
        audio = r.listen(source, phrase_time_limit=8)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            return text.lower()
        except:
            print("...")
            return 0


def stop():
    speak("Hẹn gặp lại bạn sau!")
    time.sleep(2)


def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("Máy không nghe rõ. Bạn nói lại được không!")
            time.sleep(3)
    time.sleep(2)
    stop()
    return 0


def hello(name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        speak("Chào buổi sáng bạn {}. Chúc bạn một ngày tốt lành.".format(name))
    elif 12 <= day_time < 18:
        speak("Chào buổi chiều bạn {}. Bạn đã dự định gì cho chiều nay chưa.".format(name))
    else:
        speak("Chào buổi tối bạn {}. Bạn đã ăn tối chưa nhỉ.".format(name))
    time.sleep(5)


def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        speak('Bây giờ là %d giờ %d phút %d giây' % (now.hour, now.minute, now.second))
    elif "ngày" in text:
        speak("Hôm nay là ngày %d tháng %d năm %d" %
              (now.day, now.month, now.year))
    else:
        speak("Bot chưa hiểu ý của bạn. Bạn nói lại được không?")
    time.sleep(4)


def open_application(text):
    if "google" in text:
        speak("Mở Google Chrome")
        time.sleep(2)
        os.startfile('Desktop\\Google Chrome')
    elif "word" in text:
        speak("Mở Microsoft Word")
        time.sleep(2)
        os.startfile('Desktop\\Google Chrome')
    elif "excel" in text:
        speak("Mở Microsoft Excel")
        time.sleep(2)
        os.startfile('Desktop\\Google Chrome')
    else:
        speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")
        time.sleep(3)


def open_website(text):
    reg_ex = re.search('mở (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain
        webbrowser.open(url)
        speak("Trang web bạn yêu cầu đã được mở.")
        time.sleep(3)
        return True
    else:
        return False


def open_google_and_search(text):
    search_for = text.split("kiếm", 1)[1]
    speak('Okay!')
    driver = webdriver.Chrome(path)
    driver.get("http://www.google.com")
    que = driver.find_element_by_xpath("//input[@name='q']")
    que.send_keys(str(search_for))
    que.send_keys(Keys.RETURN)
    time.sleep(10)


def send_email(text):
    speak('Bạn gửi email cho ai nhỉ')
    time.sleep(2)
    recipient = get_text()
    if 'yến' in recipient:
        speak('Nội dung bạn muốn gửi là gì')
        time.sleep(3)
        content = get_text()
        # mail = smtplib.SMTP('smtp.gmail.com', 587)
        # mail.ehlo()
        # mail.starttls()
        # mail.login('luongngochungcntt@gmail.com', 'hung23081997')
        # mail.sendmail('luongngochungcntt@gmail.com',
        #               'hungdhv97@gmail.com', content.encode('utf-8'))
        # mail.close()
        speak('Email của bạn vùa được gửi. Bạn check lại email nhé hihi.')
        time.sleep(4)
    else:
        speak('Bot không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không?')
        time.sleep(5)


def current_weather():
    speak("Bạn muốn xem thời tiết ở đâu ạ.")
    time.sleep(3)
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = get_text()
    if not city:
        pass
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temperature = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        suntime = data["sys"]
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.datetime.now()
        content = """
        Hôm nay là ngày {day} tháng {month} năm {year}
        Mặt trời mọc vào {hourrise} giờ {minrise} phút
        Mặt trời lặn vào {hourset} giờ {minset} phút
        Nhiệt độ trung bình là {temp} độ C
        Áp suất không khí là {pressure} héc tơ Pascal
        Độ ẩm là {humidity}%
        Trời hôm nay quang mây. Dự báo mưa rải rác ở một số nơi.""".format(day=now.day, month=now.month, year=now.year,
                                                                           hourrise=sunrise.hour,
                                                                           minrise=sunrise.minute,
                                                                           hourset=sunset.hour, minset=sunset.minute,
                                                                           temp=current_temperature,
                                                                           pressure=current_pressure,
                                                                           humidity=current_humidity)
        speak(content)
        time.sleep(28)
    else:
        speak("Không tìm thấy địa chỉ của bạn")
        time.sleep(2)


def play_song():
    speak('Xin mời bạn chọn tên bài hát')
    time.sleep(2)
    mysong = get_text()
    while True:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    speak("Bài hát bạn yêu cầu đã được mở.")
    time.sleep(3)


def change_wallpaper():
    api_key = 'RF3LyUUIyogjCpQwlf-zjzCf1JdvRwb--SLV6iCzOxw'
    url = 'https://api.unsplash.com/photos/random?client_id=' + \
          api_key  # pic from unspalsh.com
    f = urllib2.urlopen(url)
    json_string = f.read()
    f.close()
    parsed_json = json.loads(json_string)
    photo = parsed_json['urls']['full']
    # Location where we download the image to.
    urllib2.urlretrieve(photo, "D:\\Download____CocCoc\\a.png")
    image = os.path.join("D:\\Download____CocCoc\\a.png")
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image, 3)
    speak('Hình nền máy tính vừa được thay đổi')
    time.sleep(3)


def tell_me_about():
    try:
        speak("Bạn muốn nghe về gì ạ")
        time.sleep(2)
        text = get_text()
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0].split(".")[0])
        time.sleep(10)
        for content in contents[1:]:
            speak("Bạn muốn nghe thêm không")
            time.sleep(2)
            ans = get_text()
            if "có" not in ans:
                break
            speak(content)
            time.sleep(10)

        speak('Cảm ơn bạn đã lắng nghe!!!')
        time.sleep(3)
    except:
        speak("Bot không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại")
        time.sleep(5)


def help_me():
    speak("""Bot có thể giúp bạn thực hiện các câu lệnh sau đây:
    1. Chào hỏi
    2. Hiển thị giờ
    3. Mở website, application
    4. Tìm kiếm trên Google
    5. Gửi email
    6. Dự báo thời tiết
    7. Mở video nhạc
    8. Thay đổi hình nền máy tính
    9. Đọc báo hôm nay
    10. Kể bạn biết về thế giới """)
    time.sleep(27)


def read_news():
    speak("Chức năng còn đang xây dựng. Vui lòng chọn chức năng khác")
    time.sleep(5)


def assistant():
    speak("Xin chào, bạn tên là gì nhỉ?")
    time.sleep(2)
    name = get_text()
    if name:
        speak("Chào bạn {}".format(name))
        speak("Bạn cần Bot Alex có thể giúp gì ạ?")
        time.sleep(3)
        while True:
            text = get_text()
            if not text:
                break
            elif "dừng" in text or "tạm biệt" in text or "chào robot" in text or "ngủ thôi" in text:
                stop()
                break
            elif "có thể làm gì" in text:
                help_me()
            elif "chào" in text:
                hello(name)
            elif "giờ" in text or "ngày" in text:
                get_time(text)
            elif 'mở google và tìm kiếm' in text:
                open_google_and_search(text)
            elif "mở " in text:
                open_website(text)
            elif "ứng dụng" in text:
                speak("Tên ứng dụng bạn muốn mở là ")
                time.sleep(3)
                text1 = get_text()
                open_application(text1)
            elif "email" in text or "mail" in text or "gmail" in text:
                send_email(text)
            elif "thời tiết" in text:
                current_weather()
            elif "chơi nhạc" in text:
                play_song()
            elif "hình nền" in text:
                change_wallpaper()
            elif "đọc báo" in text:
                read_news()
            elif "định nghĩa" in text:
                tell_me_about()
            else:
                speak("Bạn cần Bot giúp gì ạ?")
                time.sleep(2)


assistant()