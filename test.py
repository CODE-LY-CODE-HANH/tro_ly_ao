# import pyttsx3
#
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# rate = engine.getProperty('rate')
# volume = engine.getProperty('volume')
#
# for i in voices:
#     print(i)
#
# engine.setProperty('volume', volume - 0.0 ) # tu 0.0 -> 1.0
# engine.setProperty('rate', rate - 50)
# engine.setProperty('voice', voices[1].id)
# engine.say('Tôi là ai đây. bạn có thể cho tôi biết tôi là ai không nè. nếu được thì cảm ơn bạn nha')
# engine.runAndWait()
# from gtts import gTTS
# import playsound
# import os
#
# def speak(text):
#     print("Bot: {}".format(text))
#     tts = gTTS(text=text, lang="vi", slow=False)
#     tts.save("sound.mp3")
#     playsound.playsound("sound.mp3", True)
#     os.remove("sound.mp3")
#
# speak("thử lại xem nào . Liệu có xảy ra lỗi không ! Mong là chạy bình thường")

# from pynput.keyboard import Key, Listener
#
#
# def on_press(key):
#     print('{0} pressed'.format(
#         key))
#
#
# def on_release(key):
#     print('{0} release'.format(
#         key))
#     if key == Key.esc:
#         # Stop listener
#         return False
#
#
#
# # Collect events until released
# with Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()

# import speech_recognition as sr
#
# def get_audio_2():
#     global name
#     name = "test"
#     ear_robot = sr.Recognizer()
#     with sr.Microphone() as source:
#         # ear_robot.pause_threshold = 2
#         print("Đang nghe ===========================")
#         audio = ear_robot.listen(source , phrase_time_limit= 4)
#     try:
#         text = ear_robot.recognize_google(audio , language= "vi-VN")
#     except:
#         print("Nhận dạng giọng nói thất bại. Vui lòng nhập lệnh ở dưới")
#         # text = input("Mời nhập: ")
#         # text = get_audio_2()
#         return 0
#     return text.lower()
#
# # print(get_audio_2())
# while True:
#     test = get_audio_2().lower()
#     if "ok google".lower() in test:
#         print(test)
#         break
#     if test != "":
#         print(test)
#         continue
#     else:
#         print(test)
#         break
# def get_text():
#     for i in range(3):
#         text = get_audio_2()
#         if text:
#             return text.lower()
#         elif i < 2:
#             print(f"Tôi nghe không rõ. Bạn có thể nói lại được không nè ? {name}")
#     # time.sleep(3)
#     # stop()
#     return 0
# get_text()
# import os
# myPATH = r"D:\testcode\youtube\music_youtube"
# ds = os.listdir(myPATH)
# for i in ds:
#     print("\nĐang phát bài :  " + i)
#     os.system(myPATH + "\\" + i)
#     print("\nĐã phát xong bài : \t\t" + i)