from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#serv_object = Service("C:\\Users\\ajinkyac\\Downloads\\Drivers\\chromedriver.exe")
driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.ID,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR,"input#btnLogin.button").click()

actual_title = driver.title
expected_title = "OrangeHRM"
if actual_title==expected_title:
    print("Title is correct")
else:
    print("Title is wrong")

driver.close()





