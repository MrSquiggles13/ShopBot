from multiprocessing.dummy import Pool as ThreadPool
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


def openTargetTab(webElement, driver):
    print("Opening New Tab...\n")
    driver.execute_script("window.open('" + webElement + "');")

    # Switch to new tab
    driver.switch_to.window(driver.window_handles[1])

    while True:

        driver.refresh()
        try:
            print("Checking if available...\n")
            # check if there is an add to cart button
            driver.find_element_by_xpath(
                "/html/body/main/div/section/article/div[2]/div[2]/div/form/div[2]/button/span[1]")
            # if there is click it bruh
            driver.find_element_by_class_name("atc-button--text").click()
            time.sleep(1)
            # find checkout button on next page and click it
            driver.find_element_by_name("checkout").click()
            print("*In Cart*\n")
            time.sleep(1)
            print("Filling out shipping info...\n")
            # uncheck marketing box
            driver.find_element_by_xpath(
                "/html/body/div/div/div/main/div[1]/form/div[1]/div[1]/div[2]/div[2]/div/div/input[2]").click()
            # first name on shipping
            # driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[1]/div/input").send_keys("Michael")
            # last name on shipping
            # driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[2]/div/input").send_keys("Ayres")
            # street for shipping
            driver.find_element_by_xpath(
                "/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[3]/div/input").send_keys(street)
            # City for shipping
            driver.find_element_by_xpath(
                "/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[5]/div/input").send_keys(
                city)
            # select state for shipping from drop down
            if state == "PA":
                driver.find_element_by_xpath(
                "/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[7]/div/select/option[46]").click()
            elif state == "MA":
                driver.find_element_by_xpath(
                    "/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[7]/div/select/option[27]").click()
            # zip code for shipping
            driver.find_element_by_xpath(
                "/html/body/div/div/div/main/div[1]/form/div[1]/div[2]/div[2]/div/div/div[8]/div/input").send_keys(
                zip)
            # submit shipping info
            driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/form/div[2]/button").click()
            time.sleep(1)
            # click go to payment info button
            driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/form/div[2]/button").click()
            time.sleep(1)
            print("Filling out payment info...\n")
            # input card number for payment info
            element = driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div[3]/div[1]/div/div[1]/iframe")
            for char in card_number:
                element.send_keys(char)

            # input name on card for payment info
            driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div[3]/div[2]/div/div/iframe").send_keys(card_name)
            # input card expiration for payment info
            element = driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div[3]/div[3]/div/div/iframe")
            for char in card_expiration:
                element.send_keys(char)
            # input card CVV for payment info
            driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/div/form/div[1]/div[2]/div[2]/div/div[3]/div[3]/div[4]/div/div[1]/iframe").send_keys(card_CVV)
            # click pay now button
            driver.find_element_by_xpath("/html/body/div/div/div/main/div[1]/div/form/div[3]/div[1]/button").click()
            print("Done")
            break
        except:
            print("Refreshing\n")


def login(driver):
    ####Login to site###
    print("Opening Main Page...\n")
    # Go to main page
    driver.get("https://toroglassgallery.com")

    print("Logging in...\n")
    # Click login on main page
    driver.find_element_by_xpath("/html/body/header/div[2]/div[1]/nav/ul[2]/li/a").click()
    # Type out user name
    driver.find_element_by_xpath("/html/body/main/section/article/div[1]/form/div[1]/input").send_keys(
        username)
    # Type out password
    driver.find_element_by_xpath("/html/body/main/section/article/div[1]/form/div[2]/input").send_keys(
        password + Keys.RETURN)

def start(page):
    driver = webdriver.Chrome()
    login(driver)
    input("                         ****Press Enter When Done Logging In****")
    openTargetTab(page, driver)


#page = input("Enter target site: ")
pay_info = []
file = open("C:Users\chris\OneDrive\Desktop\getMeAToro\pay_info.txt").read().split('\n')

for line in file:
    pay_info.append(line)


username = pay_info[0] #"ayresguitar@gmail.com"
password = pay_info[1] #"Ql@zz@ru$13@"

page = "https://toroglassgallery.com/collections/terp-slurper/products/terp-slurper-xl-barrel"


street = pay_info[2] #"58 West Summit St Apt B"
city = pay_info[3] #"Souderton"
state = pay_info[4] #"PA"
zip = pay_info[5] #"18967"

card_number = pay_info[6] #"1234123412341234"
card_name = pay_info[7] #"Michael Ayres"
card_expiration = pay_info[8] #"1223"
card_CVV = pay_info[9] #"123"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=
start(page)