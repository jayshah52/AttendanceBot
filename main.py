from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
from datetime import datetime as dt
from datetime import timedelta
import time
from info import username, password

opt = Options()
opt.add_argument("--disable-infobars")
# opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block for permission pop ups.
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2,
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 2
})
dayname = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
timetable = {"Monday": ['MIT', 'IS', 'AIML', 'DAA', 'CN'], "Tuesday": ['IS', 'AIML', 'DAA', 'CN', 'AIML'],
             "Wednesday": ['AIML', 'DAA', 'CN', 'MIT'], "Thursday": ['DAA', 'CN', 'MIT', 'ST', 'ST'],
             "Friday": ['CN', 'MIT', 'IS', 'AIML', 'ST'], "Sunday":['DAA','CN','AIML','ST','CN']}
links = {"CN":"https://meet.google.com/lookup/drusihimug?authuser=0&hs=179","MIT":"https://meet.google.com/lookup/f3lq6ew2w3?authuser=0&hs=179"
            ,"DAA":"https://meet.google.com/lookup/fwp4lmwyav?authuser=0&hs=179","ST":"https://meet.google.com/lookup/hblv2osohr?authuser=0&hs=179",
         "AIML":"https://meet.google.com/lookup/gnvv4nv5ay?authuser=0&hs=179","IS":"https://meet.google.com/lookup/flvtihrhc6?authuser=0&hs=179"}
# print(timetable['Friday'])
path = "C:\Program Files (x86)\chromedriver.exe"
classroomlink = "https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&followup=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&flowName=GlifWebSignIn&flowEntry=ServiceLogin"


class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome(path, options=opt)

    def login(self):
        self.driver.get(classroomlink)
        sleep(3)
        email = self.driver.find_element_by_id("identifierId")
        email.send_keys(username + Keys.ENTER)
        sleep(2)
        pwd = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        pwd.send_keys(password + Keys.ENTER)
        sleep(15)

    def attend(self, link):
        self.link = link
        self.driver.get(self.link)
        sleep(14)
        try:
            dismiss = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/div[2]')
            self.driver.execute_script("arguments[0].click();", dismiss)
        except:
            self.driver.implicitly_wait(3)
            dismiss = self.driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/div[3]/div/div[2]')
            self.driver.execute_script("arguments[0].click();", dismiss)

        sleep(6)
        try:
            joinnow = self.driver.find_element_by_xpath(
                '//*[@id="yDmH0d"]/c-wiz/div/div/div[5]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span')
            # self.driver.execute_script("arguments[0].click();", joinnow)
            #print(joinnow)
            joinnow.click()
        except:
            self.driver.implicitly_wait(5)
            joinnow = self.driver.find_element_by_xpath(
                '//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span')
            self.driver.execute_script("arguments[0].click();", joinnow)
            print(joinnow)

    def quit(self):
        self.driver.quit()

def driver(subject,mins):
    global starttime
    starttime = dt.now() + timedelta(minutes=mins)
    link = links[subject]
    #print(dt.now())
    #print(starttime)
    bot = Bot()
    bot.login()
    bot.attend(link)
    while dt.now() <= starttime:
        time.sleep(1)
    print(f"Successfully attened {subject}  ")
    bot.quit()

    #main()

def main():
    print(dt.now())
    daynum = dt.now().weekday()
    day = dayname[daynum]
    mins = 59
    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day,8,30) <= dt.now() < dt(dt.now().year, dt.now().month,
                                                                                   dt.now().day, 9,29):
            #subject = timetable[day][0]
            subject = timetable[day][0]
            driver(subject,mins)
        elif dt(dt.now().year, dt.now().month, dt.now().day, 9,29) <= dt.now() < dt(dt.now().year, dt.now().month,
                                                                                     dt.now().day, 10,28):

            #subject = timetable[day][1]
            subject = timetable[day][1]
            driver(subject,mins)
        elif dt(dt.now().year, dt.now().month, dt.now().day, 10,28) <= dt.now() < dt(dt.now().year, dt.now().month,
                                                                                      dt.now().day, 11,27):
            subject = timetable[day][2]
            driver(subject,mins)

        elif dt(dt.now().year, dt.now().month, dt.now().day, 11,27) <= dt.now() < dt(dt.now().year, dt.now().month,
                                                                                      dt.now().day, 12,26):

            subject = timetable[day][3]
            driver(subject, mins)
        elif dt(dt.now().year, dt.now().month, dt.now().day,16) <= dt.now() < dt(dt.now().year, dt.now().month,
                                                                                     dt.now().day,17,50):

            try:
                subject = timetable[day][4]
                driver(subject,111)
            except:
                break

if __name__ == "__main__":
    print("Hello from the Bot!")
    main()
