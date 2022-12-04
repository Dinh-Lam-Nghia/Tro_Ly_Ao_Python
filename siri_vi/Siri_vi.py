# from PyQt5.QtWidgets import QApplication, QMainWindow
# from frontEnd import Ui_siri
# from main import siri
from thuVien import *

language_vi = 'vi'
wikipedia.set_lang('vi')  

def hien(self):
    self.uic.textEdit.setText("")
    for x in lists_speak:
        self.uic.textEdit.append(str(x)+"\n-------------------------------------------------")
    # time.sleep(5)
                

# Siri nói
def speak_vi(self, text):
    print("Siri: {}".format(text))
    
    # self.uic.textEdit.setText("")
    lists_speak.append("Siri: {}".format(text))
    hien(self)
    # for x in lists_speak:
    #     self.uic.textEdit.append(str(x)+"\n-------------------------------------------------")
        
    tts = gTTS(text=text, lang=language_vi, slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", True)
    # time.sleep(0.5)
    os.remove("sound.mp3")
    
# nhận âm thanh 
def get_audio_vi(self, name):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if not name:
            print("Bạn: ", end='')
        else: 
            print(name+": ", end='')
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            
            # self.uic.textEdit.setText("")
            lists_speak.append(name+": "+text)
            hien(self)
            # for x in lists_speak:
            #     self.uic.textEdit.append(str(x)+"\n-------------------------------------------------")
        
            print(text)
            # time.sleep(0.5)
            return text
        except:
            # lists_speak.append(name+": ....")
            # hien(self)
            print("...")
            return 0   
def get_text_vi(self, name):
    for i in range(5):
        print("-->Siri đang nghe....")
        text = self.get_audio_vi(name)
        if text:
            return text.lower()
        elif i < 5:
            self.speak_vi("Siri không nghe rõ. Bạn nói lại được không!")
    time.sleep(1.5)
    self.stop_vi()
    return 0                                                         
def get_text_auto_vi(self, name):
    print("-->Siri đang nghe....")
    i=0
    while True:
        i+=1
        if i >= 15:
            self.stop_vi()
            break;
        if i % 5 == 0:
            self.speak_vi("Bạn có cần Siri giúp gì nữa không?")
        text = self.get_audio_vi(name)
        if text:
            return text.lower()
        else: 
            continue;

# dừng
def stop_vi(self, name):
    self.speak_vi("Tạm biệt {}. Hẹn gặp lại bạn sau!". format(name))

# Chức năng hiển thị các khả năng của trợ lý ảo                                                              ok
def help_me_vi(self):
    self.speak_vi("""Siri có thể giúp bạn thực hiện các câu lệnh sau đây:
    1. Chào hỏi
    2. Hiển thị giờ
    3. Mở website, application
    4. Tìm kiếm trên Google
    5. Dự báo thời tiết
    6. Mở video nhạc
    7. Đọc báo hôm nay
    8. Kể bạn biết về thế giới """)

# Chức năng giao tiếp, chào hỏi                                                 ok
def hello_vi(self, name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        self.speak_vi("Chào buổi sáng bạn {}. Chúc bạn một ngày tốt lành. Siri có thể giúp gì được cho bạn!".format(name))
    elif 12 <= day_time < 18:
        self.speak_vi("Chào buổi chiều bạn {}. Siri có thể giúp gì được cho bạn!".format(name))
    else:
        self.speak_vi("Chào buổi tối bạn {}. Siri có thể giúp gì được cho bạn!".format(name))

# Chức năng hiển thị thời gian                                                  ok
def get_time_vi(self, text):
    now = datetime.datetime.now()
    if "giờ" in text:
        if "ngày" in text:
            self.speak_vi('Bây giờ là %d giờ %d phút, ngày %d tháng %d năm %d' % (now.hour, now.minute, now.day, now.month, now.year))
        else:
            self.speak_vi('Bây giờ là %d giờ %d phút' % (now.hour, now.minute))
            
    elif "ngày" in text:
        self.speak_vi("Hôm nay là ngày %d tháng %d năm %d" %(now.day, now.month, now.year))
    else:
        self.speak_vi("Siri chưa hiểu ý của bạn. Bạn nói lại được không?")


# Chức năng phát nhạc trên Youtube                                                              ok
def play_song_vi(self, name):
    self.speak_vi('Xin mời bạn chọn tên bài hát')
    mysong = self.get_text_vi(name)
    while True:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    self.speak_vi("Bài hát bạn yêu cầu đã được mở.")
    

# Chức năng mở ứng dụng hệ thống,website và chức năng tìm kiếm từ khóa trên Google                             ok
def open_application_vi(self, text):
    if "google" in text:
        self.speak_vi("Đã mở Google Chrome")
        os.startfile(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
    elif "word" in text:
        self.speak_vi("Đã mở Microsoft Word")
        os.startfile(r'C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE')
    elif "excel" in text:
        self.speak_vi("Đã mở Microsoft Excel")
        os.startfile(r'C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE')
    elif "PowerPoint" in text:
        self.speak_vi("Đã mở Microsoft PowerPoint")
        os.startfile(r'C:\Program Files (x86)\Microsoft Office\root\Office16\POWERPNT.EXE')
    elif "Visual Studio Code" in text:
        self.speak_vi("Đã mở Visual Studio Code")
        os.startfile(r'C:\Users\anhha\AppData\Local\Programs\Microsoft VS Code\Code.exe')
    elif "Eclipse" in text:
        self.speak_vi("Đã mở Eclipse ")
        os.startfile(r'C:\Users\anhha\eclipse\jee-2022-062\eclipse\eclipse.exe')
    else:
        self.speak_vi("Ứng dụng " + text + " chưa được cài đặt. Bạn hãy thử lại!")
def open_website_vi(self, text):
    reg_ex = re.search('mở (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://' + domain
        webbrowser.open(url)
        self.speak_vi("Trang web bạn yêu cầu đã được mở.")
        return True
    else:
        return False
def open_google_and_search_vi(self, text):
    search_for = text.split("tìm kiếm", 1)[1]
    self.speak_vi('Okay!')
    url = 'https://www.google.com/search?q=' + search_for
    webbrowser.open(url)
    
# Chức năng xem dự báo thời tiết                                                        ok
def current_weather_vi(self, name):
    self.speak_vi("Bạn muốn xem thời tiết ở đâu ạ.")
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = self.get_text_vi(name)
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
        Nhiệt độ trung bình là {temp} độ C
        Áp suất không khí là {pressure} Atmotphe
        Độ ẩm là {humidity}%
        Chúc bạn một ngày tốt lành!.""".format(
                                                day = now.day,
                                                month = now.month, 
                                                year= now.year, 
                                                temp = current_temperature, 
                                                pressure = current_pressure, 
                                                humidity = current_humidity,
                                            )
        self.speak_vi(content)
        time.sleep(2)
    else:
        self.speak_vi("Không tìm thấy địa chỉ của bạn")

# Chức năng đọc báo ngày hôm nay                                                     ok
def read_news_vi(self, name):
    self.speak_vi("Bạn muốn đọc báo về gì")
    
    queue = self.get_text_vi(name)
    # print(queue)
    params = {
        'apiKey': '91a2eb74c3f94a4eb35e8856fe64e4e8',
        "q": queue,
    }
    api_result = requests.get('https://newsapi.org/v2/everything?', params)
    api_response = api_result.json()
    
    self.speak_vi("Dưới đây là các tiêu đề liên quan đến {qu}" . format(qu = queue,))
    print("Tin tức: ")

    for number, result in enumerate(api_response['articles'], start=1):
        print(f"""Tin {number}:\nTiêu đề: {result['title']}\nTrích dẫn: {result['description']}\nLink: {result['url']}
    """)
        if number <= 3:
            webbrowser.open(result['url'])
            
# Chức năng tìm định nghĩa trên từ điển wikipedia                                                   ok
def tell_me_about_vi(self, name):
    try:
        self.speak_vi("Bạn muốn nghe về gì ạ")
        text = self.get_text_vi(name)
        contents = wikipedia.summary(text)#.split('\n')
        # speak_vi(contents[0])
        self.speak_vi(contents)
        # time.sleep(5)
        # for content in contents[0:]:
            # speak_vi("Bạn muốn nghe thêm không")
            # ans = get_text()
            # if "có" not in ans:
            #     break    
            # speak_vi(content)
            # time.sleep(0.5)

        self.speak_vi('Cảm ơn bạn đã lắng nghe!!!')
    except:
        self.speak_vi("Siri không định nghĩa được thuật ngữ của bạn.")     
        

            


            
    
    