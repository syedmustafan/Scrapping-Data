"""
Printing the header text from the given URL on terminal
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://pakobserver.net")
#link = driver.find_element_by_link_text("CPEC and Environment: How bad is it? | By...")
#link.click()

main = driver.find_element_by_id("menu-main-menu-custom-1")
li = main.find_elements_by_tag_name("li")
for country in li:
    #header = country.find_element_by_class_name("menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children td-menu-item td-normal-menu menu-item-139762")
    print(country.text)
    print("test222")
    print("COmmit 1")
    print("COmmit 2")
    print("COmmit 3")
    print("COmiit 4")