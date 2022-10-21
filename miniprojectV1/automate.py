from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import subprocess
import time
cmd = 'python locator.py'
p = subprocess.Popen(cmd, shell=True)
time.sleep(3)
f = open('cord.txt', 'rt')
content = f.read()
f.close()
x = webdriver.Chrome()
act = ActionChains(x)
x.get('https://www.google.com/maps/@11.0395392,77.0277376,12z')
time.sleep(3)
mode = x.find_element_by_xpath('/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div/button/img')
mode.click()
time.sleep(4)
start = x.find_element_by_xpath('/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input')
start.send_keys('Eshwar collge of engineering')
time.sleep(4)
act.send_keys(Keys.TAB).perform()
act.send_keys(Keys.TAB).perform()
end = x.find_element_by_xpath('//*[@id="sb_ifc52"]/input')
end.send_keys('KMCH coimbatore')
act.send_keys(Keys.ENTER).perform()
