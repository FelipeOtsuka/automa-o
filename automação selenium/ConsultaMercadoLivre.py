from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get ("https://www.mercadolivre.com.br/")

time.sleep(3)

log = browser.get("https://www.mercadolivre.com/jms/mlb/lgz/login?platform_id=ML&go=https%3A%2F%2Fwww.mercadolivre.com.br%2F&loginType=explicit#nav-header")

time.sleep(3)



time .sleep(10)

busca = browser.find_element_by_name("as_word")
busca.send_keys("playstation")
busca.submit()

time.sleep(3)

order = browser.find_element_by_class_name("andes-dropdown__standalone-arrow")
order.click()

time.sleep(3)

lowerprice = browser.find_element_by_xpath("//div[contains(text(),'Menor preço')]")
lowerprice.click()

time.sleep(3)

product = browser.find_element_by_class_name("ui-search-layout__item")
product.click()

time.sleep(3)

kart = browser.find_element_by_class_name("andes-button__content")
kart.click()

time.sleep(3)

