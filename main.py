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
             "Friday": ['CN', 'MIT', 'IS', 'AIML', 'DAA']}
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


def CN():
    # CN = driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[2]/div/div[2]/div/ol/li[6]/div[1]/div[3]/h2/a[1]')
    # CN = WebDriverWait(driver,15).until(EC.presence_of_element_located(By.XPATH, '//*[@id="yDmH0d"]/div[2]/div[2]/div[1]/div/div[2]/div[2]'))
    # CN.click()
    # sleep(3)
    global starttime
    starttime = dt.now() + timedelta(minutes=59)
    print(dt.now())
    print(starttime)
    bot = Bot()
    bot.login()
    link = "https://meet.google.com/lookup/drusihimug?authuser=0&hs=179"
    bot.attend(link)
    while dt.now() <= starttime:
        time.sleep(1)
    bot.quit()
    main()


def DAA():
    # driver.get("https://meet.google.com/lookup/fwp4lmwyav?authuser=0&hs=179")
    starttime = dt.now() + timedelta(minutes=59)
    link = "https://meet.google.com/lookup/fwp4lmwyav?authuser=0&hs=179"
    bot = Bot()
    bot.login()
    bot.attend(link)
    while dt.now() <= starttime:
        time.sleep(1)
    bot.quit()
    main()


def ST():
    link = "https://meet.google.com/lookup/hblv2osohr?authuser=0&hs=179"
    starttime = dt.now() + timedelta(minutes=59)
    bot = Bot()
    bot.login()
    bot.attend(link)
    while dt.now() <= starttime:
        time.sleep(1)
    bot.quit()
    main()


def MIT():
    link = "https://meet.google.com/lookup/f3lq6ew2w3?authuser=0&hs=179"
    starttime = dt.now() + timedelta(minutes=59)
    bot = Bot()
    bot.login()
    bot.attend(link)
    while dt.now() <= starttime:
        time.sleep(1)
    bot.quit()
    main()


def AIML():
    link = "https://meet.google.com/lookup/gnvv4nv5ay?authuser=0&hs=179"
    starttime = dt.now() + timedelta(minutes=59)
    bot = Bot()
    bot.login()
    bot.attend(link)
    while dt.now() <= starttime:
        time.sleep(1)
    bot.quit()
    main()


def IS():
    link = "https://meet.google.com/lookup/flvtihrhc6?authuser=0&hs=179"
    starttime = dt.now() + timedelta(minutes=59)
    bot = Bot()
    bot.login()
    bot.attend(link)
    while dt.now() <= starttime:
        time.sleep(1)
    bot.quit()
    main()


def main():
    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day, 8, 30) <= dt.now() < dt(dt.now().year, dt.now().month,
                                                                                   dt.now().day, 9, 28):
            daynum = dt.now().weekday()
            day = dayname[daynum]
            subject = timetable[day][0]
            if subject == 'CN':
                CN()
            elif subject == 'AIML':
                AIML()
            elif subject == 'MIT':
                MIT()
            elif subject == 'DAA':
                DAA()
            elif subject == 'ST':
                ST()
            elif subject == 'IS':
                IS()
        elif dt(dt.now().year, dt.now().month, dt.now().day, 9, 29) <= dt.now() < dt(dt.now().year, dt.now().month,
                                                                                     dt.now().day, 10, 28):
            daynum = dt.now().weekday()
            day = dayname[daynum]
            subject = timetable[day][1]
            if subject == 'CN':
                CN()
            elif subject == 'AIML':
                AIML()
            elif subject == 'MIT':
                MIT()
            elif subject == 'DAA':
                DAA()
            elif subject == 'ST':
                ST()
            elif subject == 'IS':
                IS()
        elif dt(dt.now().year, dt.now().month, dt.now().day, 10, 29) <= dt.now() < dt(dt.now().year, dt.now().month,
                                                                                      dt.now().day, 11, 28):
            daynum = dt.now().weekday()
            day = dayname[daynum]
            subject = timetable[day][2]
            if subject == 'CN':
                CN()
            elif subject == 'AIML':
                AIML()
            elif subject == 'MIT':
                MIT()
            elif subject == 'DAA':
                DAA()
            elif subject == 'ST':
                ST()
            elif subject == 'IS':
                IS()
        elif dt(dt.now().year, dt.now().month, dt.now().day, 11, 29) <= dt.now() < dt(dt.now().year, dt.now().month,
                                                                                      dt.now().day, 12, 30):
            daynum = dt.now().weekday()
            day = dayname[daynum]
            subject = timetable[day][3]
            if subject == 'CN':
                CN()
            elif subject == 'AIML':
                AIML()
            elif subject == 'MIT':
                MIT()
            elif subject == 'DAA':
                DAA()
            elif subject == 'ST':
                ST()
            elif subject == 'IS':
                IS()
        elif dt(dt.now().year, dt.now().month, dt.now().day, 21, 20) < dt.now() < dt(dt.now().year, dt.now().month,
                                                                                     dt.now().day, 22):
            daynum = dt.now().weekday()
            day = dayname[daynum]
            subject = timetable[day][4]
            if subject == 'CN':
                CN()
            elif subject == 'AIML':
                AIML()
            elif subject == 'MIT':
                MIT()
            elif subject == 'DAA':
                DAA()
            elif subject == 'ST':
                ST()
            elif subject == 'IS':
                IS()


if __name__ == "__main__":
    print("Hello from the Bot!")
    main()