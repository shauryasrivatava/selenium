import os
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import base64

# step 0 : you need chrome for this. Also install modules :
# pip install selenium && pip install webdriver_manager && pip install tinydb
options = webdriver.ChromeOptions()
#uncomment the code below if you want to login via storing cache memory
# options.add_argument("user-data-dir={}\driver_data".format(os.getcwd()))

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
user="xyz@abc.com" #mail or ph.number
pas="****" #password
driver.get("https://linkedin.com/login")
sleep(2)
driver.find_element_by_id("username").send_keys(user)
driver.find_element_by_id("password").send_keys(base64.b64decode(pas.encode('ascii')).decode('ascii'))
driver.find_element_by_id("password").send_keys(Keys.RETURN)
# driver.find_element_by_class_name("btn__primary--large").click()
sleep(2)


driver.get("https://www.linkedin.com/mynetwork/invitation-manager/")
sleep(3)

buttons = driver.find_elements_by_class_name("invitation-card__action-btn")
for button in buttons:
    label = button.get_attribute("aria-label")
    word = label.split(' ')[0]
    if word == "Accept":
        print("Clicking...")
        button.click()
        sleep(2)
        print("Clicked!")
print("Done!")

driver.close()
