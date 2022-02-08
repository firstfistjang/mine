from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import telegram

driver = webdriver.Chrome()
driver.get("https://tomb.com/")
my_api_key = "5150330628:AAFDPyu7b-IxLXR_SbWOHX7CTOgvCHyLl2M"   #내 API 키 정보
chat_room_id = -748747493   # 채팅방 ID
my_bot = telegram.Bot(my_api_key)
while True:
    time.sleep(30)
    tvl = driver.find_elements_by_css_selector(".text-2xl")  #TVL 불러오기
    title = list()
    for i in tvl:
        title.append(i.text.strip())
    con = title.pop(1)
    if len(con) == 12 :
        new_con = con[1:4] + con[5:8] + con[9:12]
    else: 
        new_con = con[1] + con[3:6] + con[7:10] + con[11:14]
    new_con = int(new_con) #TVL 숫자화 완료


    peg = driver.find_elements_by_css_selector("span.text-white.text-4xl.mt-1") #Peg 불러오기
    girl = list()
    for c in peg:
        girl.append(c.text.strip())
    conpeg = girl.pop(0)
    new_conpeg = conpeg[0] + conpeg[2:6]
    new_conpeg = float(new_conpeg) #Peg 숫자화 완료
    new_conpeg = new_conpeg * 0.0001 #Peg 원상복귀

    price = driver.find_elements_by_css_selector("span.text-white.text-md") #Price 불러오기
    baby = list()
    for a in price:
        baby.append(a.text.strip())


    if new_con < 700000000 or new_conpeg < 1: #비교하기
        new_con = format(new_con, ',') #TVL 3자리 컴마
        my_bot.sendMessage(chat_id=chat_room_id, text=('Tomb status is precatious alert period 30m', 'TVL: %s'%(new_con), 'Peg: %s'%(new_conpeg), 'Tomb price:%s'%(baby.pop(0)), 'Tshare price:%s'%(baby.pop(0))))
        time.sleep(1800)
        
    
    else:
        new_con = format(new_con, ',') #TVL 3자리 컴마
        my_bot.sendMessage(chat_id=chat_room_id, text=('Tomb status is stable alert period 1h', 'TVL: %s'%(new_con), 'Peg: %s'%(new_conpeg), 'Tomb price:%s'%(baby.pop(0)), 'Tshare price:%s'%(baby.pop(0))))
        time.sleep(3570)
        

    

#append 함수(멤버 메서드)를 이용하여 순차 보관
# list1 = list() #비어있는 리스트 만들기
# for i in range(1,30,3):
#     list1.append(i)
# print(list1)
# elem.send_keys("강선우")
# elem.send_keys(Keys.RETURN)
# driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[0].click()
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()