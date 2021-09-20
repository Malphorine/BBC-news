#Lazım olan paketləri import edirik

from bs4 import BeautifulSoup 
import requests
import pyttsx3

# Yazıdan səsə çevirmək üçün pyttsx3 modulundan istifadə edirik
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice', 'voice[0].id') #Voice (0-1) arası dəyişə bilir
engine.setProperty('rate', 145) #Rate səsin sürətidir

#Yazıdan səsə çevirmək üçün funksiya yaradırıq
def speak(text):
    engine.say(text) 
    engine.runAndWait()

url = ("https://www.bbc.com/news") #Yazını çəkəcəyimiz sayt
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html5lib')
speak("Here are some news") #Proqram açılanda ilk əvvəl bu söz deyiləcək
#Xəbərin qaynağını tapırıq.
xeber = soup.find('div',{'id':'latest-stories-tab-container'}).find_all("div", {'class':'gs-c-promo nw-c-promo gs-o-faux-block-link gs-u-pb gs-u-pb+@m nw-p-default gs-c-promo--inline gs-c-promo--stacked@m nw-u-w-auto gs-c-promo--flex'})
for ad in xeber: #a xəbərin başlığı, p isə xəbərin açıqlamasıdır
    name = ad.find('div', {'class':'gs-c-promo-body gel-1/2@xs gel-1/1@m gs-u-mt@m'}).find('a')
    desc = ad.find('div', {'class':'gs-c-promo-body gel-1/2@xs gel-1/1@m gs-u-mt@m'}).find('p')
    print(name.text)
    speak(name.text)
    print(desc.text)
    speak(desc.text)
    print('')
    print('----------------------------------------') #Boşluq buraxıldıqdan sonra ana səhifədə olan digər xəbərə keçəcək
    print('')
