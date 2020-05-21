#Choose from Most Relevent,Newest and Ratings
option_r="Newest"

## find comment below in Ratings section to filter by ratings

from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
options = webdriver.ChromeOptions()

options.add_argument('--headless')
#edit the chromedriver path to path in your PC
driver = webdriver.Chrome(executable_path=r'C:/Users/saini/Downloads/chromedriver_win32/chromedriver.exe',chrome_options=options)
driver.maximize_window()
driver.delete_all_cookies()
url = 'https://play.google.com/store/apps/details?id=com.zhiliaoapp.musically&hl=en&showAllReviews=true' #Link to play store app
driver.get(url)
print("Ready!")

#filters for Most Relevent,Newest and Ratings
state_selection = driver.find_element_by_xpath("//div[.='%s']" % "Most relevant")
state_selection.click()
WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "//div[@role='option']/span[contains(text(),option_r)]"))).click()
time.sleep(1)
driver.execute_script("window.scrollTo(0, 160)")


#filters for Rating type
state_selection2 = driver.find_element_by_xpath("//div[.='%s']" % "All Ratings")
state_selection2.click()
####replace numeric in ** /span[contains(text(),'2' ** in next line with the ratings you want to sort with.. Possible options [1,2,3,4,5,All]
WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "//div[@role='option']/span[contains(text(),'2')]"))).click()
time.sleep(1)


html = driver.find_element_by_tag_name('html')
print("Scrolling to bottom!")
start_time = time.time()
while ((time.time() - start_time)<10):#time to reach bottom of page
    print(10-(time.time() - start_time))
    html.send_keys(Keys.END)
html2 = driver.page_source
soup = BeautifulSoup(html2, 'lxml')

print("Your results are ready!")
print("********************************")
print("                                ")
div = soup.find_all('div', {'class': 'd15Mdf bAhLNe'})

#here I've printed name,ratings and reviews. You can save it to csv as per your requirements.
for i in div:
    print(i.find('div', {'class': 'xKpxId zc7KVe'}).find('span', {'class': 'X43Kjb'}).text) #name
    print(i.find('div', {'class': 'xKpxId zc7KVe'}).find('div',{'class': 'pf5lIe'}).find('div')['aria-label'])#ratings
    print(i.find('div', {'class': 'UD7Dzf'}).find('span', {'jsname':'bN97Pc'}).text) #review