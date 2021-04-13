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

# chuyển văn bản thành âm thanh
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


    # tts = gTTS(text=text, lang="vi", slow=False)
    # tts.save("sound.mp3")
    # playsound.playsound("sound.mp3", True)
    # os.remove("sound.mp3")


# chuyển giọng nói thành văn bản
def get_audio():
    ear_robot = sr.Recognizer()
    with sr.Microphone() as source:
        print("Trợ Lý Ảo:  Đang nghe ! -- __ -- !")

        ear_robot.pause_threshold = 4
        audio = ear_robot.listen(source )
        # audio = ear_robot.listen(source, phrase_time_limit=5)
        try:
            text = ear_robot.recognize_google(audio, language="vi-VN")
            print("Tôi:  ", text)
            return text
        except:
            print("Trợ Lý Ảo:  Lỗi Rồi ! ... !")
            return 0


def get_audio_2():
    ear_robot = sr.Recognizer()
    with sr.Microphone() as source:
        ear_robot.pause_threshold = 2
        print("Đang nghe ===========================")
        audio = ear_robot.listen(source)
    try:
        text = ear_robot.recognize_google(audio, language="vi-VN")
    except:
        speak("Nhận dạng giọng nói thất bại. Vui lòng nhập lệnh ở dưới")
        text = input("Mời nhập: ")
    return text.lower()


def stop():
    speak("Hẹn gặp lại sau nha ! ... ")


def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("Trợ Lý Ảo không nghe rõ bạn nói. Vui lòng nói lại nha !")
    time.sleep(3)
    stop()
    return 0


def hello(name):
    day_time = int(strftime('%H'))
    if 0 <= day_time < 11:
        speak(f"Chào bạn {name}. Chúc bạn buổi sáng tốt lành.")
    elif 11 <= day_time < 13:
        speak(f"Chào bạn {name}. Chúc bạn có một buổi trưa thật vui vẻ.")
    elif 13 <= day_time < 18:
        speak(f"Chào bạn {name}. Chúc bạn buổi chiều vui vẻ.")
    elif 18 <= day_time < 22:
        speak(f"Chào bạn {name}. Tối rồi, Bạn đã cơm nước gì chưa ?")
    elif 22 <= day_time <= 23:
        speak(f"Chào Bạn {name}. Muộn rồi bạn nên đi nghủ sớm nha.")
    else:
        speak(f"Thời gian bên tôi chưa đúng hoặc gặp lỗi. Bạn nên xem lại nha.")


def get_time(text):
    now = datetime.datetime.now()
    if 'giờ' in text:
        speak(f"Bây giờ là {now.hour} giờ {now.minute} phút {now.second} giây")
    elif "ngày" in text:
        speak(f"hôm nay là ngày {now.day} tháng {now.month} năm {now.year}")
    else:
        speak("Lý Hành chưa hiểu ý bạn.")


def open_application(text):
    if "google" in text:
        speak("Mở Google Chrome")
        os.system("C:\\Users\\ASUS\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe")
    elif "word" in text:
        speak("Mở Microsoft Word")
        os.system("C:\\Users\\ASUS\\Desktop\\Word.lnk")
    elif "cốc cốc" in text:
        speak("Mở Cốc Cốc")
        os.system("C:\\Users\\ASUS\\AppData\\Local\\CocCoc\\Browser\\Application\\browser.exe")
    else:
        speak("Ứng dụng chưa cài đặt. Vui Lòng cài đặt cho tui nha !")


