from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities


# chrome_capabilities = {
#     "browserName": "chrome",
#     "version": "firefox",
#     "platform": "ANY",
#     "javascriptEnabled": True,
# }
dr = webdriver.Remote(
                      desired_capabilities=DesiredCapabilities.CHROME.copy()
                      )
dr.get("https://www.baidu.com")
dr.find_element(By.ID, "kw").send_keys("selenium grid4")
dr.find_element(By.ID, "su").click()
dr.close()
