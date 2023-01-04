from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class loginelements(BasePage):
  username=(By.XPATH ,"//input[@placeholder='Enter Username']")
  password=(By.XPATH," //input[@placeholder='Enter Password']")
  loginbtn=(By.XPATH ,"//span[normalize-space()='Login']")
  options=(By.XPATH, "//span[@class='p-button-label']")
  logout=(By.XPATH, "//a[normalize-space()='Logout']")
  #sdddssss















#time.sleep(3)
#driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()

#driver.find_element(By.XPATH,"").click()
#time.sleep(3)
#driver.find_element(By.XPATH,"//span[@class='p-checkbox-icon pi pi-check']").click()
#time.sleep(3)
#driver.find_element(By.XPATH,"//span[@class='p-checkbox-icon pi pi-check']").click()
#time.sleep(3)
#driver.find_element(By.XPATH, "//button[@class='p-button p-button-info btn-150 m-auto']").click()
#time.sleep(3)