from gtts import *
import os
import playsound

def speak(text):
    print("Bot: {}".format(text))
    tts = gTTS(text=text, lang="vi", slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", True)
    os.remove("sound.mp3")

speak("thử lại xem nào . Liệu có xảy ra lỗi không ! Mong là chạy bình thường")