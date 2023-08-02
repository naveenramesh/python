from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
opt = Options()
browser= Chrome(options=opt)
browser.get("www.google.com")