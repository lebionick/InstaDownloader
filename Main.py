from selenium import webdriver
#from selenium.webdriver.common.by import By
import urllib
import time

#account_name = input('Enter acc name: ')
account_name = 'shch_anya'
instaUrl = 'https://www.instagram.com/'
accUrl = instaUrl + account_name

driver = webdriver.Chrome('drivers/chromedriver')
driver.get(accUrl)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

aslist = driver.find_elements_by_tag_name('a')
for i in aslist:
    if '?max_id=' in str(i.get_attribute('href')):
        i.click()

aslist = None
for it in range(2):
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

aslist = driver.find_elements_by_tag_name('a')
#input()
print('hrefs:')
for i,v in enumerate(aslist):
    aslist[i] = v.get_attribute('href')
    print(aslist[i])

for href in aslist:
    if not str(href).endswith('taken-by='+str(account_name)):
        continue

    driver.get(str(href))
    imgslist = driver.find_elements_by_tag_name('img')
    print('imgs:')
    for i,v in enumerate(imgslist):
        imgslist[i] = v.get_attribute('src')
        print(imgslist[i])

    for i in imgslist:
        urllib.request.urlretrieve(i,"images/" + str(i[-26:-4]).replace('/','+')+".png")
