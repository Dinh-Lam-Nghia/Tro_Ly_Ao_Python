
from PyQt5.QtWidgets import QApplication, QMainWindow

from frontEnd import Ui_siri
from thuVien import *

# from siri_en.Siri_en import index_en

# from command import *

language_vi = 'vi'
language_en = 'en'

class siri():
        
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_siri()
        self.uic.setupUi(self.main_win)
        self.uic.btn_reset.clicked.connect(lambda: self.clear_text())
        self.uic.stack.clicked.connect(lambda: self.index_main())
    
    def clear_text(self):
        # for i in range(len(lists_speak)):
        #     lists_speak.remove(lists_speak[i])
        del lists_speak[:]
        self.uic.textEdit.setText("")
        
    # cn_vi
    # cn_en
    from siri_en.Siri_en import (current_weather_en, get_audio_en,# hien,
                                 get_text_auto_en, get_text_en, get_time_en,
                                 hello_en, help_me_en, open_application_en,
                                 open_google_and_search_en, open_website_en,
                                 play_song_en, read_news_en, speak_en, stop_en,
                                 tell_me_about_en)
    from siri_vi.Siri_vi import (current_weather_vi, get_audio_vi,
                                 get_text_auto_vi, get_text_vi, get_time_vi,
                                 hello_vi, help_me_vi, open_application_vi,
                                 open_google_and_search_vi, open_website_vi,
                                 play_song_vi, read_news_vi, speak_vi, stop_vi,
                                 tell_me_about_vi)

    def index_main(self):
        self.speak_vi("Xin chào bạn, bạn cần Siri hổ trợ bằng tiếng Việt hay tiếng Anh.")
        self.speak_en("Hello, you need Siri support in Vietnamese or English")
        while True:
            text_main = self.get_text_main("")
            if not text_main:
                break;
            elif "dừng" in text_main or "tạm biệt" in text_main or "ngủ thôi" in text_main or "stop" in text_main or "goodbye" in text_main or "sleep" in text_main:
                self.stop_main()
                break
            elif "tiếng việt" in text_main or "vietnamese" in text_main:
                self.index_vi("")
                break
            elif "tiếng anh" in text_main or "english" in text_main:
                self.index_en("")  
                break  
            else:
                self.speak_vi("Siri không hỗ trợ ngôn ngữ đó. Bạn nói lại được không?")
                self.speak_en("Siri doesn't support that language. Can you repeat?")
                
    def index_vi(self, name):
        if not name:
            self.speak_vi("Xin chào tôi là Siri tiếng Việt, bạn tên là gì nhỉ?")
            name = self.get_text_vi("Bạn")
        else:
            self.speak_vi("Xin chào tôi là Siri tiếng Việt")
        if name:
            self.speak_vi("Chào bạn {}".format(name))
            self.speak_vi("Bạn cần Siri giúp gì ạ?")
            while True:
                text_vi = self.get_text_auto_vi(name)
                if not text_vi:
                    break
                elif "dừng" in text_vi or "tạm biệt" in text_vi or "ngủ thôi" in text_vi:# "chào siri" in text or 
                    self.stop_vi(name)
                    break
                elif "có thể làm gì" in text_vi:
                    self.help_me_vi()
                elif "chào siri" in text_vi:
                    self.hello_vi(name)
                elif "giờ" in text_vi or "ngày" in text_vi:
                    self.get_time_vi(text_vi)
                elif "mở nhạc" in text_vi or "nghe nhạc" in text_vi or "nhạc" in text_vi:
                    self.play_song_vi(name)
                elif "nói tiếng anh" in text_vi or "speak english" in text_vi:
                    self.index_en(name)
                    break
                elif "nói tiếng việt" in text_vi or "speak vietnamese" in text_vi:
                    self.speak_vi("Xin chào tôi là Siri tiếng Việt. Bạn cần Siri giúp gì ạ?")
                elif "mở" in text_vi:
                    if 'mở google và tìm kiếm' in text_vi:
                        self.open_google_and_search_vi(text_vi)
                    elif "." in text_vi:
                        self.open_website_vi(text_vi)
                    else:
                        self.open_application_vi(text_vi)
                elif "thời tiết" in text_vi :
                    self.current_weather_vi(name)
                elif "đọc báo" in text_vi:
                    self.read_news_vi(name)
                elif "muốn biết" in text_vi or "là gì" in text_vi:
                    self.tell_me_about_vi(name)
                else:
                    self.speak_vi("Bạn cần Siri giúp gì ạ?")
                    
    def index_en(self, name):
        if not name:
            self.speak_en("Hi I'm English Siri, what's your name?")
            name = self.get_text_en("You")
        else:
            self.speak_en("Hello, I'm Siri in Vietnamese.")
        if name:
            self.speak_en("Hello {}".format(name))
            self.speak_en("What do you need Siri for?")
            while True:
                text_en = self.get_text_auto_en(name)
                if not text_en:
                    break
                elif "stop" in text_en or "goodbye" in text_en or "sleep" in text_en:
                    self.stop_en(name)
                    break
                elif "what can" in text_en and "do" in text_en:
                    self.help_me_en()
                elif "hello siri" in text_en:
                    self.hello_en(name)
                elif  "time" in text_en or "day" in text_en or "date" in text_en or "current" in text_en:
                    self.get_time_en(text_en)
                elif "open music" in text_en or "listen to music" in text_en or "music" in text_en:
                    self.play_song_en(name)
                elif "nói tiếng anh" in text_en or "speak english" in text_en:
                    self.speak_en("Hi I'm Siri English. What do you need Siri for?")
                elif "nói tiếng việt" in text_en or "speak vietnamese" in text_en:
                    self.index_vi(name)
                    break
                elif "open" in text_en:
                    if 'open google and search' in text_en:
                        self.open_google_and_search_en(text_en)
                    elif "." in text_en:
                        self.open_website_en(text_en)
                    else:
                        self.open_application_en(text_en)
                elif "weather" in text_en :
                    self.current_weather_en(name)
                elif "read newspaper" in text_en:
                    self.read_news_en(name)
                elif "definition" in text_en:
                    self.tell_me_about_en(name)
                else:
                    self.speak_en("What do you need Siri for?")            
    
        
        
    # nhận dạng giọng nói và chuyển âm thang thành văn bản                          ok              
    def get_audio_main(self, name):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            if not name:
                print("Bạn(You): ", end='')
            else: 
                print(name+": ", end='')
            audio = r.listen(source, phrase_time_limit=5)
            try:
                text = r.recognize_google(audio, language="vi-VN")
                
                if not name:
                    lists_speak.append("Bạn(You): "+text)
                else: 
                    lists_speak.append(name+": "+text)
                self.hien_main()
                
                print(text)
                time.sleep(0.5)
                return text
            except:
                print("...")
                return 0
    def get_text_main(self, name):
        print("-->Siri đang nghe(Siri is listening)....")
        i=0
        while True:
            i+=1
            if i >= 15:
                self.stop_main()
                break;
            if i % 5 == 0:
                self.speak_vi("Bạn có cần Siri giúp gì nữa không?")
                self.speak_en("Do you need any more help from Siri?")
            text = self.get_audio_main(name)
            if text:
                return text.lower()
            else: 
                continue;  
            
    def stop_main(self):
        self.speak_vi("Tạm biệt. Hẹn gặp lại bạn sau!")
        self.speak_en("Goodbye. See you later!")
        
    def show(self):
        self.main_win.show()
        
    def hien_main(self):
        self.uic.textEdit.setText("")
        for x in lists_speak:
            self.uic.textEdit.append(str(x)+"\n-------------------------------------------------")
        # time.sleep(5)
    
# import threading

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = siri()
    main_win.show()
    sys.exit(app.exec_())
    
            
# main_win.hien_main()
    # GD = threading.Thread(target=main_win.hien_main, args=(1,))
    # GD.start()
    # GD.join()