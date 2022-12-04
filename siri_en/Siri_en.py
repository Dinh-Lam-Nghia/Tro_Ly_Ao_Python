# from PyQt5.QtWidgets import QApplication, QMainWindow
# from frontEnd import Ui_siri
# from main import siri
from thuVien import *

language_vi = 'en'
wikipedia.set_lang('en')

def hien(self):
    self.uic.textEdit.setText("")
    for x in lists_speak:
        self.uic.textEdit.append(str(x)+"\n-------------------------------------------------")
    # time.sleep(5)

# Siri nói

def speak_en(self, text):
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
def get_audio_en(self, name):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if not name:
            print("Bạn: ", end='')
        else: 
            print(name+": ", end='')
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio, language="en-US")
            
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
def get_text_en(self, name):
    for i in range(5):
        print("-->Siri is listening....")
        text = self.get_audio_en(name)
        if text:
            return text.lower()
        elif i < 5:
            self.speak_en("Siri can't hear well. Can you repeat!")
    time.sleep(1.5)
    self.stop_vi()
    return 0   
def get_text_auto_en(self, name):
    print("-->Siri is listening....")
    i=0
    while True:
        i+=1
        if i >= 15:
            self.stop_en()
            break;
        if i % 5 == 0:
            self.speak_en("Do you need any more help from Siri?")
        text = self.get_audio_vi(name)
        if text:
            return text.lower()
        else: 
            continue;
        
# dừng
def stop_en(self, name):
    self.speak_en("Goodbye {}. See you later!". format(name))


# Chức năng hiển thị các khả năng của trợ lý ảo                                                              ok
def help_me_en(self):
    self.speak_en("""The Siri can help you with the following commands:
    1. Hello
    2. Time display
    3. Open website, application
    4. Search on Google
    5. Weather forecast
    6. Open music video
    7. Read today's newspaper
    8. Tell you about the world """)

# Chức năng giao tiếp, chào hỏi
def hello_en(self, name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        self.speak_en("Good morning friend {}. Wish you a good day. What Siri can do for you!".format(name))
    elif 12 <= day_time < 18:
        self.speak_en("Good afternoon friends {}. What Siri can do for you!".format(name))
    else:
        self.speak_en("Good evening friends {}. What Siri can do for you!".format(name))
  
# Chức năng hiển thị thời gian                                                  ok
def get_time_en(self, text):
    now = datetime.datetime.now()
    if "hour" in text:
        if "day" in text:
            self.speak_en('Now is %d hour %b minute, day %d month %d year %d' % (now.hour, now.minute, now.day, now.month, now.year))
        else:
            self.speak_en('Now it\'s %d hours %d minutes' % (now.hour, now.minute))
            
    elif "day" in text:
        self.speak_en("Today is the date %d month %d year %d" %(now.day, now.month, now.year))
    else:
        self.speak_en("Siri doesn't understand what you mean. Can you repeat?")
       
# Chức năng phát nhạc trên Youtube                                                              ok
def play_song_en(self, name):
    self.speak_en('Please choose the name of the song')
    mysong = self.get_text_en(name)
    while True:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    self.speak_en("The song you requested has already been played.")

# Chức năng mở ứng dụng hệ thống, website và chức năng tìm kiếm từ khóa trên Google                             ok
def open_application_en(self, text):
    if "google" in text:
        self.speak_en("Opened Google Chrome")
        os.startfile(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
    elif "word" in text:
        self.speak_en("Opened Microsoft Word")
        os.startfile(r'C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE')
    elif "excel" in text:
        self.speak_en("Opened Microsoft Excel")
        os.startfile(r'C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE')
    elif "PowerPoint" in text:
        self.speak_en("Opened Microsoft PowerPoint")
        os.startfile(r'C:\Program Files (x86)\Microsoft Office\root\Office16\POWERPNT.EXE')
    elif "Visual Studio Code" in text:
        self.speak_en("Opened Visual Studio Code")
        os.startfile(r'C:\Users\anhha\AppData\Local\Programs\Microsoft VS Code\Code.exe')
    elif "Eclipse" in text:
        self.speak_en("Opened Eclipse ")
        os.startfile(r'C:\Users\anhha\eclipse\jee-2022-062\eclipse\eclipse.exe')
    else:
        self.speak_en("The " + text + " application is not installed. Please try again!")
def open_website_en(self, text):
    reg_ex = re.search('open (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://' + domain
        webbrowser.open(url)
        self.speak_en("The website you requested has been opened.")
        return True
    else:
        return False
def open_google_and_search_en(self, text):
    search_for = text.split("search", 1)[1]
    self.speak_en('Okay!')
    url = 'https://www.google.com/search?q=' + search_for
    webbrowser.open(url)

# Chức năng xem dự báo thời tiết                                                        ok
def current_weather_en(self, name):
    self.speak_en("Where do you want to see the weather?.")
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = self.get_text_en(name)
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
        content = """Today is {day} month {month} year {year}
         Average temperature is {temp} degrees C
         Air pressure is {pressure} Atmotphe
         Humidity is {humidity}%
         Wish you a good day!.""".format(
                                            day = now.day,
                                            month = now.month, 
                                            year= now.year, 
                                            temp = current_temperature, 
                                            pressure = current_pressure, 
                                            humidity = current_humidity,
                                        )
        self.speak_en(content)
        time.sleep(2)
    else:
        self.speak_en("Your address could not be found")

# Chức năng đọc báo ngày hôm nay                                                     ok
def read_news_en(self, name):
    self.speak_en("What do you want to read about?")
    
    queue = self.get_text_en(name)
    # print(queue)
    params = {
        'apiKey': '91a2eb74c3f94a4eb35e8856fe64e4e8',
        "q": queue,
    }
    api_result = requests.get('https://newsapi.org/v2/everything?', params)
    api_response = api_result.json()
    
    self.speak_en("Here are the titles related to {qu}" . format(qu = queue,))
    print("News: ")

    for number, result in enumerate(api_response['articles'], start=1):
        print(f"""news {number}:\nTitle: {result['title']}\nQuote: {result['description']}\nLink: {result['url']}
    """)
        if number <= 3:
            webbrowser.open(result['url'])
           
# Chức năng tìm định nghĩa trên từ điển wikipedia                                                   ok
def tell_me_about_en(self, name):
    try:
        self.speak_en("What do you want to hear about?")
        text = self.get_text_en(name)
        contents = wikipedia.summary(text)#.split('\n')
        # speak_en(contents[0])
        self.speak_en(contents)
        # time.sleep(5)
        # for content in contents[0:]:
            # speak_en("Bạn muốn nghe thêm không")
            # ans = get_text()
            # if "có" not in ans:
            #     break    
            # speak_en(content)
            # time.sleep(0.5)

        self.speak_en('Thank you for listening!!!')
    except:
        self.speak_en("Siri doesn't define your term.")