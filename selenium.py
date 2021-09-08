import time
from selenium import webdriver
driver = webdriver.Firefox()  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');
time.sleep(2) # Let the user actually see something!
agree_btn = driver.find_element_by_id('zV9nZe')
agree_btn.click()
time.sleep(2) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('Keyboard Cat')
search_box.submit()
time.sleep(2) # Let the user actually see something!
driver.quit()
