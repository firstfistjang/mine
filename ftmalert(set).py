import telegram
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
token = "5113976949:AAHIFwv8F_adekpg6gVFlpqA__SPNJGHhQg"
id = "1954206029"
bot = telegram.Bot(token)
driver = webdriver.Chrome()
driver.get("https://www.binance.com/en/futures/FTMUSDT")
while True:
    time.sleep(10)
    ftm = driver.find_elements_by_css_selector("div.price-text")  #ftm 불러오기
    title = list()
    for i in ftm:
        title.append(i.text.strip())
    market = title.pop(0)
    new_market = market[0] + market[2:6]
    new_market = float(new_market)
    new_market = new_market * 0.0001
    print(new_market)
    standard = 2.28
    a = standard * 1.14 # -70%정도
    if new_market > a :
            bot.send_message(chat_id=id, text='Market Price: %s'%(new_market)) # 답장 보내기
            time.sleep(1800)
    
    
      