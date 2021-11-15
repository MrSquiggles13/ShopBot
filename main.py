from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import os

####Login to site####
PATH = "/Users/commanderspectre/PycharmProjects/Terp SlurperMale/chromedriver"
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=PATH)
driver = webdriver.Chrome(PATH)
#Go to main page
driver.get("https://toroglassgallery.com")
action = ActionChains(driver)

time.sleep(1)
#Click login on main page
driver.find_element_by_xpath("/html/body/header/div[2]/div[1]/nav/ul[2]/li/a").click()
#Type out user name
driver.find_element_by_xpath("/html/body/main/section/article/div[1]/form/div[1]/input").send_keys("ayresguitar@gmail.com")
#Type out password
driver.find_element_by_xpath("/html/body/main/section/article/div[1]/form/div[2]/input").send_keys("Ql@zz@ru$13@" + Keys.RETURN)

time.sleep(1)

#Terp Slurper Male
driver.execute_script("window.open('https://toroglassgallery.com/collections/terp-slurper/products/mini-terp-slurper-male');")
#Test with t-shirts
#driver.execute_script("window.open('https://toroglassgallery.com/collections/apparel/products/t-shirts-toro-script?variant=37775248490682')")
#Mini Terp Slurper Male
#driver.execute_script("window.open('https://toroglassgallery.com/collections/terp-slurper/products/terp-slurper-xl-barrel')")
#Switch to new tab
driver.switch_to_window(driver.window_handles[1])

while True:

    time.sleep(1)
    try:
        #check if there is an add to cart button
        driver.find_element_by_xpath("/html/body/main/div/section/article/div[2]/div[2]/div/form/div[2]/button/span[1]")
        #if there is click it bruh
        driver.find_element_by_class_name("atc-button--text").click()

        time.sleep(1)
        #find checkout button on next page and click it
        driver.find_element_by_name("checkout").click()

        #uncheck marketing box
        driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/form/div[1]/div[1]/div[2]/div[2]/div/div/input[2]").click()
        #first name on shipping
        #driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[1]/div/input").send_keys("Michael")
        #last name on shipping
        #driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[2]/div/input").send_keys("Ayres")
        #street for shipping
        driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[3]/div/input").send_keys("19 Donovan Street")
        #City for shipping
        driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[5]/div/input").send_keys("Pittsfield")
        #select state for shipping from drop down
        driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[7]/div/select/option[27]").click()
        #zip code for shipping
        driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[8]/div/input").send_keys("01201")
        #submit shipping info
        driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/form/div[2]/button").click()
        time.sleep(1)
        #click go to payment info button
        driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/form/div[2]/button").click()
        time.sleep(2)
        #input card number for payment info
        driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div[3]/div[1]/div/div[1]/iframe").send_keys("1111000012344321")
        #input name on card for payment info
        driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div[3]/div[2]/div/div/iframe").send_keys("Michael Ayres")
        #input card exipration for payment info
        driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div[3]/div[3]/div/div/iframe").send_keys("1223")
        #input card CVV for payment info
        driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div[3]/div[4]/div/div[1]/iframe").send_keys("333")
        #click pay now button
        driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/div/form/div[3]/div[1]/button").click()

        break
    except:
        driver.refresh()
        #print("I dont know man something happened")
