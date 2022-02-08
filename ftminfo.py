from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import telegram

driver = webdriver.Chrome()
driver.get("https://www.binance.com/en/futures/FTMUSDT")
my_api_key = "5150330628:AAFDPyu7b-IxLXR_SbWOHX7CTOgvCHyLl2M"   #내 API 키 정보
chat_room_id = -748747493   # 채팅방 ID
my_bot = telegram.Bot(my_api_key)
while True:
    time.sleep(10)
    tvl = driver.find_elements_by_css_selector("div.price-text")  
    title = list()
    for i in tvl:
        title.append(i.text.strip())
    print(title)
    my_bot.sendMessage(chat_id=chat_room_id, text=('This is ftm info', 'price: %s'%(title.pop(0)), 'funding rate: %s'%(title.pop(1)), '24h change:%s'%(title.pop(2)), '24h volume usdt:%s'%(title.pop(5))))
    time.sleep(3600)
