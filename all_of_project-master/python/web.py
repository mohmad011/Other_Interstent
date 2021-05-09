from selenium import webdriver

url = "https://www.youtube.com/watch?v=p0nHbX_H3to&list=PL1FWK-sgJ9el-axKTMU_1l5PEyv7tn-wk"

# url = "Name Of Chanel"

browser = webdriver.Chrome()

# browser = webdriver.Chrome() To Open The Browser

browser.get(url)

# browser.get(url) Will Go To The Name Of Chanel

browser.find_element_by_xpath('//*[@id="thumbnail"]').click()

# This Will Click On The Choosen Video