import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#invoking the browser with shopping website
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(3)

# 5 seconds is max timeout. page loads in 3  seconds(remaining 2 second is saved)
# Searching Vegetable using keyword 'ber'
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
#time.sleep(2)
# Adding all the items from the search list to cart
result = driver.find_elements(By.XPATH, "//div[@class='products']/div")

count = len(result)
assert count > 2
for res in result:
    res.find_element(By.XPATH, "div/button").click()
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
# Clicking on Proceed to Checkout
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

#Entering the promo code and adding explicit wait to load the promoInfo and printing it
driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[@class ='promoBtn']").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
