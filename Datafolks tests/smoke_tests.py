from selenium import webdriver


driver = webdriver.Firefox()
driver.get("https://www.datafolks.com")

logo = driver.find_element_by_class_name("tn-atom") #create variable for WebElement
assert logo.text =="DATAFOLKS"

main_text = driver.find_element_by_xpath("//div[@data-elem-id=1551634856822/h1")
assert main_text.text == "Quality code\n"
driver.quit()

