import time
#크롬 드라이버 옵션 설정
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
#로그인 정보 가져오기
import pandas as pd
works_login = pd.read_json("C:\\Users\\USER\\ve_1\\proj_web\db\\login.json",orient='records')

#크롬 드라이버 실행
url = "https://auth.worksmobile.com/login/login?accessUrl=https%3A%2F%2Fmail.worksmobile.com%2F"
driver.get(url)
driver.implicitly_wait(1)
#로그인 정보입력(아이디)
id_box = driver.find_element(By.CSS_SELECTOR,'#login_param')
login_button_1 = driver.find_element(By.CSS_SELECTOR,'#loginStart')
id = works_login['coochip']['id']
ActionChains(driver).send_keys_to_element(id_box, '{}'.format(id)).click(login_button_1).perform()
time.sleep(1)
#로그인 정보입력(비밀번호)
password_box = driver.find_element(By.CSS_SELECTOR,'#password')
login_button_2 = driver.find_element(By.CSS_SELECTOR,'#loginBtn')
password = works_login['coochip']['pw']
ActionChains(driver).send_keys_to_element(password_box, '{}'.format(password)).click(login_button_2).perform()
time.sleep(1)
#인증번호 전송
passingMail = driver.find_element(By.XPATH,'//button[@id="privateEmailButton"]')
ActionChains(driver).click(passingMail).perform()
time.sleep(1)
while True:
    #인증번호 검증
    if pd.read_json("C:\\Users\\USER\\ve_1\\proj_web\db\\sendMail.json",orient='records',dtype={"passnumber":str,"addr":str,"subaddr":str,"title":str,"main":str})['passnumber'].tolist()[-1] == 'test':
        time.sleep(0.5)
        pass
    else:
        #인증 진행
        email = pd.read_json("C:\\Users\\USER\\ve_1\\proj_web\db\\sendMail.json",orient='records',dtype={"passnumber":str,"addr":str,"subaddr":str,"title":str,"main":str})
        passingN = driver.find_element(By.XPATH,'//input[@class="_authNo _authNo1"]')
        passingnumber = email['passnumber'].tolist()[-1]
        ActionChains(driver).click(passingN).send_keys('{}'.format(passingnumber)).perform()
        time.sleep(1)
        #메일전송 페이지 전환
        driver.get('https://mail.worksmobile.com/#/compose?orderType=new')
        time.sleep(1)
        #수신자 입력
        address = driver.find_element(By.XPATH,'//input[@aria-label="받는사람"]')
        addrs = email['addr'].tolist()[-1]
        ActionChains(driver).send_keys_to_element(address, '{}'.format(addrs)).perform()
        time.sleep(1)
        #참조 입력
        subaddress = driver.find_element(By.XPATH,'//input[@aria-label="참조"]')
        subaddrs = email['subaddr'].tolist()[-1]
        ActionChains(driver).send_keys_to_element(subaddress, '{}'.format(subaddrs)).perform()
        time.sleep(1)
        #메일제목 입력
        mailtitle = driver.find_element(By.XPATH,'//input[@aria-label="제목"]')
        mtitle = email['title'].tolist()[-1]
        ActionChains(driver).click(mailtitle).send_keys_to_element(mailtitle,'{}'.format(mtitle)).perform()
        time.sleep(1)
        #메일내용 입력
        mailmain = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[3]/div[2]/div/fieldset/div/div/div/div[3]')
        mmain = email['main'].tolist()[-1]
        ActionChains(driver).click(mailmain).send_keys(Keys.PAGE_UP).send_keys('{}'.format(mmain)).perform()
        time.sleep(1)
        #전송 클릭_1
        send_button = driver.find_element(By.XPATH,'//button[@data-hotkey="sendKey"]')
        ActionChains(driver).click(send_button).perform()
        time.sleep(1)
        """
        #전송 클릭_2
        send_button = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div/h3/div/button[1]')
        ActionChains(driver).click(send_button).perform()
        time.sleep(1)
        """
        driver.quit()
        mailReset = {
            "passnumber":"test",
            "addr":"test_a",
            "subaddr":"test_s",
            "title":"test_t",
            "main":"test_m"
            }
        pd.DataFrame(mailReset,index=[0]).to_json('C:\\Users\\USER\\ve_1\\proj_web\\db\\sendMail.json',orient='records',force_ascii=False,indent=4)
        time.sleep(1)
        break