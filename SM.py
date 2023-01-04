import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver= webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("http://10.4.4.20:6122")
time.sleep(2)
driver.find_element(By.XPATH ,"//input[@placeholder='Enter Username']").send_keys("abc123")
time.sleep(2)
driver.find_element(By.XPATH ,"//input[@placeholder='Enter Password']").send_keys("pJPAiUshc541")
time.sleep(2)
driver.find_element(By.XPATH ,"//span[normalize-space()='Login']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[@class='p-button-label']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
time.sleep(3)