def open_website(text):
    reg_ex = re.search('mở (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = "https://www." + domain
        webbrowser.open(url)
        speak("Trang web bạn yêu cầu đã được mở. ")
        if input("Nếu muốn tiếp tục thì nhấn q: ") == "q":
            pass
        return True
    else:
        return False


def open_google_and_search(text):
    search_for = str(text).split("kiếm", 1)[1]
    url = f"https://www.google.com/search?q={search_for}"
    webbrowser.get().open(url)
    speak("Đây là thông tin bạn cần tìm")


def open_google_and_search2():
    speak("Nói thứ bạn cần tìm kiếm trên google")
    search = str(get_text()).lower()
    url = f"https://www.google.com/search?q={search}"
    webbrowser.get().open(url)
    speak("Đây là thông tin bạn cần tìm")


def send_email(text):
    speak("Bạn gửi email cho ai vậy nhỉ ?")
    recipient = get_text()
    if "minh" in recipient:
        speak("Nói cho tôi nội dung email bạn muốn gửi ! ... >")
        content = get_text()
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()
        mail.login("itaisv1999@gmail.com", "test7777")
        mail.sendmail("itaisv1999@gmail.com",
                      "huyph11247@gmail.com", str(content).encode("utf-8"))
        mail.close()
        speak("Email của bạn đã được gửi. Bạn vui lòng kiểm tra lại giúp !  >")
    else:
        speak("Lý Hành không hiểu bạn muốn gửi email cho ai  ...")


def current_weather():
    speak("Bạn muốn xem thời tiết ở đâu ạ.")
    # Đường dẫn trang web để lấy dữ liệu về thời tiết
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    # lưu tên thành phố vào biến city
    city = get_text()
    # nếu biến city != 0 và = False thì để đấy ko xử lí gì cả
    if not city:
        pass
    # api_key lấy trên open weather map
    api_key = "b4750c6250a078a943b3bf920bb138a0"
    # tìm kiếm thông tin thời thời tiết của thành phố
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    # truy cập đường dẫn của dòng 188 lấy dữ liệu thời tiết
    response = requests.get(call_url)
    # lưu dữ liệu thời tiết dưới dạng json và cho vào biến data
    data = response.json()
    # kiểm tra nếu ko gặp lỗi 404 thì xem xét và lấy dữ liệu
    if data["cod"] != "404":
        # lấy value của key main
        city_res = data["main"]
        # nhiệt độ hiện tại
        current_temperature = city_res["temp"]
        # áp suất hiện tại
        current_pressure = city_res["pressure"]
        # độ ẩm hiện tại
        current_humidity = city_res["humidity"]
        # thời gian mặt trời
        suntime = data["sys"]
        # 	lúc mặt trời mọc, mặt trời mọc
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        # lúc mặt trời lặn
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        # thông tin thêm
        wthr = data["weather"]
        # mô tả thời tiết
        weather_description = wthr[0]["description"]
        # Lấy thời gian hệ thống cho vào biến now
        now = datetime.datetime.now()
        # hiển thị thông tin với người dùng
        content = f"""
        Hôm nay là ngày {now.day} tháng {now.month} năm {now.year}
        Mặt trời mọc vào {sunrise.hour} giờ {sunrise.minute} phút
        Mặt trời lặn vào {sunset.hour} giờ {sunset.minute} phút
        Nhiệt độ trung bình là {current_temperature} độ C
        Áp suất không khí là {current_pressure} héc tơ Pascal
        Độ ẩm là {current_humidity}%
        """
        speak(content)
    else:
        # nếu tên thành phố không đúng thì nó nói dòng dưới 227
        speak("Không tìm thấy địa chỉ của bạn")


def play_youtube():
    speak("Nói nội dung bạn muốn tìm trên youtube")
    search = get_text()
    url = f"https://www.youtube.com/search?q={search}"
    webbrowser.get().open(url)
    speak("Đây là thứ mà tôi tìm được bạn xem qua nhé")


def play_youtube_2():
    speak("Nói nội dung bạn muốn tìm trên youtube")
    search = get_text()
    while True:
        result = YoutubeSearch(search, max_results=10).to_dict()
        if result:
            break
    url = f"https://www.youtube.com" + result[0]['url_suffix']
    webbrowser.get().open(url)
    speak("Đây là thứ mà tôi tìm được bạn xem qua nhé")
    print(result)


# url = 'https://api.unsplash.com/photos/random?client_id=' + \
#       api_key
def change_wallpaper():
    api_key = "XFyV6boeltUQBb9ROo5nPsWWvoPPDCPLRSwMaO_IXc4"
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
    speak("Hình nền máy tính bạn đã được thay đổi. Bạn ra home xem có đẹp không nha ?")


def play_music(path):
    # path là tham số chứa đường dẫn thư mục chứa nhạc
    myPATH = path
    # lấy file nhạc ra
    ds = os.listdir(myPATH)
    # dùng for mở từng bài nhạc
    for i in ds:
        print("\nĐang phát bài :  " + i)
        os.system(myPATH + "\\" + i)
        print("\nĐã phát xong bài : \t\t" + i)


def tell_me_about():
    try:
        speak("Hãy nói cho tôi nghe Bạn muốn tìm gì ạ ?")
        text = get_text()
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0])
        dem = 0
        for content in contents[1:]:
            if dem < 2:
                speak("Bạn có muốn biết thêm không ???")
                ans = get_text()
                if 'có' not in ans:
                    break
            dem += 1
            speak(content)
        speak("Đây là nội dung tôi vừa tìm được cảm ơn bạn đã lắng nghe")
    except:
        speak(f"{name} không định nghĩa được thuật ngữ của bạn !!!")


def help_me():
    speak(f"""
    {robot_name} có thể giúp bạn thực hiện các việc sau đây:
    1. chào hỏi
    2. Hiển thị giờ
    3. Mở website, ứng dụng desktop
    4. Tìm kiếm với google
    5. Gửi email
    6. Dự báo thời tiết
    7. Tìm kiếm video với youtube
    8. Thay đổi hình nền máy tính
    9. Định nghĩa với từ điển bách khoa toàn thư ( Wikipedia )
    10. Mở nhạc trong máy bạn
    """)

def main_brain():
    speak("Xin chào. Bạn tên là gì ?")
    global robot_name
    robot_name = "Lý hành"
    global name
    name = get_text()
    if name:
        speak(f'Xin chào bạn {name}.')
        speak(f'Bạn cần LÝ HÀNH giúp gì không ạ ?')
        while True:
            text = get_text()

            if not text:
                break
            elif ('tạm biệt' in text) or ('hẹn gặp lại' in text):
                stop()
                break
            elif "chào trợ lý" in text:
                hello(name)
            elif "hiện tại" in text:
                get_time(text)

            elif "mở" in text:

                if '.' in text:
                    open_website(text)
                elif "mở nhạc" in text:
                    speak("Ok. Tôi bắt đầu mở nhạc đây")
                    play_music(r"D:\testcode\youtube\music_youtube")
                else:
                    open_application(text)

            elif "tìm kiếm" in text:
                if str(text).split("kiếm", 1)[1] == "":
                    open_google_and_search2()
                else:
                    open_google_and_search(text)
            elif ("email" in text) or ("mail" in text) or ("gmail" in text):
                send_email(text)
            elif "thời tiết" in text:
                current_weather()
            elif 'youtube' in text:
                speak("Bạn muốn tìm kiếm đơn giản hay phức tạp")
                yeu_cau = get_text()
                if "đơn giản" in yeu_cau:
                    play_youtube()
                    if input():
                        pass
                elif "phức tạp" in yeu_cau:
                    play_youtube_2()
                    if input("Tiếp tục y/n: ") == "y":
                        pass
            elif "hình nền" in text:
                change_wallpaper()
            elif "định nghĩa" in text:
                tell_me_about()
            elif "có thể làm gì" in text:
                help_me()
            else:
                speak(f"Chức năng chưa có. Bạn vui lòng chọn lại chức năng đã có trong menu nha ! ")

main_brain()
