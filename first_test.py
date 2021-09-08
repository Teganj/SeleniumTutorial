import selenium.webdriver as webdriver
driver = webdriver.Firefox()

driver.get("https://docket-test.herokuapp.com/register")

driver.maximize_window()

driver.find_element_by_id("username").send_keys("Jack")
driver.find_element_by_id("email").send_keys("test@test.ie")
driver.find_element_by_id("password").send_keys("12345")
driver.find_element_by_id("password2").send_keys("12345")

driver.find_element_by_id("submit").click()

message = driver.find_element_by_xpath(
    "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]").text

assert message == "Congratulations, you are now registered"

current_url = driver.current_url

assert current_url == "https://docket-test.herokuapp.com/login"
