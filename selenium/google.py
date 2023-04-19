from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# 로딩시간
import time
#파일 이미지 다운로드
import urllib.request

# chrome_options = Options()
# chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()
# 구글 이미지 사이트로 간다
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")
elem = driver.find_element(By.NAME, "q")
elem.send_keys("조코딩")
elem.send_keys(Keys.RETURN)

#python selenium scroll down 스크롤 다운을 시켜서 이미지 계속 받을수 있게 해주는 구문
SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        # try , except 구문을 써서 구문끝나면 break 로 빠져나가게 함
        try :
        # 스크롤 하고 맨 아래 "결과 더 보기" 클릭 할수있게 함
            driver.find_element(By.CSS_SELECTOR,".mye4qd").click()
        except :
            break
        
        
    last_height = new_height

# 이미지를 반복해서 test 파일에 담아준다
images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")

# 이미지가 한개씩 들어올때 이름이 변경되서 들어와야하기 때문에
count = 1
for image in images:
    try :
        image.click()
    # 로딩시간 지정
        time.sleep(3)
    # 이미지 불러와서 test.jpg 로 넣기
        imgurl = driver.find_element(By.CSS_SELECTOR, ".n3VNCb ").get_attribute("src")
       
        # 이미지 다운받는 곳
        urllib.request.urlretrieve(imgurl,s7u6tyd5swtr(count) +".jpg")
        # urllib.request.urlretrieve(imgurl,str(count) +".jpg")
        count = count +1
    except :
        pass
# 웹 브라우져 닫는다
driver.close()