from selenium.webdriver import Chrome
from selenium.webdriver.remote.webdriver import By

path = "C:\\Users\\gutsg\\Downloads\\chromedriver_win32\\chromedriver.exe"

driver = Chrome(path)
driver.get("https://www.amazon.com/")

driver.maximize_window()

btn_signin = "//span[@id='nav-link-accountList-nav-line-1']"
txt_email = "//input[@type='email']"
btn_continue = "//input[@id='continue']"
txt_password = "//input[@type='password']"
btn_signInSubmit="//input[@id='signInSubmit']"
btn_notNow="//a[@id='ap-account-fixup-phone-skip-link']"
nav_all="//i[@class='hm-icon nav-sprite']"
nav_electronics="//a[@data-menu-id='5']"
nav_electronics_comp_accessories="//ul[@data-menu-id='5']/li[7]/a"
# driver.find_element_by_xpath(btn_signin).click()
driver.find_element(by=By.XPATH, value=btn_signin).click()
driver.find_element(by=By.XPATH, value=txt_email).clear()
driver.find_element(by=By.XPATH,value=txt_email).send_keys("sreelakshmi10.g@gmail.com")
driver.find_element(by=By.XPATH,value=btn_continue).click()
driver.find_element(by=By.XPATH,value=txt_password).send_keys("Sree@123")
driver.find_element(by=By.XPATH,value=btn_signInSubmit).click()
# driver.find_element(by=By.XPATH,value=btn_notNow).click()
driver.find_element(by=By.XPATH,value=nav_all).click()
driver.find_element(by=By.XPATH,value=nav_electronics).click()
# sleep(100)
# driver.find_element(by=By.XPATH,value=nav_electronics_comp_accessories).click()




driver.close()